# Phase 2 batch 18 attachment report

40 nodes worked. 12 attached, 28 uncovered. 15 total attachments.

## Attached

### hedge-accounting
Candidates: `regulation/ifrs9-financial-instruments` (open, matches), `regulation/ifrs9-financial-instruments-project-summary` (rejected, superseded duplicate).
Attached: `regulation/ifrs9-financial-instruments`. Its "Hedge accounting" section states "Hedge relationships qualify for accounting treatment when the hedged item and hedging instrument are economically related and the relationship meets the 80-125% effectiveness range at inception", the accounting-treatment mechanic the node describes. The project-summary article covers the same ground (it has its own "Hedge accounting" section, and even names the earnings-volatility angle more directly) but is a superseded T3 companion to the binding T1 standard, following the same precedent report-01 used for `amortised-cost-classification`, so it was not added alongside it.

### high-level-risk-management-role
Candidates: `regulation/bcbs-d328-corporate-governance` (open, matches), `concepts/three-lines-of-defence-assurance-model` (open, matches a different part).
Attached both. `bcbs-d328-corporate-governance`'s Principle 6 states the requirement directly: "a risk management function that is independent of business lines and has sufficient authority, resources, and board access to perform effectively." `three-lines-of-defence-assurance-model` covers the "why": its account of the Walker review's recommendation that a bank's chief risk officer hold "total independence from individual business units" and report to a separate board risk committee gives the crisis-era rationale the node's body asks for, which the governance-principles article states as a rule without the history behind it.

### high-quality-liquid-assets
Candidates: `regulation/bcbs-liquidity-coverage-ratio-original` (open, matches).
Attached: `regulation/bcbs-liquidity-coverage-ratio-original`. Its "High-quality liquid assets" section states the Level 1 (central bank reserves, government and central bank securities, no haircut) and Level 2 (high-grade corporate and covered bonds, 15% haircut, 40% cap) structure directly. Partial-scope note: this is the original BCBS 188 (2010) calibration, later expanded by BCBS 238 (2013); the vault holds no wiki article built from the revised standard, but the Level 1/Level 2 architecture this article states is the foundation that survived the revision, and `regulation/uk-liquidity-framework` (checked) does not restate the HQLA levels itself.

### icenet
Candidates: `methods/icenet-smoothness-and-monotonicity-constraints` (open, matches exactly).
Attached: `methods/icenet-smoothness-and-monotonicity-constraints`. Direct match, sourced from the same UCSC lecture (l08) this node is itself anchored to: "ICEnet makes them the object of the penalty... the model is fitted against a compound loss carrying three terms: the deviance loss, a smoothness penalty, and a monotonicity penalty."

### ifrs9
Candidates: `regulation/ifrs9-financial-instruments` (open, matches).
Attached: `regulation/ifrs9-financial-instruments`. Opens with "IFRS 9 is the IASB's binding accounting standard for financial instruments... Its three phases, classification and measurement, impairment, and hedge accounting", matching the node's summary of the standard directly.

### ifrs9-stage-allocation
Candidates: `concepts/ifrs9-expected-credit-loss` (open, matches the overall three-stage structure), `methods/ifrs9-sicr-triggers-and-staging` (open, matches the Stage 1-to-2 trigger in depth).
Attached both, covering different parts. `ifrs9-expected-credit-loss`'s "three-stage model" section states the 12-month/lifetime split across all three stages, which the node's body asks for. `ifrs9-sicr-triggers-and-staging` gives the significant-increase-in-credit-risk test's operationalisation (PD-comparison thresholds, qualitative triggers, the 30-DPD backstop) in the depth the node's anchor to paragraph 5.5.5 calls for, ground the overview article only touches in one sentence.

### ilaap
Candidates: `regulation/pra-ilaap` (open, matches exactly).
Attached: `regulation/pra-ilaap`. States it verbatim: "The Internal Liquidity Adequacy Assessment Process (ILAAP) is a firm-led self-assessment of all material liquidity and funding risks... The ILAAP is the liquidity counterpart to the ICAAP."

