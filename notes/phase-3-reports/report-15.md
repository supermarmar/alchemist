# Phase 3 batch 15 report

Nodes written: 20. Nodes written from vault articles: 3 (economic-loss-definition-for-lgd,
excess-of-loss-reinsurance, expected-credit-loss). Nodes written without vault articles: 17
(stub, anchor and standard treatment of the subject). Nodes not landed: 20, all left as
`stub` and tagged qualitative below.

## Nodes written

- economic-loss-definition-for-lgd: sources read: regulation/irb-lgd-estimation. Spends:
  obj.exposure:credit, obj.exposure:regulation.
- elasticity-of-demand-and-supply: sources read: stub and anchor only. Spends: none.
- embedded-value-profit-analysis: sources read: stub and anchor only. Spends: none.
- empirical-bayes-credibility-theory: sources read: methods/credibility-theory. Spends:
  obj.credibility-weight:actuarial.
- entity-embedding: sources read: methods/entity-embedding-and-network-ensembling. Spends:
  none.
- excess-of-loss-reinsurance: sources read: concepts/reinsurance,
  methods/reinsurance-pricing. Spends: none.
- expected-credit-loss: sources read: concepts/ifrs9-expected-credit-loss,
  regulation/ifrs9-financial-instruments (read for context, not listed in
  `vault_articles`). Spends: obj.exposure:credit, obj.exposure:regulation.
- expected-utility-theorem: sources read: stub and anchor only. Spends: none.
- exposed-to-risk: sources read: stub and anchor only. Spends: none.
- extreme-value-theory: sources read: stub and anchor only. Spends: none.
- factors-and-interactions: sources read: methods/ols-predictor-importance (read for
  context; the page draws on the standard GLM interaction-term treatment rather than a
  specific claim in the article). Spends: obj.coefficients:stats.
- feed-forward-neural-network: sources read: methods/feed-forward-networks-claim-frequency
  (read for context). Spends: none.
- filtered-time-series: sources read: stub and anchor only. Spends: none.
- formal-definition-of-a-limit: sources read: stub and anchor only. Spends: none.
- forward-contract-pricing: sources read: stub and anchor only. Spends:
  obj.discount-factor:fin-eng.
- forward-contract-valuation: sources read: stub and anchor only. Spends:
  obj.discount-factor:fin-eng.
- forward-rate-agreements: sources read: stub and anchor only. Spends: none.
- frequency-severity-approach: sources read: methods/aggregate-loss-models. Spends: none.
- futures-hedging: sources read: stub and anchor only. Spends: none.
- gamma-distribution: sources read: stub and anchor only. Spends: none.

No collision candidates and no split candidates arose in this batch; every node fitted one
display block and the node's first-listed domain's spelling throughout.

## Not landed

- economic-balance-sheet-approach: qualitative: a valuation basis (market-consistent
  versus accounting), not a computed quantity with a formula of its own.
- economic-stimulus-and-business-output: qualitative: the price/output response split is
  descriptive at this syllabus depth, with no single standard-treatment formula.
- economies-of-scale: qualitative: describes the shape of long-run average cost, not a
  formula for a named object.
- eligible-hedging-instruments: qualitative: an IFRS 9 eligibility checklist, no formula.
- embedded-options-and-guarantees: qualitative: descriptive; the costing formula belongs
  to the sibling node investment-guarantee-cost-methods.
- enterprise-risk-management-benefits: qualitative: a list of organisational benefits.
- equity-fundamental-analysis: qualitative: names the factors driving an equity price
  descriptively, with no formula of its own at this syllabus depth.
- exchange-rate-determination: qualitative: a supply-and-demand equilibrium account, no
  single standard formula for this object.
- exchange-traded-versus-over-the-counter-contracts: qualitative: a market-structure
  comparison, no formula.
- external-business-environment-forces: qualitative: a taxonomy of outside pressures.
- fair-value-hedge: qualitative: an accounting designation and its recognition treatment,
  no formula of its own that is not the banned balance-sheet-identity pattern.
- fair-value-through-other-comprehensive-income-classification: qualitative:
  classification criteria under IFRS 9, no formula.
- financial-condition-reporting: qualitative: describes a reporting system, no formula.
- financial-derivatives: qualitative: a definitional node; pricing formulas belong to the
  sibling nodes for each specific derivative, e.g. forward-contract-pricing.
- financial-institutions: qualitative: a taxonomy of intermediary types.
- financial-statement-preparation: qualitative: the only candidate expression is the
  balance-sheet identity, the example the brief names as failing the "true of the object,
  not just the subject in general" test.
- foreign-exchange-hedging-of-dividends-and-subsidiary-net-asset-value: qualitative:
  describes which exposures are hedged, no formula of its own at this depth.
- funds-transfer-pricing-curve: qualitative: describes how a curve is built across tenors;
  the pricing formula belongs to the prerequisite node funds-transfer-pricing.
- gdp-outlook-and-credit-losses: qualitative: a macro-to-provisioning narrative, no formula
  of its own.
- general-insurance-business-environment: qualitative: a taxonomy of outside pressures on
  a general insurer.

## Concern

None. Every required node existed, and `check.py` reported zero failures across the
20 landed pages.
