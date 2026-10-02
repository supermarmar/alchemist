# Batch 22 report

Nodes written: 17. Nodes written from vault articles: 6 (effective-interest-method,
embedded-value-calculation, exponential-dispersion-family, feature-tokenisation; two others,
expected-credit-loss-governance and forms-of-interest-rate-risk, were read from vault articles
but left as stubs, tagged qualitative below). Nodes written without vault articles: 13. Nodes
not landed: 23.

## Nodes written

- determinant: stub and anchor only. Spends: none. No collision or split candidates.
- distribution-function: stub and anchor only. Spends: none. No collision or split candidates.
- dropout: stub and anchor only. Spends: none. No collision or split candidates.
- effective-interest-method: concepts/effective-interest-rate. Spends: none. No collision or
  split candidates.
- eigenvalues-and-eigenvectors: stub and anchor only. Spends: none. No collision or split
  candidates.
- embedded-value-calculation: concepts/market-consistent-embedded-value. Spends:
  obj.discount-factor:life, obj.discount-factor:actuarial. No collision candidates. The
  expression deliberately differs from the EV = ANAV + VIF identity its prerequisite,
  assumption-setting-for-embedded-value, already spends, and instead gives the VIF
  discounting sum, to avoid restating a formula the reader already holds.
- expectation-of-life: stub and anchor only. Spends: obj.survival:life. No collision or split
  candidates.
- expected-shortfall: regulation/frtb-minimum-capital-market-risk. Spends: none. No collision
  or split candidates.
- expected-value: stub and anchor only. Spends: none. No collision or split candidates.
- exponential-dispersion-family: methods/exponential-dispersion-family-and-glm. Spends:
  obj.response-mean:stats, obj.dispersion:stats. No collision or split candidates.
- feature-tokenisation: methods/credibility-transformer. Spends: none. No collision candidate;
  possible future object for a token embedding if further nodes need one, not proposed here
  since only this node currently uses it.
- field-extension: stub and anchor only. Spends: none. No collision or split candidates.
- fixed-income-valuation: stub and anchor only. Spends: obj.discount-factor:fin-eng. No
  collision or split candidates.
- forward-foreign-exchange-hedging: stub and anchor only. Spends: none. No collision or split
  candidates.
- fundamental-theorem-of-calculus: stub and anchor only. Spends: none. No collision or split
  candidates.
- gross-less-net-reserving: stub and anchor only. Spends: none. No collision candidates. The
  expression is the gross-minus-recoveries identity, distinct from chain-ladder's own
  ultimate-claims formula, which the sibling node direct-reinsurance-reserving instead reuses
  unchanged and so was left as a stub below.
- depreciation-and-reserves: stub and anchor only. Spends: none. No collision or split
  candidates.

## Not landed

- deposit-liquidity-value-factors: qualitative: lists the features that make a deposit more or
  less favourably treated (insured, retail, operational); no formula of its own, sibling
  lcr-outflow-assumptions.
- derivative-pricing-operational-considerations: qualitative: xVA family, collateral and
  booking-capacity constraints read from concepts/xva-overview; no single defining formula.
- derivative-risk-identification-and-management: qualitative: a taxonomy of which risks a
  derivative strategy carries and how each is managed; no formula of its own.
- direct-reinsurance-reserving: qualitative: applies chain-ladder's own ultimate-claims formula
  unchanged to a reinsurance triangle; sibling chain-ladder holds the formula.
- direct-versus-reinsurance-pricing: qualitative: a comparative methodology node with no
  formula of its own.
- discontinuance-terms-methods: qualitative: surveys methods against principles set by its
  prerequisite; no formula of its own.
- downturn-lgd-estimation: qualitative: a governance and observation-period requirement (BCBS
  d424 para 235), not a computed formula.
- economic-growth-unemployment-and-inflation: qualitative: an overview of three headline
  indicators explained through the aggregate demand and supply framework already drafted in
  its prerequisite; no formula of its own.
- eligible-credit-rating-agency-criteria: qualitative: eligibility criteria for a credit
  assessment institution (objectivity, independence, transparency, market credibility); no
  formula.
- empirical-characteristics-of-asset-prices: qualitative: stylised facts of asset price series
  (fat tails, volatility clustering); no single defining formula.
- enterprise-risk-management-framework: qualitative: a governance framework topic.
- example-lcr-calculation: qualitative: the LCR ratio formula belongs to the sibling node
  liquidity-coverage-ratio (already drafted); this node is a worked numeric example of it.
- example-outflow-assumptions: qualitative: worked run-off percentages per liability category;
  sibling lcr-outflow-assumptions.
- exchange-rate-intervention: qualitative: policy discussion of intervention and its
  constraints; no formula.
- expected-credit-loss-governance: qualitative: read regulation/eba-gl-ecl-credit-risk-
  management in full; governance arrangements around ECL judgements, no formula.
- exploratory-data-analysis: qualitative: a survey of summary and visualisation tools; no
  single defining formula.
- fair-value-through-profit-or-loss-classification: qualitative: read regulation/ifrs9-
  financial-instruments; a residual classification test (fails amortised cost and FVOCI
  criteria), not a computed formula.
- financial-statement-interpretation: qualitative: a family of ratios and summary measures
  rather than one object with a single defining formula.
- fixed-versus-floating-exchange-rates: qualitative: a comparative policy topic; no formula.
- forms-of-interest-rate-risk: qualitative: read regulation/eba-gl-2022-14-irrbb-csrbb; a
  taxonomy of repricing, yield curve, basis and optionality risk, not a formula.
- general-insurance-regulatory-framework: qualitative: a regulatory framework overview topic.
- group-and-insurance-company-accounts: qualitative: extends statement preparation to group and
  insurer-specific reporting requirements; no single formula.
- guarantee-and-option-risk: qualitative: the risk that a guarantee or option costs more than
  its charge; a qualitative risk topic, not a computed formula.
