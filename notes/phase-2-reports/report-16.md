# Phase 2 batch 16 attachment report

40 nodes worked. 7 attached, 33 uncovered. 7 total attachments.

## Attached

### foundation-model
Candidates: `concepts/foundation-models-credit-risk` (open, matches directly), `ai-agents/nlp-and-language-models` (open, names "foundation model" once in a cross-reference clause, rejected), `concepts/in-context-learning-tabular-actuarial-models` (open, covers the same anchor lecture's tabular-ICL half, not the general concept, rejected).
Attached: `concepts/foundation-models-credit-risk`. Opens with a dedicated definition: "A foundation model in credit risk is a large, pre-trained neural network that consumes raw banking event sequences and produces representations that downstream tasks... fine-tune on with modest additional data." Gives both the definition and a worked use (PRAGMA, scorecard-versus-foundation-model contrast). The `nlp-and-language-models` hit is a single clause pointing elsewhere and was rejected as a passing mention; `in-context-learning-tabular-actuarial-models` shares the node's anchor lecture (ucsc.dl-actuarial-2026.l12) but its "Tabular foundation models" section is scoped to TabPFN/TabICL specifically rather than the general concept, so it was left off as the narrower companion piece.

### fraud-analytics
Candidates: `methods/statistical-fraud-detection` (open, matches), `concepts/uk-insurance-claims-fraud` (open, rejected, wrong domain).
Attached: `methods/statistical-fraud-detection`. Built from Bolton and Hand's 2002 review, it gives the general statistical framework for fraud analytics: suspicion scores rather than verdicts, the class-imbalance/cost compromise, and label uncertainty, matching the node's data-eng/ml scope. `uk-insurance-claims-fraud` was considered but rejected: it is UK motor "crash for cash" and ghost-broking typology reporting, general-insurance-specific and outside this node's ASSA F207 banking-analytics anchor.

### frequency-severity-approach
Candidates: `methods/aggregate-loss-models` (open, matches exactly).
Attached: `methods/aggregate-loss-models`. States the node's subject in its opening line: "The collective risk model represents a portfolio's total claims as a random sum of a random number of individually and identically distributed claim amounts, separating the frequency of claims from their severity." Also supplies the Panjer recursion, the node's `collective-risk-model` requirement.

### fundamental-review-trading-book
Candidates: `regulation/frtb-minimum-capital-market-risk` (open, matches, current binding standard), `regulation/bcbs-frtb-2012-consultative-document` (open, rejected, superseded 2012 first consultative document), `regulation/basel-3-1-market-risk` (open, rejected, narrower UK implementation of the same standard).
Attached: `regulation/frtb-minimum-capital-market-risk`. Covers the standardised approach, the internal models approach, expected shortfall, the default risk charge, the trading/banking book boundary and non-modellable risk factors, closing both `requires` (`internal-models-approach-market-risk`, `standardised-approach-market-risk`). It is BCBS d457, the current binding standard, and its own status line names both rejected candidates as superseded precursor and UK-specific implementation respectively, so both were left off as covering the same ground from a narrower angle.

### funding-risk
Candidates: `regulation/pra-ilaap` (open, matches half the node).
Attached: `regulation/pra-ilaap`. Defines the ILAAP as "a firm-led self-assessment of all material liquidity and funding risks" and names the specific funding-risk content it must cover: "all funding dependencies, the resilience of funding under stress." Partial-scope note: the article's primary subject is the ILAAP process itself (the node's own `requires`), with funding risk covered as one of the two things that process assesses, rather than as a dedicated funding-risk article in its own right.

### gaussian-copula
Candidates: `methods/default-correlation-copula-models` (open, matches exactly), `methods/creditmetrics-portfolio-model` (open, rejected, broader migration-model overview, same ground).
Attached: `methods/default-correlation-copula-models`. States the equivalence directly: "correlating asset values through a normal distribution is the same operation as applying a normal copula." Also addresses the node's `tail-dependence` requirement: "the normal copula's tail behaviour is a choice rather than a consequence." `creditmetrics-portfolio-model` was rejected as the broader asset-correlation portfolio model this article's equivalence result already connects to; attaching it too would duplicate ground already covered.

### glm
Candidates: `methods/exponential-dispersion-family-and-glm` (open, matches exactly), `methods/non-life-ratemaking` (open, rejected, uses GLM as a ratemaking tool rather than defining it).
Attached: `methods/exponential-dispersion-family-and-glm`. Built from the exact anchor lecture (ucsc.dl-actuarial-2026.l02) and gives the full definitional chain: the exponential dispersion family density, the canonical link, the deviance loss, and fitting by IRLS. `non-life-ratemaking` treats GLM as one ratemaking tool among several rather than defining it, so it was left off as the weaker, non-dedicated candidate.

## Uncovered (33)

Grouped by why, with the strongest rejected candidate named where one existed.

