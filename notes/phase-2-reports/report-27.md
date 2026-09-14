# Phase 2 batch 27 attachment report

40 nodes worked. 10 attached, 30 uncovered. 10 total (article, node) attachments.

## Attached

### non-proportional-reinsurance-pricing
Candidates: `methods/reinsurance-pricing` (open, matches exactly).
Attached: `methods/reinsurance-pricing`. Its opening paragraph states the node's two methods directly: "Pricing an excess-of-loss (XL) reinsurance treaty combines two techniques: experience rating, which trends and develops the treaty's own historical losses, and exposure rating, which derives expected layer losses from a curve fitted to industry severity data." The "Experience and exposure rating" section names burning cost explicitly: "Experience rating, or burn-cost analysis, gathers roughly ten years of premium and losses."

### nsfr-calculation
Candidates: `regulation/bcbs-liquidity-nsfr-monitoring-tools` (open, matches exactly, dedicated).
Attached: `regulation/bcbs-liquidity-nsfr-monitoring-tools`. Its "Net Stable Funding Ratio" section states the calculation precisely: "The NSFR is expressed as the ratio of available stable funding to required stable funding... Available stable funding is calculated by applying stability weights to the bank's liabilities and regulatory capital... Required stable funding is calculated by applying illiquidity weights to the bank's assets."

### nth-to-default-basket
Candidates: `methods/default-correlation-copula-models` (open, matches the correlation-dependency half only).
Attached: `methods/default-correlation-copula-models`. States that "pricing first-to-default and similar contracts, which the paper closes by illustrating, is precisely where that [normal-copula tail-behaviour] choice bites hardest," directly supporting the node's claim that basket price depends on default correlation between reference entities. Partial-scope limit: covers the correlation-dependency mechanism, not the basket's own payout structure or notional weighting.

### obligor-group-entity
Candidates: `regulation/pra-large-exposures-connected-clients` (open, matches exactly, dedicated).
Attached: `regulation/pra-large-exposures-connected-clients`. States the definition directly: "A group of connected clients (GCC) is a set of entities constituting a single risk, either because one of them directly or indirectly controls the others, or because they are so interconnected that financial problems at one would likely reach the rest," and gives its use: measuring exposure and concentration at group level under the large exposures framework.

### off-balance-sheet-credit-conversion-factors
Candidates: `regulation/eba-off-balance-sheet-ccf-standardised` (open, matches, dedicated), `regulation/eba-rts-obs-items-ccf` (open, near-duplicate of the same EBA/RTS/2025/06 source).
Attached: `regulation/eba-off-balance-sheet-ccf-standardised` only, the article whose own frontmatter names it "the mandated target slug"; the near-duplicate is left off per the brief's rule on overlapping coverage. States "applicable percentages ranging from 100% for bucket 1 to 10% for bucket 5," matching the node's own range. Partial-scope limit: covers the standardised-approach bucket table; does not address the node's second clause that the IRB foundation approach applies the same factors.

### operational-risk
Candidates: `regulation/operational-risk-capital-approaches` (open, matches the regulatory-capital framing), `regulation/euc-supervisory-expectations` (open, states the BCBS definition verbatim but only as a preamble clause inside an argument about end-user-computing governance, rejected as a passing mention).
Attached: `regulation/operational-risk-capital-approaches`. Partial-scope limit: treats operational risk through the Pillar 1 regulatory-capital lens (definition, history, standardised approach); does not independently cover the broader risk-management framing the node's ASSA and IFoA anchors also carry.

### operational-risk-capital-assessment
Candidates: `regulation/operational-risk-capital-approaches` (open, matches).
Attached: `regulation/operational-risk-capital-approaches`, the vault's dedicated article on assessing operational risk capital. Partial-scope limit: does not name conduct risk specifically.

### operational-risk-internal-models
Candidates: `regulation/operational-risk-capital-approaches` (open, matches).
Attached: `regulation/operational-risk-capital-approaches`. Its History section states the benefits/limitations debate directly: the 2006 AMA survey "recorded wide divergence in how banks combined internal loss data, external data, scenario analysis"; the 2016 consultation "proposed abandoning the exercise... on comparability and complexity grounds."

### operational-risk-loss-data-requirement-threshold
Candidates: `regulation/operational-risk-capital-approaches` (open, matches exactly).
Attached: `regulation/operational-risk-capital-approaches`. States: "Banks with a Business Indicator above €1bn must use loss data as a direct input... Banks holding fewer than five years of high-quality loss data calculate on the Business Indicator Component alone."

### operational-risk-loss-data-standards
Candidates: `regulation/operational-risk-capital-approaches` (open, matches the gross-loss and inclusion/exclusion half).
Attached: `regulation/operational-risk-capital-approaches`. States: "The framework specifies gross loss net of recoveries, with recoveries counted only once received, and requires inclusion of direct charges and impairments, consequential costs such as legal fees... and timing losses spanning more than one accounting period." Partial-scope limit: does not address the accounting-recognition dating requirement or the requirement to aggregate losses from one common underlying event.

## Uncovered (30)

