# Phase 3 batch 20 report

Nodes written: 21. Nodes written from vault articles: 3 (vintage-analysis,
additional-national-capital-requirements, basel-i-minimum-capital-requirements). Also drew on a
vault article without it changing the formula chosen: bayesian-credibility-theory (from
methods/credibility-theory, supplying the Z = n/(n+k) form and Jewell's exact result).
Nodes written without vault articles: 17. Nodes not landed: 19, all tagged qualitative below.

## Nodes written

- topological-properties-of-euclidean-space: stub and anchor only. Spends: none. Unlock named:
  Continuous function properties.
- two-state-credit-rating-model: stub and anchor only. Spends: obj.survival:credit,
  obj.hazard:credit. No unlocks; ended on consequence.
- unit-linked-contract: stub and anchor only. Spends: none. Unlock named: Accumulating
  with-profits contract.
- value-at-risk: stub and anchor only. Spends: none (wrote the general quantile definition;
  did not invoke the normal quantile, so no collision with obj.normal-quantile's fin-eng gap).
  Unlock named: Weaknesses of value at risk.
- vector-algebra-lines-and-planes: stub and anchor only. Spends: none. Unlock named: Vector
  functions and quadratic curves.
- vintage-analysis: methods/breeden-2016-lifecycle-environment-loan-level-forecasts. Spends:
  obj.cohort-index:credit, obj.development-index:credit. No unlocks; ended on consequence.
- warrant: stub and anchor only. Spends: none. No unlocks; ended on consequence.
- weibull-distribution: stub and anchor only. Spends: obj.hazard:stats, obj.survival:stats.
  Used scale symbol $\theta$ and shape $k$ rather than the conventional $\lambda$, to avoid
  colliding with obj.hazard's stats alias $\lambda(t)$; not raised as a collision candidate
  since the page resolves it by choosing a non-colliding symbol. No unlocks; ended on
  consequence.
- actuarial-investigation: stub and anchor only. Spends: none. No unlocks; ended on consequence.
- additional-national-capital-requirements: regulation/pillar-2a-capital-framework,
  regulation/pra-capital-buffers-ccyb-srb. Spends: none. No unlocks; ended on consequence.
- adjustment-coefficient: stub and anchor only. Spends: obj.hazard:gi. Unlock named: Optimising
  the adjustment coefficient under reinsurance.
- aggregate-expenditure-model: stub and anchor only. Spends: none. Unlock named: Keynesian
  multiplier.
- asset-share: stub and anchor only. Spends: none. Unlock named: With-profits surplus
  distribution.
- attention-mechanism: stub and anchor only. Spends: none. Unlock named: Multi-head attention.
- autoregressive-process: stub and anchor only. Spends: none (obj.coefficients is a regression
  object, semantically distinct from an AR process's own coefficients, so not spent; used
  $\phi$, which does not collide with obj.dispersion's $\varphi$). Unlock named:
  Autoregressive moving average process.
- backpropagation: stub and anchor only. Spends: none. No unlocks; ended on consequence.
- bank-financial-ratio-analysis: stub and anchor only. Spends: none. No unlocks; ended on
  consequence.
- basel-i-minimum-capital-requirements: entities/basel-accord-evolution. Spends: none. Unlock
  named: Shortcomings of the Basel Accord.
- basel-iii-tier-1-and-tier-2-redefinition: stub and anchor only (tier-1-capital and
  tier-2-capital, its prerequisites, stayed stubs this batch; wrote from the standard Basel
  III treatment). Spends: none. Unlock named: Basel III revised minimum capital requirements.
- bayesian-credibility-theory: methods/credibility-theory. Spends: obj.credibility-weight:actuarial.
  Unlock named: Bayes versus empirical Bayes credibility.
- bayesian-point-estimation: stub and anchor only. Spends: none. No unlocks (used a
  standalone example sentence instead).

## Collision and split candidates

None beyond the two symbol choices noted above (weibull-distribution, autoregressive-process),
both resolved on the page rather than flagged as objects.yaml candidates.

## Capital-cluster and with-profits-cluster allocation

Read tier-1-capital, tier-2-capital, why-banks-hold-capital, bank-capital-treatment,
basel-i-minimum-capital-requirements, basel-iii-tier-1-and-tier-2-redefinition and
additional-national-capital-requirements side by side before writing any of them. The capital
ratio (capital / RWA >= 8%) was given to basel-i-minimum-capital-requirements alone, since
that is the node whose own object the ratio defines; the CET1 + AT1 = T1 split was given to
basel-iii-tier-1-and-tier-2-redefinition; the buffer-stacking sum was given to
additional-national-capital-requirements. tier-1-capital, tier-2-capital, why-banks-hold-capital
and bank-capital-treatment were left qualitative rather than reusing any of those three
formulas.

Read with-profits-contract, accumulating-with-profits-contract and asset-share side by side.
The recursive accumulation formula was given to asset-share alone, since its stub explicitly
names the recursion as its own object; with-profits-contract and accumulating-with-profits-contract
were left qualitative, both naming asset-share as the sibling that owns the formula.

## Not landed

- technology-risk: qualitative: a governance and operational-risk topic (systems failure
  exposure) with no formula that is its own object.
- tier-1-capital: qualitative: instrument-eligibility criteria (permanence, non-cumulative
  distributions, subordination), not a formula; the composition formula belongs to the
  sibling basel-iii-tier-1-and-tier-2-redefinition.
- tier-2-capital: qualitative: instrument-eligibility criteria (five-year minimum maturity, no
  step-ups), not a formula; sibling as above.
- trade-protectionism: qualitative: a policy topic (tariffs, quotas) with no formula of its
  own; welfare-loss diagrams belong to a general trade-theory node outside this batch.
- transition-management: qualitative: an asset-management practice topic, no formula.
- treating-customers-fairly: qualitative: a conduct-regulation principle, no formula.
- underwriting-approaches: qualitative: a taxonomy of underwriting practices, no formula.
- universal-bank: qualitative: a business-model description, no formula.
- venture-capital: qualitative: an asset-class description, no formula.
- wholesale-funds-transfer-pricing-regime: qualitative: a funding-practice topic, no formula
  of its own; any pricing formula belongs to the prerequisite funds-transfer-pricing node
  outside this batch.
- why-banks-hold-capital: qualitative: a business-model topic; a balance-sheet identity would
  be the exact failure the brief warns against, so none was written.
- with-profits-contract: qualitative: sibling asset-share owns the recursive formula.
- accumulating-with-profits-contract: qualitative: sibling asset-share owns the recursive
  formula.
- actuarial-model-applications: qualitative: a list of purposes (pricing, capital, reserving,
  option valuation), no single formula.
- advisory-services-pricing: qualitative: a fee-structure description, no formula precise
  enough to be the standard treatment.
- bank-board-governance: qualitative: a governance-responsibilities topic, no formula.
- bank-capital-treatment: qualitative: an instrument-ranking overview; the composition formula
  belongs to the sibling basel-iii-tier-1-and-tier-2-redefinition.
- bank-exposure-risk-weights-ecra: qualitative: a risk-weight lookup table keyed to external
  rating, not a formula; the RWA = RW x EAD formula belongs to the prerequisite
  standardised-approach-credit-risk node outside this batch.
- behavioural-economics: qualitative: relaxes classical rationality assumptions; no single
  formula is the standard treatment at this survey level.
