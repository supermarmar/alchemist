# Batch 23 report

Nodes written: 20
Nodes written from articles: 4
Nodes written without: 16
Nodes not landed: 20

## Nodes

- hypergeometric-distribution: sources: stub and anchor only. spends: none. No collision. No split.
- identity-initialisation: sources: stub and anchor only. spends: none. No collision. No split.
- individual-conditional-expectation: sources: methods/icenet-smoothness-and-monotonicity-constraints. spends: obj.response-mean:ml. No collision. No split.
- inflation-adjusted-chain-ladder: sources: stub, anchor and chain-ladder (prerequisite). spends: obj.cohort-index:gi, obj.development-index:gi, obj.development-factor:gi, obj.ultimate:gi. No collision. No split.
- insurance-application-of-utility-theory: sources: stub and anchor only, built on utility-function and risk-aversion (prerequisites). spends: none. No collision. No split.
- integration-by-substitution: sources: stub and anchor only. spends: none. No collision. No split.
- integration-techniques: sources: stub and anchor only. spends: none. No collision. Split candidate: could become integration-by-parts and partial-fractions, no sibling node exists yet for either.
- interest-rate-swap-hedging: sources: stub and anchor only, built on swaps-hedging (prerequisite). spends: none. No collision. No split.
- investment-guarantee-cost-methods: sources: stub and anchor only; embedded-options-and-guarantees (prerequisite) checked and carries no costing formula, so this node owns both the option and simulation expressions. spends: none. No collision. No split.
- investment-risk-budgeting: sources: stub and anchor only; value-at-risk (prerequisite) checked and carries no formula yet, so this node owns the component-VaR expression as its own object, distinct from plain VaR. spends: none. No collision. No split.
- internal-models-approach-market-risk: sources: regulation/frtb-minimum-capital-market-risk. spends: none. No collision. No split. Note: the node's stub and anchor fix scope as the legacy VaR-based IMA (Basel 1996 amendment/BCBS d352 predecessor), which is what the page writes; the vault article is FRTB (d457), the expected-shortfall-based successor, and is used only for the "why this node exists" forward reference to fundamental-review-trading-book. Flagging this divergence between stub scope and vault article scope for Mario's attention.
- joint-life-annuity-and-assurance: sources: stub and anchor only, built on annuity-function and assurance-function (prerequisites, both name this node as their unlock). spends: obj.survival:life, obj.discount-factor:life. No collision. No split.
- lasso-regularisation: sources: methods/icenet-smoothness-and-monotonicity-constraints; regularisation (prerequisite). spends: obj.regularisation:ml, obj.regularisation:stats, obj.coefficients:stats. No collision. No split.
- layer-normalisation: sources: stub and anchor only. spends: none (mu is a within-slice mean, not obj.response-mean). No collision. No split.
- lhopitals-rule: sources: stub and anchor only. spends: none. No collision. No split.
- linear-combinations-and-span: sources: stub and anchor only. spends: none. No collision. No split.
- liquidity-risk-factor: sources: regulation/bcbs-liquidity-coverage-ratio-original (used to confirm the haircut concept generally, no specific numeric haircut asserted); sources-of-liquidity (prerequisite). spends: none. No collision. No split.
- loan-behavioural-tenor: sources: stub and anchor only; prepayment-behaviour-modelling (prerequisite) checked, carries no formula of its own, so the weighted-average-life expression is this node's own object. spends: none. No collision. No split.
- loan-to-deposit-ratio: sources: stub and anchor only. spends: none. No collision. No split.
- local-regression: sources: stub and anchor only; linear-regression (prerequisite). spends: obj.coefficients:stats. No collision. No split.

## Not landed

- historical-data-adjustment-for-expected-credit-losses: qualitative: an IFRS 9 process requirement (adjust historical loss experience for current and forecast conditions), carries no formula of its own.
- impairment-versus-default: qualitative: a comparison of two definitional tests (accounting impairment versus regulatory default), no formula distinguishes them.
- inflation-causes-and-costs: qualitative: a survey of causes and costs of inflation; the quantitative demand/supply and money-supply relationships belong to the sibling nodes aggregate-demand-and-supply and money-supply-effect-on-output-and-prices.
- internal-liquidity-adequacy-assessment-process: qualitative: a firm-led governance and documentation process (confirmed against regulation/pra-ilaap), no formula.
- investment-bank-products: qualitative: a survey of product lines (underwriting, trading, advisory, capital markets), no single formula.
- investment-banking-loan-pricing: qualitative: structural pricing considerations for transaction-specific lending; the base pricing formula belongs to the sibling node risk-based-pricing, which is itself still a stub.
- investment-environment-influences: qualitative: a survey of macroeconomic and institutional influences on the investment environment, no formula.
- inwards-reinsurance-reserving: qualitative: reserving considerations specific to inwards reinsurance data and loss emergence; the chain ladder formula itself belongs to the sibling node chain-ladder, already drafted.
- irb-corporate-governance-and-oversight: qualitative: board, senior management and control-function responsibilities under BCBS d424 (confirmed against regulation/bcbs-credit-risk-principles), no formula.
- irb-disclosure-requirements: qualitative: a Pillar 3 disclosure eligibility requirement (confirmed against regulation/pillar-3-disclosure-framework), no formula.
- irb-rating-system-definition: qualitative: definitional requirements for a qualifying rating system (borrower versus transaction risk, pooling), no formula.
- irb-risk-quantification-general-standards: qualitative: general data and conservatism standards for PD/LGD/EAD estimation (confirmed against regulation/eba-pd-lgd-estimation-framework), no single formula; the margin-of-conservatism mechanism is qualitative even where individual risk parameters are quantitative elsewhere in the corpus.
- irb-validation-requirements: qualitative: a validation process requirement assessed through several named statistics (accuracy ratio, binomial backtest) rather than one defining formula (confirmed against methods/irb-model-validation-and-rating-system-quality and regulation/irb-model-validation).
- leverage-ratio-general-exposure-measurement-principles: qualitative: general scope and deduction principles for the exposure measure; the defining formula LR = T1/E belongs to the sibling node leverage-ratio, already drafted.
- lgd-foundation-approach-other-collateral: uncertain: the BCBS d424 blended LGD formula for real estate and receivables collateral (LGD_U, LGD_S, haircut H_C) could not be confirmed against any vault source; grepping the vault for E_S, H_C and LGD_S found no matching article, so the formula is not written from memory.
- liability-valuation: qualitative: a survey of valuation purposes and how each shapes methodology and assumption choice, no single formula fits across GI, life and actuarial uses.
- life-insurance-investment-principles: qualitative: a survey of asset-liability matching and investment principles, no formula.
- loss-allowance-recognition: qualitative: a scope requirement over which financial instruments attract a loss allowance; the ECL formula combining PD, LGD and EAD belongs to the sibling node expected-credit-loss (confirmed against concepts/ifrs9-expected-credit-loss, which states "the ECL formula combines PD, LGD, and EAD components").
- market-and-systemic-risk-funding: qualitative: a survey of how market risk stress spills into funding and systemic risk, no formula.
- maximum-contractual-period-for-expected-credit-losses: qualitative: an accounting policy cap on the measurement horizon, no formula.
