# Batch 24 report

nodes written: 25
nodes written from articles: 8
nodes written without: 17
nodes not landed: 15

## Nodes

### mean-value-theorem
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence for bounding a function's change from its derivative.

### moment
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Method of moments estimation" (method-of-moments-estimation); "multivariate-distribution" is the other unlock but not named in prose.

### money-supply-effect-on-output-and-prices
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence for separating a growth effect from an inflation effect.

### monopoly
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Barriers to entry and contestability" (barriers-to-entry-and-contestability); "competition-policy" and "monopolistic-competition" are also unlocks but not named.

### mortality-graduation
Sources: methods/mortality-modelling.
Spends: none (chi-squared test statistic symbols not in objects.yaml).
Collision candidates: none.
Other: no unlocks; ends on the consequence for defending a smoothed table against having erased a genuine trend.

### moving-average-process
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Autoregressive moving average process" (autoregressive-moving-average-process).

### multivariable-calculus-and-directional-derivatives
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Lagrange multipliers" (lagrange-multipliers); "multiple-integrals-and-coordinate-systems" is also an unlock but not named.

### nagging
Sources: methods/entity-embedding-and-network-ensembling.
Spends: none (y-hat with superscript member index not in objects.yaml as spelled; obj.response-mean's ml alias is a plain y-hat, not an ensemble-indexed one, so not spent here).
Collision candidates: none.
Other: no unlocks; ends on the consequence, the variance-only caveat the vault article states explicitly.

### negative-binomial-distribution
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence, extending the geometric distribution's single-success case.

### non-proportional-reinsurance-pricing
Sources: methods/reinsurance-pricing.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence, the experience-rating half of the burning-cost/exposure-rating pairing the vault article describes.

### numerical-optimisation-introduction
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence. First draft tripped the "rather than" cap at 2 occurrences and was rewritten to 0 before landing.

### off-balance-sheet-credit-conversion-factors
Sources: regulation/eba-off-balance-sheet-ccf-standardised.
Spends: obj.exposure:credit, obj.exposure:regulation.
Collision candidates: none.
Other: unlock named is "Leverage ratio off-balance sheet exposure measurement" (leverage-ratio-off-balance-sheet-exposure-measurement).

### options-hedging
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence, the asymmetry a protective put gives over a forward hedge.

### order-statistic
Sources: methods/eba-pd-backtesting-methodology.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence, motivated by the order-statistics backtest the vault article describes.

### ordinary-differential-equations-and-ivps
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Laplace transform" (laplace-transform); "matrix-exponential-and-linear-systems" is also an unlock but not named.

### original-loss-curve
Sources: methods/reinsurance-pricing.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence for pricing a layer without a curve.

### orthogonality
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Diagonalisability of symmetric matrices" (diagonalisability-of-symmetric-matrices).

### perfect-competition
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Market failure" (market-failure); "monopolistic-competition" is also an unlock but not named.

### polynomial-ring-and-factorisation
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence for classifying roots algebraically.

### posterior-derivation-conjugate-cases
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence for resolving Bayes' theorem to a closed form.

### potential-future-exposure
Sources: regulation/counterparty-credit-risk-saccr.
Spends: none (PFE, N, a not in objects.yaml; obj.exposure's EAD_i spelling belongs to the SA-CCR aggregate mentioned in prose, not to this page's own display block).
Collision candidates: none.
Other: no unlocks; ends on the consequence, tying the add-on to the SA-CCR EAD = alpha(RC + PFE) relationship paraphrased from the vault article.

### power-series-and-convergence
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: unlock named is "Fourier analysis and series" (fourier-analysis-and-series); "laurent-series" is also an unlock but not named.

### premium-and-reserve-calculation
Sources: stub and anchor only.
Spends: obj.discount-factor:life.
Collision candidates: none.
Other: unlock named is "Pricing and reserving principles" (pricing-and-reserving-principles); "profit-test" is also an unlock but not named. Two display blocks used (equivalence premium and reserve recursion); considered a split candidate but the two are one identity applied twice, so kept as one page.

### present-value
Sources: stub and anchor only.
Spends: obj.discount-factor:actuarial.
Collision candidates: none.
Other: unlock named is "Cashflow valuation" (cashflow-valuation); "real-interest-rate" is also an unlock but not named.

### price-elasticity-of-deposits
Sources: stub and anchor only.
Spends: none.
Collision candidates: none.
Other: no unlocks; ends on the consequence for the funding-cost/funding-volume trade-off.

## Not landed

- monetary-transmission-to-business-activity: qualitative: the transmission mechanism is a sequence of narrative steps (rate to borrowing cost to spending), with no single defining or measuring formula in the standard treatment.
- mortality-risk: qualitative: the node describes a risk source (deviation of experience from pricing or reserving assumptions), not an object with its own defining formula.
- net-interest-income-over-cycle: qualitative: describes how several drivers move together over the cycle; no single formula measures the node's own object.
- net-interest-margin-limitations: qualitative: the defining ratio belongs to the sibling "Net interest margin and net interest spread" (net-interest-margin-and-spread); this node is a discussion of that ratio's uses and blind spots.
- non-unit-reserves: uncertain: the standard treatment projects non-unit cashflows recursively rather than stating one closed-form reserve formula, and I could not state that recursion confidently as the standard treatment states it without the CS2/SP2 course material.
- normal-versus-observed-distributions: qualitative: a comparative discussion of tail and skew behaviour against a normal or lognormal benchmark; no single formula defines or measures the comparison itself.
- nsfr-compliance: qualitative: the ratio itself belongs to the sibling "NSFR calculation" (nsfr-calculation); this node covers the balance sheet actions taken to raise it.
- nth-to-default-credit-derivative-treatment: uncertain: the Basel capital treatment for a first-to-default or nth-to-default basket is a multi-step allocation rule rather than one formula, and no vault article covers it; I could not state it confidently as the standard treatment states it.
- oligopoly: qualitative: a reaction-function formula (Cournot best response) belongs to the sibling "Game theory and oligopoly strategy" (game-theory-and-oligopoly-strategy); this node is the general market-structure description.
- operational-risk-events: qualitative: a definitional node (the basic unit an operational risk loss database records); no defining formula.
- operational-risk-key-risk-indicators: qualitative: describes a category of monitoring metric, not one metric with a single formula.
- pension-obligation-risk-quantification: qualitative: the standard treatment measures sensitivity via asset and liability duration matching, which belongs most naturally to the sibling "Impact of pension risk on available capital" (pension-risk-impact-on-bank-capital).
- pillar-2-additional-capital-requirement: qualitative: Pillar 2 add-ons are supervisor-specific judgements with no universal formula, confirmed against entities/basel-accord-evolution and methods/credit-risk-concentration-bcbs, neither of which gives one.
- portfolio-management: qualitative: covers construction and monitoring technique generally; the Markowitz mean-variance formula belongs to the sibling "Asset return relationships" (asset-return-relationships), already a prerequisite rather than an unlock of this node.
- pricing-and-financing-strategies: qualitative: covers pricing and new-business strain financing choices generally; no single defining formula for the node's own object.
