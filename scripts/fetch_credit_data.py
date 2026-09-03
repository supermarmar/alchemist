"""Convert the Bondora loan book CSV in data/ to typed parquet files.

Input (local only, gitignored, never committed):
    data/LoanData_Bondora.csv    Bondora P2P loan book, 179,235 loans, extract
                                  dated 2021-07-20, downloaded from
                                  https://www.bondora.com/en/public-reports

Outputs (all under the gitignored data/):
    data/bondora_raw.parquet       faithful typed conversion, no rows dropped
    data/bondora_pd.parquet        the fixed-horizon modelling table: seasoned
                                    loans, application-time features, and a
                                    12-month default flag
    data/bondora_survival.parquet  the survival table the S-series lectures
                                    read: every loan, its observed duration,
                                    and how it left the risk set

`lectures/S1_credit-survival-bridge.qmd` reads both `bondora_survival.parquet`
and `bondora_pd.parquet`, joining the two on LoanId to compare its
cumulative-incidence estimate against lecture 1's observed 12-month default
rate. Keep both functions even where only the survival table looks needed at
a glance.

Typing strategy: the CSV encodes missing values as empty strings and writes
decimals like ".6800", so whole-file schema inference leaves 81 of 112 columns
as strings. After replacing empty strings with nulls, each remaining string
column is cast to Date, Datetime, Int64 or Float64 in that order of
preference, and a cast is adopted only when it parses every non-null value.
Genuine label columns (Rating, Status, WorkExperience, ...) survive as strings
because no cast wins losslessly.

The fixed-horizon table keeps application-time information only. Everything
Bondora records after origination is excluded by construction, because those
columns leak the outcome into the covariates: Status, DefaultDate,
ActiveLateCategory, WorseLateCategory, CurrentDebtDays*, DebtOccuredOn*, the
payment and balance columns (PrincipalBalance, *PaymentsMade, *WriteOffs,
*Overdue*, *PostDefault, *TillDate, *DebtServicingCost), the recovery columns
(EAD1, EAD2, *Recovery, RecoveryStage, StageActiveSince, GracePeriod*,
ReScheduledOn, Restructured, NextPayment*, NrOfScheduledPayments,
LastPaymentOn, ContractEndDate, MaturityDate_Last), and Bondora's own model
outputs computed over the life of the loan (ExpectedLoss, LossGivenDefault,
ExpectedReturn, ProbabilityOfDefault, EL_V0/V1, Rating_V0/V1/V2,
ModelVersion). Rating itself is kept: it is assigned at listing time.

Target definition: default_12m = 1 where DefaultDate (Bondora's own platform
flag) falls within 365 days of LoanDate, on loans originated at least 365 days
before the newest origination date in the file, so that every kept loan has a
complete 12-month observation window.

Survival table: bondora_survival.parquet answers a different question and so
takes a different shape. It keeps all 179,235 loans rather than the seasoned
subset, because a survival likelihood wants a short-seasoned loan as a
censored observation rather than as a dropped one, and it records when each
loan left the risk set rather than whether it defaulted inside a fixed window.
Exits are encoded three ways. A loan exits as `default` on its DefaultDate,
which takes precedence over Status, since some Repaid loans carry a
DefaultDate, having defaulted and later recovered, and default is absorbing.
A loan exits as `settled` where Status is Repaid and no DefaultDate exists, on
its ContractEndDate. Everything else is `censored` at ReportAsOfEOD.
Settlement is a competing risk rather than censoring, which is why the exit
kind travels in the file: a table carrying only the binary event indicator
would have baked prepayment-as-censoring into the data irreversibly.

ContractEndDate is on the leakage exclusion list above and is nonetheless read
here, deliberately. The exclusion protects a fixed-horizon target, where
knowing when the loan ended leaks the outcome into the covariates. A survival
model's response IS the exit time, so the same column is the response rather
than a covariate. It never enters the survival table as a feature; only the
derived duration and exit kind do.

Run with the project environment:
    .venv/bin/python scripts/fetch_credit_data.py
"""

