# Batch 10 report

Attached 11 of 40 nodes (15 attachments); 29 uncovered.

## Attached

- **credit-risk-mitigation** -> `regulation/crr-credit-risk-provisions`. Its "Credit risk mitigation" section covers funded and unfunded protection, the substitution approach, and cross-references credit insurance. Guarantees and credit insurance are covered; netting is not named explicitly.
- **credit-risk-model-validation** -> `regulation/irb-model-validation`. Its "Regulatory framework and independence requirements" section states validation must be periodic, independent of development, and organisationally separated, matching the node's scope/independence/frequency framing directly. (Initially considered `synthesis/internal-models-governance`, a hub that only links out to this treatment; displaced it after reading the linked article, per advisor guidance.)
- **credit-risk-modelling-approach** -> `methods/structural-credit-risk-models`. Its "Relation to the reduced-form alternative" section states the structural/reduced-form/intensity-based taxonomy almost verbatim to the node.
- **credit-risk-parameters-defaulted-assets** -> `regulation/irb-lgd-estimation`, `regulation/eba-pd-lgd-estimation-framework`. Both give ELBE and LGD-in-default (parameters for defaulted assets, distinct from PD/LGD/EAD) dedicated, substantive treatment.
- **credit-risk-strategy** -> `regulation/eba-loan-origination-monitoring`. Its "Governance and credit risk appetite" section states the credit risk strategy requirement and that "pricing must reflect the risk taken on at origination", matching the node's tolerance-plus-profitability framing.
- **credit-valuation-adjustment** -> `concepts/credit-valuation-adjustment`, `regulation/bcbs-d507-cva-framework`. Direct, full-article treatment of CVA definition, mechanics and the regulatory capital charge.
- **crr-eu** -> `regulation/crr`. Direct CRR overview article.
- **cva-approach-choice**, **cva-capital-requirement-scope**, **cva-hedge-eligibility** -> `regulation/bcbs-d507-cva-framework`. Approach choice: BA-CVA/SA-CVA/materiality-threshold treated, but the node's partial-use carve-out (an SA-CVA bank still applying BA-CVA to part of its book) is not named. Scope: near-verbatim match on covered transactions and the notional threshold. Hedge eligibility: BA-CVA's eligible-instrument list and beta cap are covered; the "entered into for the purpose of mitigating CVA risk and managed as such" condition and SA-CVA's own hedge restrictions are not.
- **cybercrime-risk-management** -> `regulation/pra-cyber-resilience-stress-test-2025`. Substantive but narrow: one voluntary thematic exercise's findings on defence/recovery capability, not a survey of bank IT risk categories generally.

## Uncovered (29), by cluster

**Governance/business (credit-risk-committee, credit-risk-due-diligence-requirements, credit-scoring, cumulative-liquidity-model, currency-as-asset-class, currency-risk, custodian-role, customer-needs-analysis, customer-relationship-profitability, cybercrime-and-fraud-risk):** no vault article treats the specific subject. `credit-risk-due-diligence-requirements`: confirmed via direct read of `vault/markdown/bcbs/d424.md` lines 153-166 that SA paragraphs 4-6 are exactly on-subject; no wiki article cites them. `credit-scoring`: vault's ML credit-scoring articles are model-methodology reviews (gradient boosting vs logistic regression), not the bought-vs-built-score/asset-writing-strategy framing the node needs. `cybercrime-and-fraud-risk`: `methods/statistical-fraud-detection` and the ECB AI article both treat detection methodology, not the risk category itself; no cyber-attack coverage at all.

**CVA (cva-exposure-modelling-requirements):** anchor confirmed live and correct, not superseded. Direct read of `vault/markdown/bcbs/d424.md` line 5122 (CVA para 31) shows the exposure-model/accounting-CVA-consistency requirement verbatim. `regulation/bcbs-d507-cva-framework` describes SA-CVA only as "sensitivities-based... reduced granularity" and never discusses the underlying exposure-model mechanics or accounting-CVA consistency, so it is a related-but-different subject, not a substantive section on this node.

**Statistics/data-eng pedagogy (cross-validation, curtate-future-lifetime, curve-fitting-and-linear-programming, data-analysis-aims, data-analysis-lifecycle, data-analysis-process, data-governance-and-ethics, data-grouping-for-homogeneity, data-leakage, data-protection-regulation-banking, data-provenance-and-scale, data-quality-checks-and-limitations, data-requirements-for-valuation, data-sources-and-characteristics, data-visualisation, data-wrangling, database-driven-statistical-modelling):** consistently zero. Where the vault uses the same words it is a different subject: `data-leakage` finds only privacy/prompt/spreadsheet "leakage"; `data-quality-checks-and-limitations` finds `concepts/data-quality-dimensions`, a dbt/DAMA pipeline-testing article, not actuarial data adequacy assessment; `data-wrangling`/`data-visualisation` are named only as tool capabilities inside `methods/validation-reporting`, a passing mention.

## Ledger

Proposed `.staging/phase-2/ledger-10.yaml`: 17 entries, 11 reusing ids already minted by earlier batches (extending `needed_by` only, no optional fields, to avoid note conflicts), 5 new (`up-wst111-course-notes`, `up-wst311-course-notes`, `up-wtw152-course-notes`, `dl-actuarial-2026-l06-ensembling-embedding`, `bcbs-d424-cva-exposure-model-requirements`). The `dl-actuarial-2026-l06` url follows the exact pattern of the five already-seeded lecture urls but was not fetched to confirm it resolves. `merge_ledger.py --dry-run` completed with only pre-existing, unrelated note collisions from other concurrent batches; no complaint touched a ledger-10 entry. `bcbs-d424-sa-and-intro-provisions` reused with no note added (existing note covers different paragraphs); the SA para 4-6 finding above is recorded here instead, per the wave brief's guidance that the merge keeps only the first writer's note.

## check.py

`1560 nodes, 13 paths, 0 failures`

## Ambiguity

None in the brief itself. One genuine judgement call: `credit-risk-model-validation`'s anchor (assa.f207.1.3, general banking governance) is IRB-specific in the attached article; flagged above rather than treated as a clean match.
