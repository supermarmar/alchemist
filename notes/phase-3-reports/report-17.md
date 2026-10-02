# Batch 17 report

Nodes written: 17. Nodes written from articles: 4. Nodes written without: 13. Nodes not
landed: 23.

## Nodes

### lee-carter-model
Sources: methods/mortality-modelling.
Spends: none.
No collision or split candidates.

### leverage-ratio-exposure-measure-scope
Not landed: qualitative. Scope-of-consolidation rule, no formula of its own; the leverage
ratio (sibling, prerequisite) carries the ratio LR = T1/E.

### leverage-ratio-minimum-requirement
Sources: stub and anchor only.
Spends: none.
No collision or split candidates.

### lgd-foundation-approach-unsecured-claims
Sources: regulation/eba-credit-insurance-unfunded-protection.
Spends: none.
No collision or split candidates.

### life-table-probabilities
Sources: stub and anchor only (requires: life-table, drafted, read for l_x/d_x notation).
Spends: obj.survival:life, obj.lifetime-cdf:life.
No collision or split candidates.

### lifetime-consistency-condition
Sources: stub and anchor only.
Spends: obj.survival:life.
No collision or split candidates.

### lifetime-distribution-estimation
Not landed: qualitative. The specific estimators (Kaplan-Meier, exposed-to-risk, central
exposed-to-risk) are owned by sibling nodes under survival-model; this node is the umbrella
concept with no formula of its own.

### linear-regression
Sources: stub and anchor only.
Spends: obj.coefficients:stats, obj.response-mean:stats.
No collision or split candidates.

### linear-transformation
Sources: stub and anchor only.
Spends: none.
No collision or split candidates.

### liquidity-risk-beyond-lcr
Not landed: qualitative. Sources of liquidity risk the LCR does not capture; descriptive, no
formula of its own. The liquidity coverage ratio (prerequisite) carries the LCR formula.

### liquidity-risk-limit-framework
Not landed: qualitative. A catalogue of limit types, no formula.

### lloyds-market
Not landed: qualitative. Market structure and oversight, no formula.

### loan-underwriting-criteria
Not landed: qualitative. Policy criteria, no formula.

### lognormal-distribution
Sources: stub and anchor only.
Spends: none.
No collision or split candidates.

### low-interest-rate-strategic-impact
Not landed: qualitative. Strategic consequences of margin compression, no formula. Net interest
margin (prerequisite) carries the NIM formula.

### macroeconomic-policy-instruments
Not landed: qualitative. A classification of policy types, no formula.

