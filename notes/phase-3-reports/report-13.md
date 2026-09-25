# Batch 13 report

nodes written: 29
nodes written from articles: 7
nodes written without: 22
nodes not landed: 11

## Nodes

### binomial-distribution
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "confidence interval for a binomial probability and a Poisson mean" (confidence-interval-binomial-poisson).

### bayesian-prior-and-posterior
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlocks named "Bayesian point estimation" and "Credible interval" in prose.

### behavioural-tenor-modelling
Sources: concepts/eve-and-nii.
Spends: none (w_i, t_i not in objects.yaml).
Collision candidates: none.
Other: no unlocks; ends on the consequence of a mispriced facility.

### binary-classifier-evaluation-metrics
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: two-block ceiling reached (precision and recall in one display); ROC/AUC is a genuine split candidate for a second page.

### binomial-and-poisson-exposure-models
Sources: stub and anchor only.
Spends: obj.hazard:life, obj.lifetime-cdf:life.
Collision candidates: none.
Other: no unlocks; ends on the consequence for graduation.

### binomial-option-pricing-model
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "risk-neutral pricing measure".

### binomial-representation-theorem
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence rather than naming martingale-representation-theorem, which does not require this node.

### bond-credit-analysis
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence.

### bootstrap-method
Sources: methods/statistical-power-analysis.
Spends: none.
Collision candidates: none.
Other: unlock named is "Bootstrap confidence interval".

### brace-gatarek-musiela-model
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Calibrating the Brace-Gatarek-Musiela model with Black's model".

### burning-cost-approach
Sources: methods/reinsurance-pricing.
Spends: none.
Collision candidates: none.
Other: unlock named is "Non-proportional reinsurance pricing".

### capital-allocation
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Capital performance metrics".

### capital-project-appraisal
Sources: stub and anchor only.
Spends: obj.discount-factor:actuarial.
Collision candidates: none.
Other: unlock named is "Risky investment evaluation".

### capital-structure-and-cost-of-capital
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks (cost-of-capital does not require this node); ends on the consequence. Kept MM Proposition II here and WACC on cost-of-capital to avoid duplicating a formula across the two nodes.

### capital-target-setting
Sources: regulation/pra-icaap-and-pillar-2.
Spends: none.
Collision candidates: none.
Other: unlock named is "Capital management strategy".

### cash-flow-hedge
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence, referencing the prerequisite hedge-accounting by name (not a forward reference).

### cauchy-riemann-equations
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Cauchy's integral theorem".

### chain-ladder
Sources: methods/chain-ladder-reserving.
Spends: obj.development-factor:gi, obj.ultimate:gi, obj.cohort-index:gi, obj.development-index:gi.
Collision candidates: none.
Other: unlock named is "Bornhuetter-Ferguson method". Factor estimator itself left to development-factor.

### change-of-measure
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence. Used Girsanov's drift-shift form per the anchor (SP6 3.3-6), leaving the density itself to radon-nikodym-derivative.

### chooser-and-binary-option
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: two-block ceiling reached (chooser value, binary payoff); a split into two separate nodes is a genuine candidate.

### collateralised-debt-obligation
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence.

### commodities
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence.

### compound-poisson-distribution
Sources: stub and anchor only.
Spends: obj.hazard:gi (bare lambda as the Poisson claim-count parameter, treated as the gi claim intensity).
Collision candidates: none, but flagged as a close call: this lambda is a period claim-count parameter rather than a per-unit-time hazard rate, and a future gi-domain node using both concepts on one page should watch for the same ambiguity obj.hazard's ml alias note already documents.
Other: unlock named is "Moments of compound claim distributions".

### consumer-utility-maximisation
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Behavioural economics".

### cost-of-capital
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Capital structure and dividend policy" (chosen over "Embedded value calculation" as the closer fit). WACC kept here, MM Proposition II kept on capital-structure-and-cost-of-capital.

### counterparty-credit-risk
Sources: regulation/counterparty-credit-risk-saccr.
Spends: obj.exposure:credit.
Collision candidates: none.
Other: unlock named is "Potential future exposure".

### credit-approval-cutoffs
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence (break-even odds).

### credit-concentration-risk
Sources: methods/credit-risk-concentration-bcbs.
Spends: none.
Collision candidates: none.
Other: unlock named is "Risk concentration".

### credit-default-swap-bond-spread-relationship
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence.

## Not landed

- benefit-payment-risk-factors: qualitative: a list of risk factors affecting benefit payments (level, timing, security), no formula the standard treatment attaches to the object.
- business-application-of-economic-concepts: qualitative: a survey of how firms apply opportunity cost and marginal analysis, no single defining formula.
- business-cycle: qualitative: the boom-recession pattern itself has no defining formula of its own; the output gap that measures deviation from potential is already owned by actual-versus-potential-growth.
- capital-and-provisioning-influence-on-pricing: qualitative: describes how provisioning and capital requirements feed into pricing and financing strategy, no single formula for that influence.
- central-bank: qualitative: an institutional description of a central bank's roles, no defining formula.
- challenger-bank: qualitative: an institutional description of a market entrant, no defining formula.
- contingent-event-products-and-benefits: qualitative: a taxonomy of benefit types and providers, no formula.
- contract-design: qualitative: the trade-offs between premium, benefit and charge design, no single formula the standard treatment gives for "contract design" itself.
- corporate-funds-transfer-pricing-regime: qualitative: the corporate-specific adaptation of funds transfer pricing; the FTP formula itself belongs to the prerequisite funds-transfer-pricing.
- corporate-governance-structure-factors: qualitative: the factors (size, complexity, ownership) shaping governance structure, no formula.
- cost-management-for-providers: qualitative: how a provider controls and manages payment and expense costs, no single defining formula.
