# Phase 2 batch 38 attachment report

40 nodes worked. 10 attached, 30 uncovered. 10 total attachments.

## Attached

### thirty-days-past-due-presumption
Candidates: `methods/ifrs9-sicr-triggers-and-staging` (open, matches, dedicated subsection), `concepts/ifrs9-expected-credit-loss` (open, matches, one-sentence citation only).
Attached: `methods/ifrs9-sicr-triggers-and-staging`. Its "Qualitative triggers and the 30-DPD backstop" section states the node's subject directly: "the 30-days-past-due rebuttable presumption in IFRS 9 paragraph 5.5.11 must function as a backstop rather than a primary trigger," and that supervisors expect the framework to catch deterioration "before they reach 30 DPD, not that the backstop handles the majority of Stage 2 transfers." `concepts/ifrs9-expected-credit-loss` states the same rule in one clause ("A rebuttable presumption applies when an asset is 30 days past due") without the backstop framing, so per the brief's overlap rule the dedicated treatment is attached and the broader overview left off. Partial-scope note: neither article discusses the specific rebuttal mechanics (what "reasonable and supportable information" showing risk has not increased would look like).

### three-lines-of-defence
Candidates: `concepts/three-lines-of-defence-assurance-model` (open, matches exactly, dedicated).
Attached: `concepts/three-lines-of-defence-assurance-model`. Quotes BCBS 223 directly: "The business units are the first line of defence... The second line of defence includes the support functions... The third line of defence is the internal audit function." Covers the three-role separation the node describes in full, plus context (the IIA's 2020 rewrite, the PRA's SS5/16 expectation) the node's stub body does not need but does not contradict.

### through-the-cycle-probability-of-default
Candidates: `methods/credit-risk-procyclicality` (open, matches, dedicated paragraph), `methods/single-factor-credit-risk-model-vasicek-and-belkin` and `methods/ifrs9-vasicek-segment-to-rating-grade` (both open, use "through-the-cycle transition matrix" as a technical input without defining the concept, rejected as passing use rather than treatment).
Attached: `methods/credit-risk-procyclicality`. States: "through-the-cycle rating systems, which assign ratings on the basis of long-run average credit quality rather than current conditions, produce more stable capital requirements than point-in-time systems," and names the trade-off against pricing sensitivity. This is the node's exact subject with a definition and a use (capital-requirement stability), not merely a term in passing. Partial-scope note: doesn't cover the specific "averaging the realised default rate over calendar time" recovery mechanic the node's second sentence describes.

### tier-1-capital / tier-2-capital
Candidates: `regulation/eu-crr-2013-own-funds` (open, matches both nodes exactly, dedicated).
Attached to both nodes: `regulation/eu-crr-2013-own-funds`. Its "Capital tiers and instrument eligibility" section states CET1 and AT1 (together, Tier 1) absorb losses "on a going-concern basis," matching tier-1-capital's definition verbatim in substance, and states Tier 2 instruments "provide gone-concern loss absorption," matching tier-2-capital's definition. One article, attached to both nodes since it treats both tiers with equal depth in the same section structure.

### total-capital-requirement
Candidates: `regulation/pillar-2a-capital-framework` (open, matches, one direct sentence), `regulation/pra-icaap-and-pillar-2` (open, covers the PRA Buffer/Pillar 2B mechanism but not the summation itself, considered and left off as the less direct match), `regulation/basel-3-1-uk-implementation` (open, broad Basel 3.1 overview, no TCR-specific statement, rejected).
Attached: `regulation/pillar-2a-capital-framework`. States Pillar 2A "sits alongside the minimum Pillar 1 requirement and systemic buffers as one of three layers of the overall capital stack," which is the node's sum-of-three-layers definition stated directly. Partial-scope note: doesn't enumerate the buffers themselves (CCoB, CCyB, G-SIB buffer) or use the term "total capital requirement."