**No vault content at all** (confirmed by both index grep and full-text grep across `vault/wiki`): non-interest-revenue, non-retail-credit-risk-qualitative-factors, non-unit-reserves, nonlinear-time-series-model, normal-distribution, nsfr-compliance, nth-to-default-credit-derivative-treatment, numerical-error-and-convergence, numerical-integration, numerical-linear-system-solution, numerical-methods-for-initial-value-problems, observational-plan, occupation-time, oligopoly, on-balance-sheet-netting, operational-and-insurance-risk-management, operational-loss-amounts-by-type, operational-loss-dates-by-type, operational-loss-event-grouping, operational-risk-consolidated-and-subsidiary-calculation, operational-risk-events, operational-risk-key-risk-indicators, operational-risk-loss-event-types, operational-risk-loss-exclusion-approval.

**Passing mentions only, rejected:**
- normal-versus-observed-distributions: no article anywhere in the vault pairs Value at Risk with a normal, lognormal, fat-tail or skew term; searched directly rather than assuming absence.
- nonparametric-methods: `methods/ml-credit-scoring-empirical-and-review` uses "nonparametric regression setting" once, describing Kruppa et al.'s random-forest probability-estimator framework, a machine-learning modelling sense unrelated to rank-based hypothesis testing.
- operational-risk-correlation-dependence: `regulation/operational-risk-capital-approaches`'s History section names "dependence between units" once, as one of five items the 2011 AMA supervisory guidelines addressed, with no exposition of what the dependence assumption is or how it is modelled; no dedicated wiki article on the underlying source (BCBS 196) exists.
- operational-risk-data-integration: the same History section names combining "internal loss data, external data, scenario analysis" once, describing the 2006 AMA practice survey's finding of divergence, not the rationale or method for combining them.
- operational-risk-distribution-assumptions: same History section names "distributional assumptions" once in the same five-item list; `methods/aggregate-loss-models` (Panjer recursion) is general-insurance frequency-severity machinery with no operational-risk framing and no treatment of heavy-tailed severity choice, and was already judged too thin for a single-distribution node by batch 26 (rejected there for `negative-binomial-distribution` on identical grounds).

**Considered and deliberately not attached despite surface similarity:**
- oligopoly: `concepts/ev-auto-loan-credit-risk` and `concepts/bbb-small-business-finance-markets` both use "market structure" as a generic phrase (US EV-loan data provenance; UK SME lending volumes), not the theoretical concept of a small-firm-dominated market.
- on-balance-sheet-netting: `regulation/fsb-tlac-gone-concern-loss-absorption` names "set-off or netting rights" once, as a TLAC-eligibility exclusion criterion for derivatives and secured liabilities, not deposit-loan netting under a right of set-off.
- non-retail-credit-risk-qualitative-factors: `methods/block-design-regression` uses "qualitative factors" for behavioural inputs to a staged credit-scoring regression, and `regulation/pra-ss1-23-model-risk-management` uses it for model-materiality tiering; neither treats management quality or industry outlook in an obligor assessment.
- numerical-optimisation-introduction: `methods/mathematics-for-machine-learning` lists "Continuous optimisation covers convexity, gradient descent and constrained optimisation with Lagrange multipliers" as a description of a textbook chapter's contents, not exposition in the article's own text, the same "coverage description of an external source" pattern batch 26 flagged for a different node.
- nth-to-default-credit-derivative-treatment: `concepts/debit-valuation-adjustment` uses "first-to-default convention" for the bilateral CVA/DVA valuation convention (whoever defaults first between two counterparties), an unrelated meaning from a basket credit derivative.

## Ledger (`ledger-27.yaml`)

13 entries: 10 reuse an existing id from `proposed-ids.yaml` (each with a note naming the further section this batch needs, since none of the reused claims already covered batch 27's ground) and 3 are new documents. `merge_ledger.py --dry-run` reports "would write 98 entries (4 seeded)" with no complaints against any id this batch touched; the eight disagreement notes it printed are pre-existing conflicts between other batches' fragments (`up-wtw114-course-notes`, `up-wst111-course-notes`, `up-wtw354-course-notes`, `up-ekn110-course-notes`, `ifoa-sp1-core-reading-2026`, `dl-actuarial-2026-l02-glm`, `up-wtw218-course-notes`).

New documents: two BCBS d424 operational-risk-chapter paragraphs not covered by any existing ledger id (consolidated-versus-subsidiary Business Indicator calculation, paragraph 14; loss-exclusion supervisory approval, paragraph 27), both ledgered `status: ingested` since d424 is already an ingested source for this batch's two attached articles and neither paragraph is an acquisition gap, only a wiki-article scope gap. One new University of Pretoria course code (WTW123, an introductory numerical-methods module distinct from WTW383, covering four of this batch's uncovered nodes: numerical integration, initial-value problems, linear systems and error/convergence).

One judgement call the brief didn't cover directly: `nth-to-default-credit-derivative-treatment` carries two paragraph anchors within the *same* document and chapter (bcbs.d424.sa.para-198 and para-89), rather than two different anchor bodies. Treated this as the reuse-with-note case rather than the multi-anchor-body case: reused `bcbs-d424-credit-derivative-recognition` (paragraphs 195-198, which already covers para-198's protection-buyer recognition ground) and noted that para-89's protection-seller capital treatment is a further need within the same Standardised Approach chapter, rather than opening a second entry.