from pathlib import Path

import polars as pl

DATA = Path(__file__).resolve().parent.parent / "data"

DATE_FORMATS = ["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]

# Application-time columns for the modelling table, grouped as in the Bondora
# data dictionary. LoanId, LoanNumber and LoanDate come along as identifiers
# and vintage, not as covariates.
APPLICATION_COLUMNS = [
    # loan terms as listed
    "AppliedAmount", "Amount", "Interest", "LoanDuration", "MonthlyPayment",
    "UseOfLoan", "Rating",
    # borrower demographics
    "Age", "Gender", "Country", "County", "City", "LanguageCode",
    "Education", "MaritalStatus", "NrOfDependants",
    # employment and income
    "EmploymentStatus", "EmploymentDurationCurrentEmployer",
    "EmploymentPosition", "WorkExperience", "OccupationArea",
    "HomeOwnershipType",
    "IncomeFromPrincipalEmployer", "IncomeFromPension",
    "IncomeFromFamilyAllowance", "IncomeFromSocialWelfare",
    "IncomeFromLeavePay", "IncomeFromChildSupport", "IncomeOther",
    "IncomeTotal",
    # liabilities and affordability
    "ExistingLiabilities", "LiabilitiesTotal", "RefinanceLiabilities",
    "DebtToIncome", "FreeCash",
    # application metadata and credit history on the platform
    "VerificationType", "NewCreditCustomer",
    "ApplicationSignedHour", "ApplicationSignedWeekday", "MonthlyPaymentDay",
    "NoOfPreviousLoansBeforeLoan", "AmountOfPreviousLoansBeforeLoan",
    "PreviousRepaymentsBeforeLoan", "PreviousEarlyRepaymentsBefoleLoan",
    "PreviousEarlyRepaymentsCountBeforeLoan",
]


def _lossless_cast(s: pl.Series) -> pl.Series:
    """Return s cast to the strictest type that parses every non-null value."""
    non_null = s.drop_nulls()
    if non_null.is_empty():
        return s
    for fmt in DATE_FORMATS:
        parsed = non_null.str.to_datetime(fmt, strict=False)
        if parsed.null_count() == 0:
            if fmt == "%Y-%m-%d":
                return s.str.to_date(fmt, strict=False)
            return s.str.to_datetime(fmt, strict=False)
    as_float = non_null.cast(pl.Float64, strict=False)
    if as_float.null_count() == 0:
        cast = s.cast(pl.Float64, strict=False)
        if (as_float == as_float.round(0)).all() and (as_float.abs() < 2**62).all():
            return cast.cast(pl.Int64)
        return cast
    return s


def convert_bondora_raw() -> pl.DataFrame:
    df = pl.read_csv(DATA / "LoanData_Bondora.csv", infer_schema_length=None)
    empties_to_null = [
        pl.col(c).replace("", None) for c, t in df.schema.items() if t == pl.String
    ]
    df = df.with_columns(empties_to_null)
    df = df.with_columns(
        [_lossless_cast(df[c]) for c, t in df.schema.items() if t == pl.String]
    )
    df.write_parquet(DATA / "bondora_raw.parquet")
    return df


def build_bondora_pd(raw: pl.DataFrame) -> pl.DataFrame:
    horizon_end = raw["LoanDate"].max()
    df = (
        raw.filter(pl.col("LoanDate") + pl.duration(days=365) <= horizon_end)
        .with_columns(
            default_12m=(
                (pl.col("DefaultDate") - pl.col("LoanDate")).dt.total_days() <= 365
            )
            .fill_null(False)
            .cast(pl.Int8),
            # data cleaning: 53 seasoned loans carry Age below Bondora's minimum of 18
            Age=pl.when(pl.col("Age") >= 18).then(pl.col("Age")),
        )
        .select(["LoanId", "LoanNumber", "LoanDate", *APPLICATION_COLUMNS, "default_12m"])
    )
    df.write_parquet(DATA / "bondora_pd.parquet")
    return df


# Mean Gregorian month in days, matching the convention lecture 1 uses to turn
# date differences into months on book.
MONTH = 30.4375


def build_bondora_survival(raw: pl.DataFrame) -> pl.DataFrame:
    """Build the survival table: one row per loan, with its exit time and kind.

    Unlike bondora_pd.parquet this keeps every loan, because a survival
    likelihood wants the short-seasoned loans as censored observations rather
    than dropped ones. See the module docstring for the exit encoding and for
    why ContractEndDate is admitted here after being excluded there.

    Args:
        raw: the faithful conversion written by convert_bondora_raw.

    Returns:
        One row per loan: identifiers, vintage, the observed duration in months
        and in whole months, the exit kind, the event indicator, the available
        observation window, and the application covariates.
    """
    tau = raw["ReportAsOfEOD"][0]
    defaulted = pl.col("DefaultDate").is_not_null()
    repaid = pl.col("Status") == "Repaid"

    df = (
        raw.with_columns(
            exit_kind=pl.when(defaulted)
            .then(pl.lit("default"))
            .when(repaid)
            .then(pl.lit("settled"))
            .otherwise(pl.lit("censored")),
            # Defaults exit on DefaultDate whatever Status says afterwards.
            # Settlements exit on the contract end, falling back to the
            # original maturity for the small number of repaid loans that
            # carry no end date. Everything else is still at risk and is
            # censored at tau.
            exit_date=pl.when(defaulted)
            .then(pl.col("DefaultDate"))
            .when(repaid)
            .then(pl.coalesce(["ContractEndDate", "MaturityDate_Original"]))
            .otherwise(pl.lit(tau)),
            # data cleaning: 53 loans carry Age below Bondora's minimum of 18
            Age=pl.when(pl.col("Age") >= 18).then(pl.col("Age")),
        )
        # Some settled loans carry an end date after the snapshot, i.e. a
        # scheduled date rather than the actual early repayment. Capping at
        # tau is the longest exposure consistent with the loan having ended
        # by then.
        .with_columns(exit_date=pl.min_horizontal("exit_date", pl.lit(tau)))
        .with_columns(
            t_obs=(pl.col("exit_date") - pl.col("LoanDate")).dt.total_days() / MONTH,
            A=(pl.lit(tau) - pl.col("LoanDate")).dt.total_days() / MONTH,
            delta=(pl.col("exit_kind") == "default").cast(pl.Int8),
        )
        # Whole months at risk, floored at 1: a loan exiting inside its first
        # month still contributes that month to the discrete-time risk set.
        .with_columns(t_obs_m=pl.col("t_obs").ceil().clip(lower_bound=1).cast(pl.Int32))
        .select(
            [
                "LoanId", "LoanNumber", "LoanDate",
                "t_obs", "t_obs_m", "exit_kind", "delta", "A", "Status",
                *APPLICATION_COLUMNS,
            ]
        )
    )
    df.write_parquet(DATA / "bondora_survival.parquet")
    return df


def main() -> None:
    raw = convert_bondora_raw()
    print(f"bondora_raw.parquet: {raw.shape}")
    pd_table = build_bondora_pd(raw)
    rate = pd_table["default_12m"].mean()
    print(f"bondora_pd.parquet: {pd_table.shape}, default_12m rate {rate:.4f}")
    surv = build_bondora_survival(raw)
    kinds = surv["exit_kind"].value_counts().sort("count", descending=True)
    counts = ", ".join(f"{k} {n:,}" for k, n in kinds.iter_rows())
    print(f"bondora_survival.parquet: {surv.shape}, {counts}")


if __name__ == "__main__":
    main()