### market-implied-survival-curve
Sources: stub and anchor only (requires: survival-model-credit-risk, drafted, read for the
F(t)=1-S(t) framing).
Spends: obj.hazard:credit.
Collision candidate: recovery rate has no object in objects.yaml; credit-default-swap and this
page both write it as $\delta$ to avoid the canonical credit symbol R, which obj.asset-correlation
already claims for that domain (R = asset correlation, per the Basel formula's own notation).
Proposed: obj.recovery-rate, credit alias $\delta$ or $R^{\text{rec}}$, fin-eng alias $\delta$.

### market-structure-and-firm-behaviour
Not landed: qualitative. MC = MR holds for every firm regardless of market structure, so it
fails the "true of the subject in general" test; the node itself is the classification, not a
formula.

### matrix-algebra-and-linear-systems
Sources: stub and anchor only.
Spends: none.
No collision or split candidates.

### minority-interest-treatment
Not landed: uncertain. The EU CRR own-funds article states the proportionality-cap principle
(qualifying minority interest is included only in proportion to the subsidiary's contribution
to the consolidated capital requirement) but gives no worked formula for Article 84's surplus
calculation, and I cannot state the exact CRR form confidently enough to present it as the
standard treatment.

### model-adaptation
Not landed: qualitative. The adaptation ladder (in-context learning, PEFT, full fine-tuning) is
descriptive; LoRA's own low-rank decomposition formula, where one exists in the corpus, belongs
to a fine-tuning-specific node, not this one.

### model-inventory
Not landed: qualitative. A register's required contents, no formula.

### model-lifecycle
Not landed: qualitative. Process stages, no formula.

### model-risk-appetite
Not landed: qualitative. Tolerance and escalation policy, no formula.

### moment-extraction-from-generating-function
Sources: stub and anchor only.
Spends: none.
No collision or split candidates.

### monetary-policy
Not landed: qualitative. Describes how policy is conducted by the Bank of England and the ECB;
no formula belongs to this item (a Taylor rule would be a different, narrower node).

### money-multiplier
Sources: stub and anchor only.
Spends: none.
No collision or split candidates.

### mortality-and-morbidity-variation-factors
Not landed: qualitative. A catalogue of variation drivers (regional, social, economic), no
formula.

### mortality-convergence
Not landed: qualitative. Describes a tendency (smoker/non-smoker convergence with age); no
standard-treatment formula found.

### mortality-forecast-error-sources
Not landed: qualitative. Model, parameter and trend risk are named categories in the CMI and
Dowd et al. literature (read via methods/mortality-modelling), not a single decomposition
formula; inventing a variance split would not be the standard treatment.

### multi-asset-and-quanto-option
Sources: stub and anchor only.
Spends: none.
Split candidate: the node bundles three distinct payoff structures (exchange, basket, quanto);
consider splitting into an exchange/basket node and a quanto node if the graph later wants each
examined separately.

### national-banking-regulation
Not landed: qualitative. Describes an added layer of national rules on top of supra-national
standards, no formula.

### net-interest-margin-and-spread
Sources: stub and anchor only (requires: net-interest-margin, drafted, read for the NIM
formula and to distinguish spread from it).
Spends: none.
Note: this node's title covers both NIM and spread; the NIM formula itself already sits on the
prerequisite page, so this page's own expression is the spread only, to avoid restating a
formula the prerequisite owns.

### net-investment-hedge
Not landed: qualitative. IFRS 9 defines the relationship and its qualifying conditions; the
effectiveness-ratio formula it shares with the other two hedge types belongs to hedge
accounting (prerequisite, drafted).

### non-economic-influences-on-investment-supply-and-demand
Not landed: qualitative. A catalogue of non-economic drivers (sentiment, taxation, regulation),
no formula.

### nsfr-calculation
Sources: methods/mortality-modelling not applicable; regulation/bcbs-liquidity-nsfr-monitoring-tools
(requires: net-stable-funding-ratio, drafted, read for the ASF/RSF ratio it already states).
Spends: none.
Note: this page's expression is the item-level weighted-sum construction of ASF and RSF, kept
distinct from the ratio itself, which the prerequisite page already carries.

### nth-to-default-basket
Sources: methods/default-correlation-copula-models.
Spends: none.
Collision candidate: recovery rate again written as $\delta_{(n)}$ rather than $R$, for the
same reason as market-implied-survival-curve; correlation is also this node's subject matter,
which makes avoiding the credit-domain $R$ collision especially important here.

### numerical-error-and-convergence
Sources: stub and anchor only.
Spends: none.
No collision or split candidates.

### obligor-group-entity
Not landed: qualitative. Grouping rules for connected legal entities under the large exposures
framework; descriptive, no formula in SS3/25 (only a landing-page summary is held in the
vault).

### operational-risk-internal-models
Not landed: qualitative. The vault's own operational-risk-capital-approaches article confirms
the Advanced Measurement Approaches were withdrawn and replaced by the standardised formula;
this node is the benefits-and-limitations discussion of the withdrawn approach, and the
replacement formula (ORC = BIC x ILM) belongs to operational-risk-capital-assessment
(prerequisite, drafted).

## Not landed

- leverage-ratio-exposure-measure-scope: qualitative: scope-of-consolidation rule, no formula
- lifetime-distribution-estimation: qualitative: umbrella concept; estimators owned by sibling nodes
- liquidity-risk-beyond-lcr: qualitative: catalogue of uncaptured liquidity risks
- liquidity-risk-limit-framework: qualitative: catalogue of limit types
- lloyds-market: qualitative: market structure and oversight
- loan-underwriting-criteria: qualitative: policy criteria
- low-interest-rate-strategic-impact: qualitative: strategic consequences, no formula
- macroeconomic-policy-instruments: qualitative: classification of policy types
- market-structure-and-firm-behaviour: qualitative: MC = MR is true in general, fails the test
- minority-interest-treatment: uncertain: CRR Art 84 surplus formula not confidently stated from sources
- model-adaptation: qualitative: adaptation ladder is descriptive
- model-inventory: qualitative: register contents
- model-lifecycle: qualitative: process stages
- model-risk-appetite: qualitative: tolerance and escalation policy
- monetary-policy: qualitative: describes conduct of policy, no formula belongs here
- mortality-and-morbidity-variation-factors: qualitative: catalogue of variation drivers
- mortality-convergence: qualitative: describes a tendency, no standard formula
- mortality-forecast-error-sources: qualitative: named error categories, not a single formula
- national-banking-regulation: qualitative: added layer of national rules
- net-investment-hedge: qualitative: qualifying conditions; formula belongs to hedge accounting
- non-economic-influences-on-investment-supply-and-demand: qualitative: catalogue of drivers
- obligor-group-entity: qualitative: grouping rules, no formula
- operational-risk-internal-models: qualitative: benefits/limitations of a withdrawn approach