### impaired-assets
Candidates: `concepts/ifrs9-expected-credit-loss` (open, matches).
Attached: `concepts/ifrs9-expected-credit-loss`. Its three-stage-model section states "Stage 3 assets are credit-impaired; lifetime ECL also applies", which is the definitional match the node's "exposures a bank has recognised as having suffered a measurable fall in credit quality" claim needs. Partial-scope note: the article names the Stage 3/credit-impaired classification but does not itemise the standard's own indicators of impairment (significant financial difficulty, breach of contract, and so on).

### impairment-gain-or-loss
Candidates: `concepts/ifrs9-poci-assets` (open, matches partially).
Attached: `concepts/ifrs9-poci-assets`. Its "Loss allowance: cumulative change mechanics" section quotes the general rule the node describes ("subsequent deterioration is recognised as an impairment loss; subsequent improvement is recognised as an impairment gain") and cites paragraph 5.5.14 directly, one of the node's three anchors. Partial-scope note: the article states this mechanic inside the POCI-specific cumulative-change context rather than the general Stage 1-3 period-on-period case (paragraph 5.5.8, the node's other anchor), so the underlying P&L rule is covered but its general (non-POCI) application is not spelt out.

### in-context-learning
Candidates: `concepts/in-context-learning-tabular-actuarial-models` (open, matches).
Attached: `concepts/in-context-learning-tabular-actuarial-models`. States it directly: "A pre-trained model receives, at prediction time, a set of similar cases together with their outcomes, and adjusts its prediction from that context without any retraining."

### in-context-learning-credibility-transformer
Candidates: `concepts/in-context-learning-tabular-actuarial-models` (open, matches).
Attached: `concepts/in-context-learning-tabular-actuarial-models`. Its "Grafting context onto a credibility model" section describes the retrieval, decorator and causal-masking mechanism the node's body names. Partial-scope note: the node's own critique (that a diluted or self-correlated retrieved neighbourhood can add little accuracy while leaving explanations undisturbed) is not stated explicitly, though the article's own finding that the margin over the base model "is again slender" points the same direction without drawing the conclusion.

### individual-conditional-expectation
Candidates: `methods/icenet-smoothness-and-monotonicity-constraints` (open, matches almost word for word).
Attached: `methods/icenet-smoothness-and-monotonicity-constraints`. "An individual conditional expectation curve is obtained by holding one policy fixed, sweeping one covariate across a set of representative values, and recording the prediction at each. The partial dependence plot is the average of those curves over the portfolio."

## Uncovered (28)

**No vault content at all** (confirmed by both index and full-text grep across `vault/wiki`): health-cash-plan, health-care-product-design-merits-comparison, health-care-product-design-principles, health-care-regulatory-and-tax-regime, health-care-risk-mitigation-actions, health-insurance-benefit-structures, heat-equation, heath-jarrow-morton-model, high-volatility-commercial-real-estate-exposure, hull-white-model, hvcre-slotting-and-correlation-formula, hypergeometric-distribution, illiquid-asset-index-construction, implied-volatility, income-inequality-and-poverty, increasing-annuity-certain, indifference-curves, individual-investment-strategy.

**Passing mentions only, rejected:**
- hedge-funds: `regulation/counterparty-credit-risk-saccr` names "hedge funds and other non-bank financial intermediaries" as a high-risk CCR counterparty category requiring enhanced disclosure, one clause; no treatment of strategies, fee structures or investor liquidity terms.
- hedging: `regulation/basel-3-1-market-risk` mentions "legitimate hedging positions" inside its residual-risk-add-on discussion, one clause; no general definition of hedging as an offsetting position taken to reduce net risk.
- hypothesis-testing: `methods/statistical-power-analysis` uses null hypothesis, Type I error and power throughout, but entirely as applied vocabulary for choosing a PD point-prediction test; it never states the vocabulary as a foundational definition (sensitivity, specificity, critical region, p-value) the way the node needs.
- identity-initialisation: `concepts/deep-learning-foundations` names "residual connections" as getting their own textbook chapter "because they are what made depth trainable in practice", one clause in a table-of-contents-style survey; no treatment of the zero-weight initialisation mechanism itself.
- impairment-versus-default: `regulation/irb-definition-of-default` states that default "is the point at which a credit obligation is classified as impaired for regulatory capital purposes", one clause that uses "impaired" loosely to describe default itself rather than distinguishing the two tests the node is about.
- income-producing-real-estate-exposure: `regulation/eba-specialised-lending-risk-weights` names income-producing real estate (IPRE) as one of four specialised-lending categories under Article 147(8)/147(11) CRR, one clause; no statement of the cash-flow-dependence criterion that defines the category.
- income-protection-insurance: `regulation/pure-protection-market-study` lists "income protection" alongside term assurance and critical illness cover among the products the FCA's study covers, one clause; no description of the benefit mechanic.
- index-linked-contract: `regulation/eiopa-supervisory-monitoring` names "index-linked portfolios" inside a stress-test recommendation, one clause; no definition of the contract type.
- independence-of-random-variables: `methods/pluto-tasche-pd-estimator` and `methods/creditrisk-plus-portfolio-model` both use independent default events as a standing modelling assumption at length, but as an applied premise inside a specific estimator rather than a statement of the general condition or how it is checked from a joint distribution.

