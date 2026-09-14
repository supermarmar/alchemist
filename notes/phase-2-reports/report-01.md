# Phase 2 batch 1 attachment report

40 nodes worked. 6 attached, 34 uncovered. 7 total attachments.

## Attached

### accounting-for-impairments
Candidates: `concepts/ifrs9-expected-credit-loss` (open, matches directly), `regulation/ifrs9-financial-instruments` (open, broader IFRS 9 overview with a shorter impairment section).
Attached: `concepts/ifrs9-expected-credit-loss`. It is the dedicated ECL/impairment article; the broader overview would have been a weaker second citation for the same ground, so it was left off.

### accounting-regulatory-and-risk-approaches
Candidates: `methods/credit-loss-modelling-frameworks` (open, matches).
Attached: `methods/credit-loss-modelling-frameworks`. Opens on "each places different demands on the same underlying credit models" and covers the accounting-versus-regulatory divergence (IFRS 9/CECL vs Basel A-IRB, numerator/denominator interaction) and the internal-model-reuse layer in its "Model reuse and calibration adjustments" section. Partial-scope note: it does not name a separate "internal risk-based" view as its own third category; the coverage is real but not a perfect three-way match to the node's framing.

### actual-versus-predicted-plot
Candidates: `concepts/balance-property-and-auto-calibration` (open, matches exactly).
Attached: `concepts/balance-property-and-auto-calibration`. States the diagnostic verbatim ("built out-of-sample by binning on the predictor into deciles and averaging actuals and predictions within each bin"). Its source is the same UCSC lecture (l07) this node is itself anchored to.

### actuarial-professional-standards
Candidates: `regulation/technical-actuarial-standards` (open, matches half the node).
Attached: `regulation/technical-actuarial-standards`. Covers the "technical actuarial standards" half of the node (TAS 100/200, seven Principles) in full. The node also names a professional code of conduct, which the vault does not hold; not a reason to withhold the half that is covered.

### additional-national-capital-requirements
Candidates: `regulation/pra-capital-buffers-ccyb-srb` (open), `regulation/pillar-2a-capital-framework` (open), `regulation/countercyclical-capital-buffer` (rejected).
Attached both PRA articles: buffers (CCyB/CCoB/G-SII/O-SII/SRB) and Pillar 2A together cover "capital requirements or buffers a national regulator imposes above the Basel minimum". Rejected `countercyclical-capital-buffer`: it is a BCBS survey of cross-jurisdiction CCyB practice, not framed around a national regulator's addition to a Basel floor, and is subsumed by the PRA buffers article for UK purposes.

### amortised-cost-classification
Candidates: `regulation/ifrs9-financial-instruments` (open, matches exactly), `regulation/ifrs9-financial-instruments-project-summary` (rejected, superseded duplicate).
Attached: `regulation/ifrs9-financial-instruments`. Its "Classification and measurement" section states the business-model-plus-SPPI test verbatim. The project-summary article covers the identical ground but is a superseded T3 companion to the binding standard, so it was not added alongside it.

## Uncovered (34)

Grouped by why, with the strongest rejected candidate named where one existed.

**No vault content at all** (confirmed by both index grep and full-text grep across `vault/wiki`): abstract-vector-space, accumulated-value, accumulating-with-profits-contract, acquisitions-and-disposals-assessment, active-management-styles, actual-versus-expected-analysis, actuarial-advisory-roles, actuarial-cash-flow-model, actuarial-funding, actuarial-investigation, actuarial-model-applications, actuarial-model-uses, actuarial-modelling-process, actuarial-problem-solving-approaches, actuarial-professionalism-in-banking, actuarial-techniques-in-banking, adapting-to-risk-environment-change, adjustment-coefficient, adjustment-coefficient-reinsurance-optimisation, advertising-and-demand, advisory-services-pricing, agency-risk, aggregate-demand-and-supply, aggregate-expenditure-model, alternative-bank, american-option-pricing-methods, aml-and-sanctions-compliance.

**Passing mentions only, rejected:**
- 2008-financial-crisis-and-recovery: `entities/basel-accord-evolution` cites 2007-09 as Basel III's trigger in one sentence; no treatment of the crisis itself (monetary policy, stimulus/austerity, European aftershocks).
- actual-versus-potential-growth: `regulation/countercyclical-capital-buffer` lists "the output gap" as one of several CCyB-neutrality indicators in one clause; no explanation of potential vs actual growth.
- activation-function: the underlying lecture (vault `markdown/courses/2026_eth_deep-learning-actuarial-04-05-feed-forward-networks.md`) has a full "Activation functions" section, but the only attachable wiki article built from it, `methods/feed-forward-networks-claim-frequency`, mentions activation in one clause. Logged in the ledger as a wiki-coverage gap rather than an acquisition gap, since the source is already ingested.
- age-period-cohort-mortality-model: `methods/mortality-modelling` names an "age-period-cohort extension" in one clause, sourced to a T5 presentation slide, with no model structure or identifiability constraint given.
- agency-risk: `regulation/eba-esg-green-brown-prudential-factors` uses a principal-agent model as an analytical device for one ESG argument; not a treatment of agency risk generally.

**Considered and deliberately not attached despite surface similarity:**
- age-period-cohort: `methods/breeden-2016-lifecycle-environment-loan-level-forecasts` treats a credit-modelling instance of age/vintage/environment confounding, but frames it as short-history estimation difficulty rather than stating the general identification result (that period equals age plus cohort exactly, so at most two of three are identifiable). Judged too applied to draft the generic stats node from; the vault's own anchor for this node (ucsc.dl-actuarial-2026.l01) turned out not to cover it either (see ledger note).

## Ledger (`ledger-01.yaml`)

18 entries: 16 new documents plus two that extend already-seeded ids (`ifoa-cm1-core-reading-2026`, `ifoa-cs2-core-reading-2026`) with this batch's nodes added to `needed_by` only, all other fields copied verbatim. `merge_ledger.py --dry-run` reports "would write 20 entries (4 seeded)" with no complaints.

Proposed documents, grouped by the node's own anchor body per the brief's default rule: IFoA CB2/SP5/CP1/SP7/SP2/SP9/CM2/SP6 Core Reading 2026 (5, 1, 6, 1, 1, 2, 2, 1 nodes respectively), ASSA F107/F207 Study Material 2026 (4 and 2 nodes), University of Pretoria WTW221/IAS712/LEW700/IAS211 Course Notes (1 node each). Two exceptions to the anchor-default rule, both explained in the ledger's `note` field: `dl-actuarial-2026-l04-05-fnn` for activation-function is the anchor body's own document, but logged as `status: ingested` with a note that the gap is wiki-article scope, not acquisition, since the source is already in the vault; `holford-1983-age-period-cohort` for age-period-cohort departs from the anchor body entirely because that lecture (l01) turned out to contain no age-period-cohort content on direct inspection.
