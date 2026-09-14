# Phase 2 batch 25 attachment report

40 nodes worked. 10 attached, 30 uncovered. 13 total attachments.

## Attached

### ml-in-banking-risk-management
Candidates: `methods/ml-credit-risk-methods` (open, matches the credit-decisions half), `methods/ml-credit-scoring-empirical-and-review` (open, near-duplicate of the above), `concepts/llm-in-credit-risk-landscape` (open, LLM-specific rather than ML generally, rejected as off-target).
Attached: `methods/ml-credit-risk-methods`. Opens on "Machine learning has shifted from a research curiosity to a practitioner staple in credit risk over the fifteen years from 2010 to 2025" and gives a dedicated, sourced treatment of ML displacing logistic regression for credit decisions. Partial-scope limit: the node also names fraud detection and other risk-management tasks, and no vault article treats ML for fraud detection in banking; ledgered under `assa-f107-study-material-2026`.

### model-adaptation
Candidates: `ai-agents/llm-fine-tuning-generation-models` (open, matches the PEFT and full-fine-tuning rungs), `concepts/in-context-learning-tabular-actuarial-models` (open, matches the in-context-learning and retrieval rungs), `methods/pragma-foundation-model` (rejected, a single case study rather than a treatment of the ladder itself).
Attached both. `ai-agents/llm-fine-tuning-generation-models` states "Full fine-tuning updates all model parameters" and describes Parameter-efficient fine-tuning (PEFT) and LoRA in a named section. `concepts/in-context-learning-tabular-actuarial-models` states a pretrained model "adjusts its prediction from that context without any retraining" and separately describes a 64-nearest-neighbour retrieval mechanism, covering the ladder's cheap end. Between the two articles the full four-rung ladder the node describes is covered; the "bureau score as bottom-rung precedent" is the node's own analytical framing rather than a sourced claim, so no remainder was ledgered for it.

### model-inventory
Candidates: `regulation/pra-ss1-23-model-risk-management` (open, matches directly), `regulation/model-risk-management-framework` (open, same ground at one remove).
Attached: `regulation/pra-ss1-23-model-risk-management`. Its "first principle requires firms to maintain a comprehensive, firm-wide model inventory and to implement a risk-based tiering approach that assigns materiality and complexity ratings to each model" is a named section (Principle 1) matching the node directly. `regulation/model-risk-management-framework` paraphrases the same fact one level up and was left off as the broader overview.

### model-lifecycle
Candidates: `regulation/pra-ss1-23-model-risk-management` (open, matches most of the node), `regulation/model-risk-management-framework` (open, broader overview of the same fact), `regulation/fed-model-risk-management-sr11-7-revised` (open, US jurisdiction, subsumed).
Attached: `regulation/pra-ss1-23-model-risk-management`, which "establishes five high-level principles covering the full model lifecycle" spanning development, validation, deployment and ongoing monitoring. Partial-scope limit: no vault article names an explicit retirement or decommissioning stage; ledgered under `assa-f207-study-material-2026`.

### model-risk
Candidates: `regulation/pra-ss1-23-model-risk-management` (open, matches verbatim), `regulation/model-risk-management-framework` (open, same definition one level up), `regulation/fed-model-risk-management-sr11-7-revised` (rejected, US-only restatement).
Attached: `regulation/pra-ss1-23-model-risk-management`. States: "Model risk itself is defined as the potential for adverse consequences from model errors or the inappropriate use of modelled outputs to inform decisions, with consequences ranging from deterioration in prudential position to reputational damage and financial loss," which matches the node's definition closely enough to need no partial-scope note.

### model-risk-appetite
Candidates: `regulation/pra-ss1-23-model-risk-management` (open, names "model risk appetite" directly), `concepts/risk-appetite-framework` (open, broader risk-appetite overview not specific to models).
Attached: `regulation/pra-ss1-23-model-risk-management`. States: "The board is expected to set a model risk appetite, approve the MRM policy, and receive regular reports on the firm's model risk profile against that appetite," and separately covers materiality tiering (Principle 1) and validation escalation (Principle 4), together matching the node's "limits on model use, materiality thresholds and escalation triggers". `concepts/risk-appetite-framework` was left off as the broader, model-non-specific overview.

### model-risk-management
Candidates: `regulation/pra-ss1-23-model-risk-management` (open, matches in depth for one jurisdiction), `regulation/model-risk-management-framework` (open, matches at discipline level across jurisdictions), `regulation/fed-model-risk-management-sr11-7-revised` (rejected, US-only restatement of the same ground).
Attached both. This is a "different parts, attach both" case rather than a duplicate: `regulation/model-risk-management-framework` opens with the jurisdiction-neutral definition the generic node needs ("Model risk management (MRM) is the discipline of identifying, measuring, and controlling the risk of adverse consequences from quantitative models"), while `regulation/pra-ss1-23-model-risk-management` supplies the worked depth on validation, limitations and appropriate use the node also asks for (independent validation reporting lines, post-model-adjustment governance). `regulation/fed-model-risk-management-sr11-7-revised` was left off as it restates the same ground for a second jurisdiction rather than adding a new part.