**Considered and deliberately not attached despite surface similarity:**
- historical-data-adjustment-for-expected-credit-losses: `methods/forward-looking-information-modelling` treats the closely related but different question of incorporating macroeconomic forecasts into PD/LGD regressions; it does not address the standard's own requirement (paragraph B5.5.52) to adjust historical loss experience for current conditions, strip non-recurring effects, and check that ECL movements track the economic data the entity's own methodology says should drive them.

## Ledger (`ledger-18.yaml`)

18 entries: 14 reuse an id already in `ledger-ids.yaml` (needed_by extended only, every other field copied verbatim, with a note where this batch's nodes need a different chapter of the same document than the seeded claim names, which is 13 of the 14); 4 are new.

Reused ids, grouped by document: `ifoa-sp1-core-reading-2026` (6 nodes: health-cash-plan, both health-care-product-design nodes, health-care-regulatory-and-tax-regime, health-care-risk-mitigation-actions, income-protection-insurance), `ifoa-cs1-core-reading-2026` (3: hypergeometric-distribution, independence-of-random-variables, hypothesis-testing), `ifoa-sp5-core-reading-2026` (3: illiquid-asset-index-construction, indifference-curves, hedge-funds), `ifoa-sp6-core-reading-2026` (3: heath-jarrow-morton-model, hull-white-model, implied-volatility), `up-wst211-course-notes` (2: hypergeometric-distribution, independence-of-random-variables), `ifoa-cm1-core-reading-2026` (2: health-insurance-benefit-structures, increasing-annuity-certain), `assa-f107-study-material-2026` (2: hedging, impairment-versus-default), and one node each against `ifoa-cm2-core-reading-2026`, `up-wtw386-course-notes`, `up-ias712-course-notes`, `ifoa-sp2-core-reading-2026`, `up-wst121-course-notes`, `up-wst221-course-notes`, `ifoa-sp9-core-reading-2026`. Only `up-wtw386-course-notes` (heat-equation) needed no note: its seeded claim already is the heat equation's own derivation.

Four new ids, all departing from a simple reuse: `up-ekn110-course-notes` for income-inequality-and-poverty, because its anchor (up.ekn110.10) is a distinct Pretoria first-year economics course from the up-ekn120-course-notes already seeded (development economics, growth divergence between countries, not distribution within one). `bcbs-d424-irb-specialised-lending-real-estate`, covering all three of high-volatility-commercial-real-estate-exposure, hvcre-slotting-and-correlation-formula and income-producing-real-estate-exposure, because the seeded `bcbs-d424-irb-risk-weight-functions` id covers only the general corporate risk-weight formula (Chapter CRE31) and not the specialised-lending real-estate definitions or the HVCRE correlation add-on these three nodes need; it is a separate entry against the same underlying standard rather than an extension. Two entries depart from the anchor-default rule outright because direct inspection showed their anchor's own document is already ingested and the gap is wiki-article scope rather than acquisition: `iasb-ifrs9-standard-historical-data-adjustment` for historical-data-adjustment-for-expected-credit-losses (the IFRS 9 standard is cited throughout the vault; paragraph B5.5.52 specifically has no dedicated treatment) and `dl-actuarial-2026-l12-identity-initialisation` for identity-initialisation (lecture 12 is already ingested via `concepts/in-context-learning-tabular-actuarial-models`, which covers the in-context-learning mechanism but not identity initialisation), both following the precedent report-01 set for `activation-function`. `merge_ledger.py --dry-run` reports "would write 73 entries (4 seeded)" with no complaints against this fragment.
