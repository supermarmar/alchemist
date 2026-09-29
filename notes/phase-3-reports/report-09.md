# Batch 09 report

Nodes written: 20
Nodes written from articles: 5
Nodes written without: 15
Nodes not landed: 20

## Nodes written

### parameter-risk
Left as stub; see Not landed.

### pareto-distribution
Sources read: stub and anchor only.
Spends declared: none.

### partial-least-squares
Sources read: stub and anchor only.
Spends declared: none.

### passive-and-active-valuation-approaches
Left as stub; see Not landed.

### pca
Sources read: methods/ols-predictor-importance (background on PCA's variance-only criterion and its risk of sign conflict with a target; not otherwise usable since the article covers PCA as an IFRS 9 dimensionality-reduction technique rather than the general method).
Spends declared: none.

### pension-fund-de-risking
Left as stub; see Not landed.

### pension-fund-interest-rate-and-inflation-hedging
Sources read: stub and anchor only.
Spends declared: none.

### pension-obligation-risk
Left as stub; see Not landed.

### persistency-risk
Sources read: stub and anchor only.
Spends declared: none.

### physical-risk
Left as stub; see Not landed.

### pillar-1-minimum-capital-requirements
Sources read: entities/basel-accord-evolution (Basel I's 8% minimum ratio and flat risk-weight architecture), regulation/eu-crr-2013-capital-requirements-regulation (Article 92's 4.5%/6%/8% split).
Spends declared: none.

### poisson-distribution
Sources read: stub and anchor only.
Spends declared: none.

### policy-data-risk
Left as stub; see Not landed.

### policy-data-validation
Left as stub; see Not landed.

### political-risk
Left as stub; see Not landed.

### population-heterogeneity-and-selection
Left as stub; see Not landed.

### portfolio-risk-return-analysis
Sources read: stub and anchor only.
Spends declared: none.

### post-event-impact-management
Left as stub; see Not landed.

### premium-structure
Sources read: stub and anchor only.
Spends declared: none.

### prepayment-risk
Sources read: stub and anchor only.
Spends declared: none.

### pricing-data
Left as stub; see Not landed.

### pricing-risk-and-uncertainty
Left as stub; see Not landed.

### private-medical-insurance
Left as stub; see Not landed.

### probability-theory-foundations
Sources read: stub and anchor only.
Spends declared: none.

### product-credit-risk-measurement
Sources read: methods/ifrs9-portfolio-segmentation (grouping exposures by shared credit risk characteristics, the regulatory rationale for product/segment-level rather than borrower-level parameters).
Spends declared: none.

### product-design-factors
Left as stub; see Not landed.

### production-and-cost-theory
Sources read: stub and anchor only.
Spends declared: none.

### project-risk
Left as stub; see Not landed.

### property-derivative
Sources read: stub and anchor only.
Spends declared: none.

### property-markets
Left as stub; see Not landed.

### propositional-logic
Left as stub; see Not landed.

### proprietary-trading-activities
Left as stub; see Not landed.

### providers-of-financial-products
Left as stub; see Not landed.

### qualitative-credit-analysis
Left as stub; see Not landed.

### radon-nikodym-derivative
Sources read: stub and anchor only.
Spends declared: none.

### random-number-generation-software
Sources read: stub and anchor only.
Spends declared: none.

### random-sample
Sources read: stub and anchor only.
Spends declared: none.

### real-number-properties
Sources read: stub and anchor only.
Spends declared: none.

### recurrent-neural-network
Sources read: stub and anchor only.
Spends declared: none.

### reduced-form-credit-model
Sources read: methods/structural-credit-risk-models (the structural/reduced-form contrast, used to state what the reduced-form approach deliberately does not model).
Spends declared: obj.hazard:credit, obj.survival:credit.

## Not landed

- parameter-risk: qualitative: the standard treatment (estimation-error risk in a correctly specified model) is a risk concept with no defining formula of its own; the vault article on stochastic claims reserving discusses parameter risk only as a named component of reserve uncertainty, not as an object with a formula.
- passive-and-active-valuation-approaches: qualitative: contrasts two valuation philosophies (fixed basis versus market-consistent revaluation) with no formula distinguishing them.
- pension-fund-de-risking: qualitative: a governance and asset-allocation strategy (reducing growth-asset holdings as funding improves), not a measured object.
- pension-obligation-risk: qualitative: a risk-transmission concept (scheme deficit becoming a call on bank capital) with no standard formula.
- physical-risk: qualitative: an operational-risk category (damage to premises, systems, or people) with no defining formula.
- policy-data-risk: qualitative: a data-quality risk concept; the vault article on risk data aggregation and reporting states governance principles, not a formula.
- policy-data-validation: qualitative: a data-quality process (completeness and accuracy checks before use); the vault article on data quality dimensions gives named checks, not a formula.
- political-risk: qualitative: a risk category defined by its source (government action, unrest), with no standard measure.
- population-heterogeneity-and-selection: qualitative: an actuarial practice concept explaining why classes need separate mortality tables; no single formula is the standard treatment at this syllabus item's depth.
- post-event-impact-management: qualitative: a process (managing impact after an event has occurred, e.g. remediation), not a measured object.
- pricing-data: qualitative: a data-governance topic (sources and quality of pricing data), with no defining formula.
- pricing-risk-and-uncertainty: qualitative: a survey of risk sources in general insurance pricing, with no single formula.
- private-medical-insurance: qualitative: a product description, with no defining formula.
- product-design-factors: qualitative: a list of factors shaping product design, with no formula.
- project-risk: qualitative: a risk category (project failure to deliver), with no standard measure.
- property-markets: qualitative: covers direct and indirect property investment and market features, with no single defining formula.
- propositional-logic: qualitative: the syllabus item covers connectives, truth tables, and valid argument as a system rather than a single object; no one formula defines "propositional logic" itself.
- proprietary-trading-activities: qualitative: a definitional distinction (trading for own account versus on behalf of customers), with no formula.
- providers-of-financial-products: qualitative: a survey of provider types (insurers, pension schemes, banks, the state), with no defining formula.
- qualitative-credit-analysis: qualitative: by definition covers non-financial-statement factors (management quality, industry position), with no formula.

## Concerns

None. No collision candidates and no split candidates arose in this batch: every
written node held to one display block, and no symbol on a written page matched
an `objects.yaml` entry outside the credit hazard/survival pair spent on
reduced-form-credit-model.

## Check result

.venv/bin/python scripts/check.py: "1560 nodes, 13 paths, 0 failures"