### mortality-forecast-error-sources
Candidates: `methods/mortality-modelling` (open, matches most of the node).
Attached: `methods/mortality-modelling`. Its "Comparing models and testing them out of sample" section states that "Cairns and co-authors' 2007 working paper compares eight stochastic models against England & Wales and US data and finds no single model dominates" (model risk) and that a later backtest found "parameter-uncertainty-adjusted intervals are appropriately wider than those without it" (parameter risk). Partial-scope limit: the article does not treat the risk that a past trend simply does not continue as its own distinct error source; ledgered under `ifoa-cs2-core-reading-2026`.

### mortality-graduation
Candidates: `methods/mortality-modelling` (open, matches the smoothing half).
Attached: `methods/mortality-modelling`. States that "Currie's 2007 presentation applies penalised B-splines as a two-dimensional regression basis" and that this "smooths the mortality surface directly", covering graduation as smoothing. Partial-scope limit: the article does not treat statistical testing of the graduated table's fit; ledgered under `up-ias382-course-notes`.

### mortality-projection-approaches
Candidates: `methods/mortality-modelling` (open, matches directly and by name).
Attached: `methods/mortality-modelling`. States: "Booth and Tickle's 2008 review of the subsequent century and a half classifies forecasting methods into expectation, extrapolation and explanation approaches, and concludes that extrapolative two-factor methods... have been the most successful," which names all three approaches the node describes (expert opinion, extrapolation, causal explanation) against a citation. No partial-scope limit.

## Uncovered (30)

Grouped by why, with the strongest rejected candidate named where one existed.

**No vault content at all** (confirmed by both index and full-text grep across `vault/wiki`): monetary-transmission-to-business-activity, monetary-union, money-and-banking, money-multiplier, money-supply-and-monetary-policy, money-supply-effect-on-output-and-prices, monopolistic-competition, modelling-with-difference-equations, mortality-investigation-classification, mortality-option-cost-assessment, mortality-profit.

**Passing mentions only, rejected:**
- money-market-reference-rates: `methods/lgd-discount-rate` cites SONIA once, as the PRA's mandated LGD discount-rate benchmark (SONIA plus 5%), not as one of a taxonomy of reference rates.
- money-markets: `regulation/bcbs-securitisation-framework` and `regulation/bcbs-liquidity-nsfr-monitoring-tools` mention commercial paper and money-market funds in one clause each, inside securitisation and liquidity-monitoring arguments.
- mortality-and-morbidity-variation-factors: `concepts/climate-linked-mortality` states regional cold-tolerance variability in one sentence; no treatment of the social and economic drivers the node asks for.
- mortality-convergence: `methods/mortality-modelling` uses "convergence periods" once, but as a projection-model assumption parameter (how fast the CMI and SOA mortality models converge to each other), a different sense of the word from the node's initially-distinct-groups convergence.
- moment: `methods/exponential-dispersion-family-and-glm` gives the mean and variance of a GLM response as functions of the cumulant function, in one sentence, without stating the general definition of a moment.
- moment-extraction-from-generating-function: `methods/creditrisk-plus-portfolio-model` and `methods/aggregate-loss-models` both use a probability-generating function to recover a portfolio loss distribution, a related but different device from moment extraction, and neither names the differentiate-at-the-origin technique.
- moment-generating-function: same cumulant-function sentence as `moment` above; the MGF itself is never named. The lecture this node's primary anchor points to is already in the vault as a cited source (`dl-actuarial-2026-l02-glm`) but no wiki article treats the MGF as its own topic.
- monetary-policy: `regulation/irrbb-shock-calibration` and `regulation/eba-eu-wide-stress-test-methodology` reference central bank policy rates in passing, as an input to interest-rate-risk or stress-test calibration, not as a treatment of monetary policy itself.
- monopoly: `concepts/lending-discrimination-evidence` uses "monopoly rents" once, in an argument about algorithmic price discrimination, not about monopoly theory.
- moral-hazard-and-adverse-selection: adverse selection is covered extensively (`methods/heterogeneity-shortfall-impact` and others), but only as an IRB credit-pricing effect where mispriced risk grades cause selection into or out of an offer; moral hazard does not appear anywhere in the vault. Neither half of this two-part node is a genuine match for what the vault covers.

