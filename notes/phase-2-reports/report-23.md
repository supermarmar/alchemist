# Phase 2 batch 23 attachment report

40 nodes worked. 22 attached, 18 uncovered. 26 total attachments.

## Attached

### link-function
Candidates: `methods/exponential-dispersion-family-and-glm` (open, matches directly).
Attached: `methods/exponential-dispersion-family-and-glm`. Its "Link choice and what the canonical link buys" section states the definition verbatim: "A generalised linear model applies a smooth, strictly increasing link g to the mean and sets g(mu(X)) equal to a linear combination of the covariates."

### liquid-asset-buffer
Candidates: `regulation/bcbs-liquidity-coverage-ratio-original` (open, matches the definition half), `regulation/pra-ilaap` (open, matches the stress-drawdown half).
Attached both. The LCR article defines the numerator as "unencumbered assets that can be converted into cash rapidly and reliably through sale or repo in private markets, even under stressed conditions", the stock the node describes. `pra-ilaap` covers the "draw on if a liquidity stress materialises" half: SS24/15 Chapter 4 "addresses conditions for LAB drawdown: firms may draw on their LAB in a stress event, but only with PRA agreement." Definition plus use, from two articles that do not overlap.

### liquidity-adequacy-regulatory-requirements
Candidates: `regulation/pra-ilaap` (open, matches the UK and EU legs).
Attached: `regulation/pra-ilaap`. States UK SS24/15 requirements in full and references the EU legs directly: "The EBA's 2016 guidelines (EBA/GL/2016/10) established the harmonised EU-wide ILAAP information framework" and the ECB SSM Guide's seven principles. Partial-scope limit: the node wants a four-way EU/UK/US/South Africa comparison; this article gives only the UK and EU legs. US and South Africa are ledgered.

### liquidity-contingency-plan
Candidates: `regulation/bcbs-liquidity-governance-principles` (open, matches).
Attached: `regulation/bcbs-liquidity-governance-principles`. Its "Stress testing and contingency funding" section states the plan must be "operational, not theoretical", "specifying that the plan should define clear escalation procedures, identify alternative funding sources, and be tested periodically."