### total-loss-absorbing-capacity
Candidates: `regulation/fsb-tlac-gone-concern-loss-absorption` (open, matches exactly, dedicated), `regulation/uk-bank-resolution-mrel` (open, covers the "EU cousin" MREL the node mentions, but as the UK-specific implementation of TLAC rather than the node's core subject).
Attached: `regulation/fsb-tlac-gone-concern-loss-absorption` only. Defines TLAC as the standard "requiring global systemically important banks (G-SIBs) to maintain sufficient loss-absorbing and recapitalisation capacity so they can be resolved in an orderly way without recourse to public funds," and its own text already states the MREL relationship the node's second clause needs ("forms the basis for MREL frameworks implemented in the UK, the EU, and other major jurisdictions"), so the UK-specific MREL article was not attached separately as it would duplicate ground this article already covers for the node's purposes.

### transaction-costs
Candidates: `concepts/effective-interest-rate` (open, matches, direct paragraph).
Attached: `concepts/effective-interest-rate`. States: "Where a loan carries upfront origination fees, processing costs, or other charges that are integral to the lending arrangement, the EIR is higher than the nominal contractual interest rate, because those costs are spread over the expected life of the instrument," and that such costs "are amortised into interest income over the asset's expected life rather than recognised immediately at origination." Matches the node's mechanism precisely. Partial-scope note: doesn't state the formal "would not have arisen had the entity not acquired, issued or disposed of" IFRS 9 B5.4.8 definition.

### twelve-month-versus-lifetime-expected-credit-losses
Candidates: `concepts/ifrs9-expected-credit-loss` (open, matches, dedicated section).
Attached: `concepts/ifrs9-expected-credit-loss`. Its "The three-stage model" section states: "Stage 1 assets are those for which credit risk has not increased significantly since origination; the allowance equals 12-month ECL. Stage 2 assets have experienced a significant increase in credit risk (SICR) since origination but are not yet credit-impaired; the allowance equals lifetime ECL." Partial-scope note: doesn't state the node's specific "12-month ECL is the portion of lifetime ECL attributable to default events possible within twelve months" nuance, nor the distinction from a shorter-horizon loss estimate or from cash shortfalls expected within the year, which the node's anchor paragraph (IFRS 9 B5.5.43) addresses directly.

### unbiasedness
Candidates: `concepts/balance-property-and-auto-calibration` (open, matches, named section), `methods/ols-assumption-violations` (open, uses "unbiased" as a running property across four Gauss-Markov violations but without stating the underlying definition, considered and left off as the weaker match).
Attached: `concepts/balance-property-and-auto-calibration`. Its "Unbiasedness at the portfolio level" section states: "Global statistical unbiasedness is an out-of-sample property: the expected exposure-weighted prediction on fresh data equals the expected exposure-weighted claim," structurally the same statement as the node's "expected value equals the parameter it is estimating." Partial-scope note: phrased for an insurance pricing model rather than as the general estimator-theory definition, and the node's stub form doesn't need more.

## Uncovered (30)

Grouped by why, with the strongest rejected candidate named where one existed.

**No vault content at all** (confirmed by both index grep and full-text grep across `vault/wiki`): theory-of-finance, time-distributed-layer, time-inhomogeneous-markov-chain, time-series-applications-in-finance, time-series-forecasting, time-series-markov-representation, time-series-model-identification-and-diagnostics, time-series-model-selection, time-series-operator-notation, time-series-stationarity, time-value-of-money, topological-properties-of-euclidean-space, total-return-swap, trade-protectionism, trading-and-funding-policy, trading-income, transactional-product-pricing, transition-intensity-likelihood, transition-intensity-mle, transition-management, transition-probability-estimation-from-exposure, treasury-bond-futures, treasury-function-structure, twin-peaks-regulation, underwriting-approaches, underwriting-level-factors.

**Passing mentions only, rejected:**
- tracking-error: `methods/ifrs9-ecl-backtesting-and-validation` uses the phrase "tracking errors" once, but for macro-scenario forecast accuracy in IFRS 9 backtesting ("material tracking errors triggering a formal review of the scenario design framework"), a different concept entirely from a portfolio's return standard deviation against a benchmark.
- treating-customers-fairly: `regulation/debt-collection-sector-conduct-supervision` quotes the phrase once, inside a 2021 FCA portfolio letter's historical finding on root causes of harm ("insufficient emphasis on treating customers fairly within firm culture"), not as the regulatory principle itself.

**Considered and deliberately not attached despite surface similarity:**
- two-state-credit-rating-model: `methods/structural-credit-risk-models`'s "Relation to the reduced-form alternative" section discusses intensity-based reduced-form pricing as a contrast to Merton's structural model, but doesn't describe a two-state performing/defaulted model at constant transition intensity, the node's specific subject.
- two-state-decrement-model: `methods/lgd-survival-analysis` and related LGD survival articles (`methods/ifrs9-lgd-term-structure`) build Cox and Kaplan-Meier survival models for LGD recovery timing, using the same survival-function apparatus, but model recovery from default rather than the alive/dead actuarial decrement the node describes, and never identify the model as equivalent to the random lifetime model.
- treating-customers-fairly: `regulation/fca-consumer-duty` covers the FCA's current retail-conduct framework in depth (three cross-cutting rules, four outcome areas) but is the 2023 Consumer Duty regime that superseded TCF; it never names Treating Customers Fairly or Principle 6, and the node's IFoA CP1 anchor is specifically the older named model.

## Ledger (`ledger-38.yaml`)

14 entries, all 14 reusing an existing id from `proposed-ids.yaml`; no new documents were needed. Every uncovered node's anchor body already had a document proposed by an earlier wave, so this batch only extended `needed_by` and added a note on each entry naming the different unit or section its nodes need, since none of the fourteen seeded claims already described that ground (`ifoa-cs2-core-reading-2026`'s seeded claim is survival graduation; batch 38's ten CS2 nodes need Unit 2 time series and Unit 4 transition intensities instead, so the note names both). `merge_ledger.py --dry-run` reports "would write 94 entries (4 seeded)" with no complaints; the disagreement notes it printed (`up-wtw114-course-notes`, `up-wst111-course-notes`, `up-wtw354-course-notes`, `up-ekn110-course-notes`, `ifoa-sp1-core-reading-2026`'s `primary_alternative`, `dl-actuarial-2026-l02-glm`) are pre-existing conflicts between other batches' fragments, none of which batch 38 touches or introduces.

One judgement call the brief didn't cover directly: `up-fbs122-course-notes`'s seeded claim (discounting project cash flows to present value) already states the time-value-of-money concept the node needs, unlike most of this batch's reused ids, so that entry's note records the match rather than a departure, and only lists the node's five other, unledgered anchor bodies. One entry, `dl-actuarial-2026-l10-11-transformers` for time-distributed-layer, is flagged as a likely wiki-article scope gap on an already-ingested source rather than an acquisition gap, following wave 1's `activation-function` precedent, since the lecture that defines attention also introduces the shared-weight feed-forward layer beneath it.