**Considered and deliberately not attached despite surface similarity:**
- model-choice-from-data: `methods/nguyen-2025-enhancing-credit-risk-ml` offers "a practical selection framework for practitioners weighing predictive performance against governance and interpretability requirements", close in wording to the node's "quantitative results... qualitative judgement" framing, but it is a single ML-benchmark case study rather than a treatment of the general actuarial principle.
- model-control-cycle: the strongest candidate, `regulation/pra-ss1-23-model-risk-management` (already attached to five other nodes in this batch), frames periodic revalidation and ongoing monitoring as one governance principle among five rather than as the specify-monitor-revise cycle the node describes.
- model-fitting: `methods/vasicek-asset-correlation-estimation` gives a full worked estimation (IMM versus MLE, with Monte Carlo bias quantification) but for one specific parameter of one specific model, not a treatment of model fitting as a general concept.
- model-informed-decision-making: `concepts/risk-appetite-framework` and the vault's stress-testing articles each cover one input to the decision the node describes, but no article combines stochastic modelling, scenario analysis, stress testing and model/parameter risk into a single decision framework weighed against risk appetite.
- model-performance-metrics: `methods/credit-model-metrics-binder-2026` and the vault's other discrimination and calibration articles are exactly the classification-specific metrics (AUC, Gini, Somers' D, Brier score) the node's own wording excludes ("beyond the classification-specific metrics a machine learning pipeline reports"); no article treats regression goodness-of-fit measures (R-squared, deviance, AIC/BIC) as a distinct topic.
- model-selection-regression: `methods/adjustment-set-selection` selects regression covariates by the causal-DAG backdoor criterion, a different selection principle from choosing variables by fit measures such as AIC or BIC.
- model-validation-committee: `regulation/pra-ss1-23-model-risk-management` covers independent validation as a function in depth (separate reporting lines, escalation standing) but names no committee structure, membership or reporting cadence.
- modification-gain-or-loss: `concepts/ifrs9-poci-assets` covers modification only for the narrower purchased/originated credit-impaired case, using a credit-adjusted EIR, a different mechanic from the general rule the node describes; `concepts/effective-interest-rate` states explicitly that its source paper "is silent on... the treatment of modifications"; `regulation/ifrs9-financial-instruments` has no modification section at all.
- monte-carlo-option-pricing: the vault's Monte Carlo references are all for credit-portfolio parameter estimation (`methods/vasicek-asset-correlation-estimation`) or are explicitly what a closed-form credit model avoids needing (`methods/creditrisk-plus-portfolio-model`: "this avoids the need for Monte Carlo simulation"), not derivative option pricing.

## Ledger (`ledger-25.yaml`)

20 entries: 17 reuse ids already seeded or proposed in wave 1, 3 are new. Every reused id needed a `note`, because in every case this batch's nodes want a section of the document that the inherited `claim` does not describe (e.g. `ifoa-cb2-core-reading-2026`'s seeded claim covers the 2008 crisis and advertising; this batch needs monetary policy, the money multiplier, monopoly and monopolistic competition from the same document). Claims, documents, tiers, acquisition and status were copied verbatim in every case; nothing was rewritten.

`needed_by` across the fragment covers 34 distinct node ids: the 30 fully uncovered nodes above, plus 4 partial-coverage remainders from the Attached section (ml-in-banking-risk-management's fraud-detection half, model-lifecycle's retirement stage, mortality-graduation's statistical-testing half, and mortality-forecast-error-sources' trend-discontinuity half), each under the id its own anchor body's default document already carries.

The 3 new ids: `up-ias721-course-notes` (a University of Pretoria enterprise-risk-management course several existing nodes already anchor to but no batch had proposed), `dl-actuarial-2026-l02-glm` (status `ingested`, following batch 1's activation-function precedent: the lecture is already in the vault as a cited source, but no wiki article treats the moment generating function as its own topic, so the gap is wiki-article scope rather than acquisition), and `iasb-ifrs9-standard-modification-of-financial-assets` (one paragraph-range id for IFRS 9 para 5.4.3/B5.4.6, following the shape the seeded `bcbs-d424-*` entries already established, since the existing `iasb-ifrs9-standard-cash-shortfall-and-hedge-types` id covers a different part of the standard).

No entry departs from the anchor-body default rule.

## Verification

`.venv/bin/python scripts/check.py`: all eleven rules pass (1560 nodes, 13 paths, 0 failures). `.venv/bin/python scripts/merge_ledger.py --dry-run`: no complaints against this fragment (the handful of "claim differs" notes it prints are disagreements between other batches' concurrently-staged fragments and the seeded values, not against any id this fragment introduces or reuses in a way that conflicts). `stray_writes` confirms all ten of this batch's own node writes fall inside the batch-25 manifest; `git diff` also shows roughly eighty other node files changed, all belonging to other batches running concurrently in the same shared working tree, none touched by this agent.