**No vault content at all** (confirmed by both index grep and full-text grep across `vault/wiki`): forward-contract-pricing, forward-contract-valuation, forward-foreign-exchange-hedging, forward-futures-payoff, forward-measure-valuation, forward-rate-agreements, forward-rate-versus-futures-rate, functions-limits-and-continuity, fundamental-theorem-of-calculus, funds-transfer-pricing-curve, future-lifetime-random-variable, future-loss-random-variable, futures-and-options, futures-hedging, gains-from-trade-and-specialisation, game-theory-and-oligopoly-strategy, general-insurance-accounting, general-insurance-business-environment, general-insurance-market, general-insurance-product, general-insurance-risk-and-uncertainty, gev, fourier-analysis-and-series, frequency-severity-modelling-banking (the one hit, `regulation/operational-risk-capital-approaches`, is the SMA capital formula, not frequency/severity loss modelling, and was not even a passing mention worth naming).

**Passing mentions only, rejected:**
- funds-transfer-pricing: `regulation/bcbs-bank-capital-balance-sheet-distress` names it in one clause ("Banks govern their strategy through changes to funds transfer pricing and internal hurdle rates") inside an argument about CET1 target-ratio adjustment; no treatment of the FTP mechanism itself.
- fused-lasso: `methods/icenet-smoothness-and-monotonicity-constraints` names it once in a list ("Elastic net, fused LASSO, group LASSO, and SCAD extend the family") with no definition, despite sharing the node's exact anchor lecture (ucsc.dl-actuarial-2026.l08). Logged in the ledger as a wiki-coverage gap rather than an acquisition gap, since the source is already ingested, matching wave 1's `activation-function` precedent.
- gamma-distribution: `methods/creditrisk-plus-portfolio-model` treats each sector's default rate "as gamma-distributed rather than fixed" as a modelling assumption, with no density, moments or general definition given.
- geometric-distribution: `methods/aggregate-loss-models` names it as one member of the Panjer class ("Poisson, binomial, negative binomial and geometric distributions are exactly the members of this family") with no separate treatment.
- geometric-brownian-motion: `methods/vasicek-loan-portfolio-value` states "Asset values follow correlated geometric Brownian motions" as one clause inside the Merton-style derivation of the Vasicek ASRF formula; no SDE, no solution, no Ito's lemma.
- gdp-outlook-and-credit-losses: `methods/ifrs9-scenario-design-and-weighting` names GDP growth as the dominant IFRS 9 scenario variable in one clause ("GDP growth and unemployment rate dominate the variable selection across EU institutions"); `regulation/eba-downturn-lgd-estimation` and `methods/forward-looking-information-modelling` were also checked and are similarly one-clause mentions inside downturn-identification and stationarity-testing discussions respectively, neither treating the GDP-outlook-to-credit-loss relationship as its own subject.

**Considered and deliberately not attached despite surface similarity:**
- fraud-risk: `methods/statistical-fraud-detection` (the article attached to `fraud-analytics` in this same batch) is the canonical statistical treatment of fraud detection, but this node's domain is life/health insurance risk (SP1/SP2 anchors: non-disclosure and claims fraud in protection business), which the article never addresses. `concepts/uk-insurance-claims-fraud` covers UK motor claims fraud typologies, a different insurance line again. Neither treats fraud as a life-insurance risk category.
- general-insurance-data-quality: `concepts/data-quality-dimensions` gives a full generic treatment (the DAMA taxonomy: accuracy, completeness, consistency, timeliness, uniqueness, validity) but carries no general-insurance content whatsoever; it is a data-engineering article about dbt tests and DAMA definitions, not an actuarial GI data-quality treatment.
- general-insurance-regulatory-framework: `regulation/general-insurance-pricing-practices` (the price-walking ban, PS21/5) and `regulation/general-insurance-value-measures` (PS20/9 reporting) are both dedicated, real FCA GI regulatory articles, but each is one specific conduct rule rather than the regulatory framework as a whole (which SP7 examines as PRA/FCA dual regulation, Solvency II and conduct regulation together). Attaching either would misrepresent a narrow rule as framework coverage.

## Ledger (`ledger-16.yaml`)

16 entries, all reusing ids already proposed in wave 1: none of batch 16's anchor bodies (ASSA F107/F207, IFoA CM2/SP5/SP6/SP1/CS1/CS2/CM1/CB2/SP7/SP8, University of Pretoria WTW114/WTW124/WTW386, and the UCSC dl-actuarial l08 lecture) needed a new document, since wave 1's 59 seeded ids already cover every anchor body the corpus's closed vocabulary permits. Each entry copies `document`, `expected_tier`, `acquisition`, `status` and `claim` verbatim from `ledger-ids.yaml` and adds only this batch's `needed_by` node ids and a `note` identifying which section of the document is needed, since every seeded claim describes a different chapter than the one this batch's nodes require. `merge_ledger.py --dry-run` reports "would write 73 entries (4 seeded)" with no complaint attributable to this fragment; a first run reported a transient parse failure on another batch's concurrently-written `ledger-18.yaml`, which resolved on retry once that batch's write completed.

The one anchor-default departure worth naming explicitly: `fundamental-theorem-of-calculus` is anchored to `up.wtw124.9`, but the already-seeded `up-wtw114-course-notes` claim also names "the fundamental theorem of calculus" from an earlier course. Both entries are kept (one per node's own anchor, per the default rule), with a note on the WTW124 entry flagging the apparent overlap as a presumed second, separate treatment rather than resolving it, since direct inspection of an unacquired document is not possible.
