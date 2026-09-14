# Phase 2 batch 26 attachment report

40 nodes worked. 4 attached, 36 uncovered. 4 total attachments.

## Attached

### nagging
Candidates: `methods/entity-embedding-and-network-ensembling` (open, matches exactly).
Attached: `methods/entity-embedding-and-network-ensembling`. Its "Ensembling answers it by averaging conditionally independent fits" section states the node's definition verbatim, naming nagging as "network aggregating, after Richman and Wuthrich" and giving the same no-bootstrap-needed reasoning the node body states. Sourced from the same UCSC lecture (l06) the node itself anchors to.

### noise-covariate-benchmark
Candidates: `methods/localglmnet` (open, matches exactly).
Attached: `methods/localglmnet`. Its "Calibrating significance on a noise covariate" section states the mechanism precisely: "adding a standard normal covariate independent of everything else, then reads the fluctuation in its fitted attention weights as the amount attributable to pure noise." Sourced from the same UCSC lecture (l09) the node itself anchors to.

### net-interest-income
Candidates: `concepts/eve-and-nii` (open, matches), `concepts/economic-value-of-rating-systems` was not a separate candidate, just a passing mention of "net interest margin" (a different node's territory, see Uncovered).
Attached: `concepts/eve-and-nii`. Its "What each measure represents" section defines NII directly ("NII captures the change in expected earnings over a short horizon... It projects interest income and expense over a short forward horizon") and gives its regulatory use (the EBA supervisory outlier test). Partial-scope note: the article frames NII inside the EVE/NII IRRBB duality rather than as a standalone banking-book profitability metric, and does not address the node's anchor body (ASSA F107) directly, but the core definition and mechanics are genuinely there.

### net-stable-funding-ratio
Candidates: `regulation/bcbs-liquidity-nsfr-monitoring-tools` (open, matches exactly, dedicated), several other regulation articles that cite NSFR in passing (`regulation/uk-liquidity-framework`, `regulation/pra-liquidity-framework-modernisation-cp5-26`, `regulation/bcbs-basel3-implementation-monitoring`, others).
Attached: `regulation/bcbs-liquidity-nsfr-monitoring-tools` only. Its dedicated "## Net Stable Funding Ratio" section states the ratio precisely: "the ratio of available stable funding to required stable funding, with the requirement that this ratio equals or exceeds 100%." The other hits link to this article rather than duplicating the definition, so per the brief's rule on overlapping coverage, the dedicated article is attached and the citing ones left off.

## Uncovered (36)

Grouped by why, with the strongest rejected candidate named where one existed.

**No vault content at all** (confirmed by both index grep and full-text grep across `vault/wiki`): moving-average-process, multi-asset-and-quanto-option, multi-product-and-lifecycle-pricing, multi-state-model, multifactor-interest-rate-model, multifactor-model, multiple-integrals-and-coordinate-systems, multiple-state-markov-model, multiple-transition-cashflow-valuation, multivariable-calculus-and-directional-derivatives, multivariate-autoregressive-model, multivariate-time-series, murphy-decomposition, mutual-bank, nelson-aalen-estimator, net-interest-margin-and-spread, net-interest-margin-limitations, net-investment-hedge, net-premium-valuation, new-business-risk, non-economic-influences-on-investment-supply-and-demand.

**Passing mentions only, rejected:**
- mortality-risk: `methods/longevity-risk-transfer` cites "mortality risk" only inside a footnote title (Cox and Lin, "Natural Hedging of Life and Annuity Mortality Risks"); `concepts/climate-linked-mortality` uses "relative mortality risk by temperature" as a one-off phrase inside a climate-hazard statistic. Neither treats mortality risk as the risk that experienced deaths or survivals differ from assumption.
- multilateral-development-bank-exposure-risk-weights: `regulation/crr-credit-risk-provisions` names "multilateral development banks" once, as one item in a fifteen-item exposure-class list; no eligibility criteria or risk-weight table.
- multiple-decrement: `methods/ifrs9-lifetime-pd-term-structure` and `concepts/ifrs9-expected-credit-loss` both name "competing risks" in one clause each, describing how IFRS 9 lifetime-PD data construction handles them (by exclusion from the risk set, not by explicit competing-risk modelling), rather than treating multiple decrement generally.
- multiple-external-ratings-treatment: `regulation/eu-crr-2013-credit-risk`, `regulation/pra-crr-rulebook-restatement-2025` and `regulation/bcbs-securitisation-framework` all cite ECAI ratings, but for rating-to-risk-weight mapping tables, not the rule for an exposure carrying more than one disagreeing rating.
- national-banking-regulation: `regulation/bcbs-basel3-implementation-monitoring` discusses "national implementation" as cross-jurisdiction Basel III monitoring data, a different frame from a national regulator's own rules layered on top of supra-national standards.
- negative-binomial-distribution: `methods/aggregate-loss-models` names it once as a member of the Panjer class alongside Poisson, binomial and geometric; no distributional treatment of its own.
- net-asset-value: `regulation/basel-3-1-market-risk` uses NAV only as the 90% de minimis threshold for the CIU trading-book boundary, a specific regulatory usage rather than NAV as a fund performance measure.
- net-interest-income-over-cycle: `regulation/eba-eu-wide-stress-test-methodology`'s "Market risk and net interest income" section and `regulation/boe-stress-testing-approach`'s sensitivity-analysis paragraph both discuss NII projection as stress-test methodology (a 3-year adverse-scenario projection), not the general cyclicality of rates, loan demand and funding costs the node describes.
- net-interest-margin: `concepts/economic-value-of-rating-systems` names it in one clause ("the institution gains on both net interest margin and return on capital simultaneously"), inside an unrelated argument about rating-system investment appraisal.
- net-present-value: `concepts/effective-interest-rate` mentions NPV only as the mechanism for solving the EIR equation by root-finding ("the discount rate at which the net present value of the cash flow stream equals zero"), not as an investment appraisal method in its own right.

**Considered and deliberately not attached despite surface similarity:**
- multi-head-attention: `concepts/in-context-learning-tabular-actuarial-models` and `methods/credibility-transformer`, both built from the same lecture pair (l10-11) the node anchors to, discuss attention mechanisms and a single attention layer in depth, but neither names or describes a multi-head structure (several heads run in parallel with independent query/key/value parameters, then concatenated and reprojected). Judged too close a false match to attach; ledgered as a likely wiki-article scope gap on an already-ingested source rather than an acquisition gap.
- multivariate-distribution, multivariate-normal-distribution, multivariate-sample-estimation: `methods/probabilistic-machine-learning` lists "chapters 2 and 3: Probability, univariate and multivariate models" as coverage of Murphy's textbook, but this is a coverage description of an external source, not exposition in the vault's own article text. No content a node body could be written from.
- murphy-decomposition: "Murphy" appears across four vault articles (`methods/probabilistic-machine-learning`, `methods/mathematics-for-machine-learning`, `methods/statistical-learning-with-python`, `methods/probabilistic-ml-advanced-topics`), every instance an author citation to Kevin Murphy's *Probabilistic Machine Learning* textbooks, unrelated to Murphy's forecast-verification score decomposition. `methods/scorecard-scaling`'s "score decomposition" is a credit-scorecard point-allocation concept, also unrelated.
- new-business-and-asset-sales: `concepts/market-consistent-embedded-value` discusses the "market-consistent value of new business" (MCVNB, an embedded-value pricing concept) and `concepts/pcp-structure-and-residual-value-risk` cites FLA new-business volume statistics; neither treats mitigating risk by changing future new business or selling assets, which is the node's subject.

## Ledger (`ledger-26.yaml`)

21 entries: 16 reuse an existing id from `ledger-ids.yaml` (extending `needed_by` with this batch's nodes and adding a `note` on the further chapter each needs, since none of the reused claims already covered batch 26's ground) and 5 are new documents. `merge_ledger.py --dry-run` reports "would write 73 entries (4 seeded)" with no complaints; the three disagreement notes it printed (`up-wtw114-course-notes`, `up-wst111-course-notes`, `up-wtw354-course-notes`) are pre-existing conflicts between other batches' fragments, none of which batch 26 touches.

New documents, by anchor body: two BCBS d424 paragraphs not covered by wave 1's existing d424 entries (MDB risk weights, para 13; multiple-ECAI-ratings treatment, para 103), two University of Pretoria course codes not previously ledgered (WTW218 for multivariable calculus and multiple integrals; WST321 for multivariate time series), and one UCSC deep-learning-summer-school entry (Lecture 7, for Murphy's decomposition).

Two judgement calls the brief didn't cover directly. First, multiple-decrement carries four anchor bodies; I picked `ifoa-cm1-core-reading-2026` as the sole document (CM1 is the standard UK actuarial-mathematics text for multiple decrement) and did not ledger the other three, noting why in that entry: the `ucsc.dl-actuarial-2026.l01` anchor is the same general-overview lecture wave 1's own ledger already found unreliable as a specific-topic anchor (its age-period-cohort entry), and `up.ias353.4` duplicates ground CM1 already covers. Second, two nodes (`multi-head-attention`, `murphy-decomposition`) anchor to UCSC lectures whose slide decks are already ingested as sources for existing vault articles that stop short of the specific content needed; both are ledgered with `status: ingested` and a note flagging a wiki-article scope gap rather than an acquisition gap, following the precedent wave 1 set for `activation-function`.