### liquidity-coverage-ratio
Candidates: `regulation/bcbs-liquidity-coverage-ratio-original` (open, matches exactly), `regulation/bcbs-liquidity-risk-framework` (open, broader overview), `regulation/bcbs-liquidity-risk-principles-evolution` (open, near-duplicate broader overview).
Attached: `regulation/bcbs-liquidity-coverage-ratio-original`. It is the dedicated LCR article, stating the 100% threshold, the 30-day stress scenario, and the HQLA level structure verbatim. The two broader framework overviews cover the same ground at less depth and were left off; they are themselves near-duplicates of each other (the vault's own `open_questions` flags this).

### liquidity-risk
Candidates: `regulation/bcbs-liquidity-risk-framework` (open, thin match), `regulation/bcbs-liquidity-risk-principles-evolution` (open, near-duplicate of the above).
Attached: `regulation/bcbs-liquidity-risk-framework`. No vault article states the node's literal definition. This is the thinnest attachment in the batch: its opening sentence, "the 2007-2009 global financial crisis demonstrated that capital adequacy alone could not prevent bank failure if a firm lost access to funding", is the closest the vault comes to the solvency-versus-funding distinction the node states, and it is cited for that distinction rather than for a definition. The near-duplicate principles-evolution article says the same thing with more history and was left off. The definitional gap itself is ledgered.

### liquidity-risk-beyond-lcr
Candidates: `regulation/bcbs-liquidity-nsfr-monitoring-tools` (open, matches directly), `regulation/pra-liquidity-framework-modernisation-cp5-26` (open, matches a different source of LCR blind spot).
Attached both. The NSFR article states the structural gap directly: "addressed a structural dimension of liquidity risk that the Liquidity Coverage Ratio was not designed to reach... Where the LCR required a 30-day buffer against acute stress outflows, the NSFR required that a bank's structural funding profile... meet a minimum standard over a one-year horizon." CP5/26 names a second, more recent source of LCR blind spot: the composition/monetisation risk and central-bank-facility reliance gaps exposed by the 2023 turmoil. Different parts of the node, both attached.

### liquidity-risk-factor
Candidates: `regulation/bcbs-liquidity-coverage-ratio-original` (open, matches as one instance).
Attached: `regulation/bcbs-liquidity-coverage-ratio-original`. Its "Structure and calibration" section is a dedicated treatment of haircuts on assets (Level 2 assets at a 15% haircut) and run-off assumptions on funding lines (partial drawdown of committed credit and liquidity facilities), which is the mechanism the node describes. Partial-scope limit: the article instantiates the concept through one regulatory calibration rather than stating it as a general concept in its own right; the general statement is ledgered.

### liquidity-risk-management-overview
Candidates: `regulation/bcbs-liquidity-governance-principles` (open, matches).
Attached: `regulation/bcbs-liquidity-governance-principles`. Its whole-document scope, governance, measurement and management, stress testing, contingency funding, supervisory oversight and public disclosure, is the "key elements of managing a bank's liquidity risk" the node describes.

### liquidity-risk-oversight-framework
Candidates: `regulation/bcbs-liquidity-governance-principles` (open, matches).
Attached: `regulation/bcbs-liquidity-governance-principles`, specifically its "Governance and management framework" section: the board's responsibility for "establishing and approving the firm's liquidity risk tolerance" and senior management's "operational framework", which is the risk appetite, governance and control environment the node names.

### liquidity-stress-testing
Candidates: `regulation/pra-ilaap` (open, matches the current UK practice), `regulation/bcbs-liquidity-governance-principles` (open, matches the foundational governance angle).
Attached both. `pra-ilaap`'s "Liquidity stress testing" section covers scenario dimensions (name-specific, market-wide, combined), multiple time horizons, and the L-SREP report the testing feeds. `bcbs-liquidity-governance-principles`'s "Stress testing and contingency funding" section adds the governance angle the node also names: results must "feed directly into the design and sizing of the liquidity buffer" and the methodology is "subject to board review and senior management sign-off." Different angles on the same subject, both attached.

### lloyds-market
Candidates: `regulation/lloyds-market-oversight` (open, matches the oversight half), `regulation/lloyds-reserving-governance` (open, narrower reserving-only standard).
Attached: `regulation/lloyds-market-oversight`. It gives a dedicated, substantial treatment of Lloyd's regulatory oversight (Minimum Standards MS1, MS5, MS13, MS14, Capital Guidance, Validation Guidance). Partial-scope limit: the node also wants the market's structure as a marketplace of underwriting syndicates and its place in the wider London market, neither of which this article, or any other candidate, reaches; that remainder is ledgered. `lloyds-reserving-governance` was rejected as narrower still (reserving governance only, a sub-topic of oversight already covered).

### loan-repayment-schedule
Candidates: `methods/loan-repayment-plan` (open, matches exactly).
Attached: `methods/loan-repayment-plan`. States the definition verbatim: "A loan repayment plan is the period-by-period schedule decomposing each payment on an annuity loan into its principal and interest components," and covers the effective interest rate the node also names.

### localglmnet
Candidates: `methods/localglmnet` (open, matches exactly).
Attached: `methods/localglmnet`. A dedicated article on the exact node subject, architecture, attention-weight interpretation and all.

### logistic-regression
Candidates: `methods/scorecard-scaling` (open, matches the scorecard half).
Attached: `methods/scorecard-scaling`. States the second half of the node verbatim: "Together they define an affine mapping from log-odds to score points: Score = Factor x (...) + Offset," which is the "classical credit scorecard, whose displayed points are an affine rescaling of the same linear predictor" the node describes. Partial-scope limit: the node's first half, logistic regression as the binomial GLM under the logit link with coefficients read as log-odds ratios, is not stated by name in any vault article; ledgered as a wiki-coverage gap against the already-ingested GLM lecture source.

### longevity-hedging-with-derivatives
Candidates: `methods/longevity-risk-transfer` (open, matches directly).
Attached: `methods/longevity-risk-transfer`. Its "Bonds, swaps and the index-versus-indemnity divide" section is a dedicated treatment of longevity bonds and mortality swaps as instruments transferring "systematic longevity risk", matching the node exactly.

### loss-allowance-recognition
Candidates: `concepts/ifrs9-expected-credit-loss` (open, matches the amortised-cost/FVOCI half).
Attached: `concepts/ifrs9-expected-credit-loss`. States "the ECL model governs the entire stock of loans measured at amortised cost or fair value through other comprehensive income," matching the scope half of the node, plus the three-stage measurement mechanics. Partial-scope limit: the node also names lease receivables, contract assets, loan commitments and financial guarantee contracts as within scope, which this article does not state; ledgered as a wiki-coverage gap.

### loss-distribution
Candidates: `methods/aggregate-loss-models` (open, matches the aggregate half).
Attached: `methods/aggregate-loss-models`. Its collective risk model treats "the total of all claims in a portfolio" half of the node at length (frequency-severity separation, Panjer recursion). Partial-scope limit: the node's other half, choosing a distribution for an individual claim's size, is not treated; the article assumes a severity distribution is already chosen. Ledgered.

### loss-given-default
Candidates: `regulation/irb-lgd-estimation` (open, matches exactly).
Attached: `regulation/irb-lgd-estimation`. States the definition verbatim: "Loss given default (LGD) is the fraction of exposure expected to be lost upon the default of an obligor, after accounting for recoveries and the costs of resolution," plus the full downturn-LGD and estimation-requirements treatment.

### machine-learning-pricing
Candidates: `methods/non-life-ratemaking` (open, matches directly).
Attached: `methods/non-life-ratemaking`. States that neural networks, regression trees, bagging, random forests and boosting "extend the classical actuarial toolbox of GLMs" and that "the transparency that has always made GLMs attractive... is precisely what more flexible non-parametric methods trade away," matching the node's interaction/non-linearity point.

### machine-learning-risk-in-banking
Candidates: `regulation/eba-machine-learning-irb` (open, matches the opacity half), `concepts/ml-fairness` (rejected, unclassified confidentiality).
Attached: `regulation/eba-machine-learning-irb` only. It states the opacity risk at length: "the discussion paper's core argument is that ML's predictive gains come at the cost of opacity, and that opacity collides with specific CRR articles." `concepts/ml-fairness` was considered for the "unintended bias" half but rejected: its frontmatter carries no `confidentiality` field, which `attachment_complaint` treats as unclassified and `attach_articles.py` refuses outright; its body also states the source licence is CC BY-NC-ND, "permits internal reading but not derivative course text", a second reason to keep it out of a teaching corpus. The bias half is uncovered and ledgered.

### mack-model
Candidates: `methods/chain-ladder-reserving` (open, matches the derivation), `methods/stochastic-claims-reserving` (open, matches the two-moments restatement and validation).
Attached both. `chain-ladder-reserving` gives the derivation: "Mack proved that this construction is only optimal... From these conditions Mack derived a distribution-free formula for the mean squared error of the reserve, decomposing it into process variance and parameter estimation error." `stochastic-claims-reserving` restates the model in the node's own terms, "Mack's model specifies only the first two moments of incremental claims, mean and variance both proportional to the prior cumulative, without assuming a full distribution, and reproduces the chain-ladder point estimate exactly," and adds Meyers's (2019) empirical validation findings. Different parts of the node (derivation versus restatement-and-validation), both attached; neither is a dedicated Mack-model article, so no overview to leave off.

## Uncovered (18)

Grouped by why, with the strongest rejected candidate named where one existed.

**No vault content at all** (confirmed by both index grep and full-text grep across `vault/wiki`): loan-to-deposit-ratio.

**Passing mentions only, rejected:**
- linear-transformation: no candidate found at all beyond `up-wtw211-course-notes`'s own eigenvector chapter, which is a different WTW211 topic, not a mention within an article.
- liquidity-risk-limit-framework: `regulation/bcbs-liquidity-nsfr-monitoring-tools`'s "Supervisory monitoring tools" section names concentration of funding and available unencumbered assets, categories that overlap the node's list, but the article frames these as a supervisor's monitoring toolkit, not a bank's own internal limit-setting framework. Considered but rejected on framing grounds.
- loan-behavioural-tenor: `regulation/irrbb-shock-calibration` treats "behavioural maturity assumptions" at length, but for non-maturity deposit rate sensitivity (the liability side, IRRBB repricing), not loan prepayment tenor (the asset side, liquidity cash-flow purposes). Same general concept, opposite side of the balance sheet and a different risk.
- loan-facility-structuring: `concepts/bbb-small-business-finance-markets` names "flexible revolving credit" and "term loans" in one clause of SME lending-volume statistics, with no treatment of choosing facility type or terms.
- loan-underwriting-criteria: `methods/model-shift-quantification` and `methods/forrest-2024-model-shift-mrm` both use "credit policy" only as a covariate whose shift needs monitoring for model stability, not as a treatment of underwriting rules.
- local-regression: `concepts/balance-property-and-auto-calibration` gives two genuine sentences on local regression as one calibration-diagnostic smoothing option ("Local regression with quadratic splines gives a continuous version, at the cost of two hyper-parameters, the nearest-neighbour fraction and the spline degree"), but subordinate to an argument about the balance property, not a treatment of the method in general.
- lognormal-distribution: `methods/reinsurance-pricing` treats the lognormal only as one of two competing aggregate-loss models for reinsurance treaty pricing (versus the Heckman-Meyers collective risk model), never defining the distribution itself.
- lognormal-security-price-model: `methods/vasicek-loan-portfolio-value` uses "correlated geometric Brownian motions" for asset values in a Merton-style credit portfolio loss model, a different application (credit risk, not security-price modelling with empirical for/against evidence).
- loss-distribution-approach-validation: `regulation/operational-risk-capital-approaches`'s History section names the AMA's four inputs (internal loss data, external data, scenario analysis, business-environment and internal-control factors) and the 2011 guidelines' coverage of "distributional assumptions", but only as one-sentence historical summary; it does not treat independent validation or the thin-tail-data problem the node names.
- loss-distribution-parameter-estimation: `methods/lgd-survival-analysis` treats right-censored, incomplete recovery data at length, the same general "incomplete data" theme, but via Cox proportional hazards and Kaplan-Meier survival curves, not the maximum-likelihood-versus-method-of-moments comparison on a chosen loss or failure-time distribution the node describes.
- low-frequency-high-severity-events: `regulation/operational-risk-capital-approaches` covers the exact risk type (operational risk) but is entirely about the standardised capital formula; it never treats the frequency-severity modelling problem or the scarce-data limitation the node names.
- low-interest-rate-strategic-impact: `regulation/eiopa-supervisory-monitoring` and `regulation/iais-holistic-framework` both mention a "low interest rate environment" or "low-rate environment" in one clause each, but as an insurance-sector Solvency II recovery-period or systemic-monitoring trigger, not a bank's strategic margin-compression response.
- macroeconomic-measurement: `methods/credit-risk-procyclicality` names "the credit-to-GDP gap" as the CCyB's calibration reference in one clause; GDP appears elsewhere only as a model covariate (`methods/supervised-macroeconomic-index`, `methods/forward-looking-information-modelling`), never as a subject of its own compilation or interpretation.
- macroeconomic-policy-instruments: `regulation/irrbb-shock-calibration`'s source footnote cites a BCBS working paper section on "interest rate environment, monetary policy, deposit betas, and rate-cycle asymmetry", but the wiki article's own prose never expounds policy instrument types or channels.

**Considered but deliberately not attached despite surface similarity:**
- loss-allowance-presentation-in-other-comprehensive-income: confirmed by grep that no article states the specific rule (loss allowance recognised in OCI rather than as a reduction to carrying amount for an FVOCI asset). `concepts/ifrs9-expected-credit-loss`, otherwise the closest IFRS 9 article and already attached to a sibling node, names FVOCI only as a measurement category within ECL scope, never this presentation mechanic. Logged in the ledger as a wiki-coverage gap rather than an acquisition gap, since IFRS 9 is already ingested.
- low-credit-risk-simplification: confirmed by grep that no article states the low-credit-risk exemption. `methods/ifrs9-sicr-triggers-and-staging`, the closest SICR article, covers quantitative and qualitative triggers at length but never the investment-grade exemption from needing them. Same wiki-coverage-gap treatment as above.

## Ledger (`ledger-23.yaml`)

16 entries: 4 new documents plus 12 that extend already-seeded or wave-1 ids (`assa-f107-study-material-2026`, `assa-f207-study-material-2026`, `ifoa-cb2-core-reading-2026`, `ifoa-cm2-core-reading-2026`, `ifoa-cs1-core-reading-2026`, `ifoa-cs2-core-reading-2026`, `ifoa-sp1-core-reading-2026`, `ifoa-sp7-core-reading-2026`, `ifoa-sp9-core-reading-2026`, `up-ekn120-course-notes`, `up-wtw211-course-notes`, `up-wst212-course-notes`) with this batch's node ids added to `needed_by` only, all other fields copied verbatim. `merge_ledger.py --dry-run` reports "would write 94 entries (4 seeded)" with no complaint against any of this batch's entries; the note lines it does print concern disagreements between other batches' fragments already in the shared staging directory.

Ledgered nodes split into two groups: sixteen fully uncovered nodes (grouped above), and eight more (`liquidity-adequacy-regulatory-requirements`, `liquidity-risk`, `liquidity-risk-factor`, `lloyds-market`, `logistic-regression`, `loss-allowance-recognition`, `loss-distribution`, `machine-learning-risk-in-banking`) that are the stated remainder of a partial attachment; both kinds are named in the relevant `note` field against the id they extend. Three new ids are wiki-coverage rather than acquisition gaps against a source already ingested: `dl-actuarial-2026-l02-glm-logistic-regression` (the GLM lecture already drives `methods/exponential-dispersion-family-and-glm` but never specialises to logistic regression by name), and `iasb-ifrs9-oci-loss-allowance-presentation`, `iasb-ifrs9-loss-allowance-scope` and `iasb-ifrs9-low-credit-risk-simplification` (IFRS 9 is already ingested but three specific paragraphs, 5.5.2, 5.2.2/5.5.1, and 5.5.10, are not yet drawn out in any wiki article). One departure from the anchor-body default: `up-ekn120-course-notes` is proposed alongside `ifoa-cb2-core-reading-2026` for `macroeconomic-measurement`, since the node carries both anchor bodies and EKN120 (an introductory macroeconomics course) is the more likely home for GDP-measurement basics specifically, though this was not directly inspected and is stated as an assumption in the note.
