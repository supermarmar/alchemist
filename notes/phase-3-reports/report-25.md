# Batch 25 report

Nodes written: 12. Written from articles: 3. Written without articles: 9. Nodes not landed: 28.

## Written

- probability-of-default: sources read: regulation/irb-pd-estimation (read in full; the page's own formula is the general PD = E[Y|X=x] the node's requires already point to, since the article's content, long-run average default rates and the margin of conservatism, belongs to the calibration nodes downstream, not to this one). Spends: obj.response-mean:stats. Collision candidate: obj.pd, credit/regulation write PD, stats would write p(x) or pi(x); objects.yaml has no entry for it.
- proportional-reinsurance-pricing: sources read: concepts/reinsurance. Spends: none.
- put-call-parity: sources read: stub and anchor only. Spends: none.
- retail-exposure-classification-and-risk-weights: sources read: regulation/eba-retail-diversification (0.2% granularity threshold taken directly from it). Spends: obj.exposure:credit, obj.exposure:regulation.
- ridge-regularisation: sources read: stub and anchor only. Spends: obj.coefficients:ml, obj.coefficients:stats, obj.regularisation:ml, obj.regularisation:stats.
- riemann-integral: sources read: stub and anchor only. Spends: none.
- risk-measure-utility-relationship: sources read: stub and anchor only. Spends: none.
- self-financing-portfolio-strategy: sources read: stub and anchor only. Spends: none.
- sequences-of-functions: sources read: stub and anchor only. Spends: none.
- shutdown-point: sources read: stub and anchor only. Spends: none.
- stochastic-process: sources read: stub and anchor only. Spends: none.
- risky-investment-evaluation: sources read: stub and anchor only. Spends: none.

## Not landed

- pricing-in-practice: qualitative: no defining formula for the node's own object; the factors are market structure and demand, covered by market-structure-and-firm-behaviour.
- profit-and-loss-account-importance: qualitative: the P&L formula belongs to bank-income-statement, already drafted; this node is about why the bottom line matters, not a further calculation.
- rate-setting: qualitative: the practical factors that move a rate off its technical price have no formula of their own; rating-methodology owns the pricing process this sits inside.
- rating-basis-selection: qualitative: a list of considerations (retention, reinsurance, expenses, capital), no formula; sibling of rating-methodology.
- real-estate-exposure-general-requirements: qualitative: the LTV-banded risk-weight formula belongs to residential-real-estate-exposure-risk-weights and commercial-real-estate-exposure-risk-weights; this node states eligibility conditions only.
- reconstruction-discrimination-gap: qualitative: the reconstruction loss and eigenvector formulas belong to autoencoder and pca; no separate formula measures the gap itself in the standard treatment.
- regulatory-influence-on-provisioning-and-capital: qualitative: a policy-influence topic; regulatory-versus-economic-capital is the sibling with the capital-adequacy content.
- reinsurance-programme-choice: qualitative: a list of considerations (cost, counterparty strength, retention appetite), no formula; sibling of reinsurance-structure-appropriateness.
- relative-performance-measurement: qualitative: the tracking-error formula already belongs to tracking-error and relative-performance-risk.
- reserving-basis: qualitative: a judgement topic (assumptions, granularity, inflation and discounting treatment), no formula of its own.
- reserving-triangle-distortion: qualitative: a judgement topic about adjusting for distortion; the development-factor formula belongs to chain-ladder.
- retail-and-commercial-bank-products: qualitative: a product list, no formula.
- retail-loan-pricing: qualitative: the pricing formula belongs to risk-based-pricing; this node is about applying a standard rate structure to a homogeneous population.
- revised-standardised-approach-credit-risk: qualitative: the RWA = weight x exposure formula belongs to standardised-approach-credit-risk (and basel-i-credit-risk-quantification for the general form); this node covers the revised weight tables, not a new formula.
- risk-concentration: qualitative: the HHI formula already belongs to credit-concentration-risk.
- risk-governance-roles-and-responsibilities: qualitative: a governance and roles topic (board, senior management, three lines of defence), no formula.
- risk-measurement: qualitative: the frequency x severity expected-loss formula belongs to frequency-severity-approach; this node is the general step from classification to quantification.
- risk-neutral-pricing-measure: qualitative: the discounted-expectation formula already belongs to risk-neutral-pricing; this node's own content, existence and uniqueness of the measure, has no formula the standard treatment states.
- selected-risk-analysis: qualitative: applies the ERM process to named risk categories in turn; risk-classification is the sibling with the classification content, no formula here.
- short-term-liquidity-ratios: qualitative: the ratio structure already belongs to liquidity-coverage-ratio; this node applies the same numerator-denominator logic at shorter, non-regulatory horizons.
- solvency-projection: qualitative: a projection process over a business plan; available-capital and capital-requirement-by-risk-type hold the ratio's own formulas.
- sovereign-exposure-risk-weights: qualitative: a rating-to-weight lookup table, no formula of its own; the general RWA formula belongs to standardised-approach-credit-risk.
- standard-risk-weight-for-other-assets: qualitative: a flat 100% weight with named exceptions, no formula.
- standardised-approach-counterparty-credit-risk: qualitative: the EAD = alpha(RC + PFE) formula already belongs to counterparty-credit-risk.
- standardised-approach-operational-risk-2023: qualitative: the Business Indicator Component and Internal Loss Multiplier formulas belong to their own dedicated sibling nodes; this node is the overview replacing the earlier menu of approaches.
- state-health-care-funding-approaches: qualitative: a mechanisms topic (taxation, social insurance, mixed funding), no formula.
- statistical-reserving-model: qualitative: the GLM formula reproducing the chain ladder belongs to over-dispersed-poisson-model; this node's own stub describes the same model class.
- stochastic-reserving: qualitative: an overview of the method family; the specific formulas belong to mack-model, over-dispersed-poisson-model and bootstrap-reserving.
