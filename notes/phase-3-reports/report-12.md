# Phase 3 batch 12 report

Nodes written: 21
Nodes written from articles: 1 (basel-i-credit-risk-quantification)
Nodes written without: 20 (from stub, anchor and standard knowledge of the subject)
Nodes not landed: 19

## Nodes written

### value-at-risk-capital-assessment
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### vector-space-rn
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### volatility-estimation-from-market-data
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### white-noise-process
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### yield-curves
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### accumulated-value
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### actual-versus-expected-analysis
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### age-period-cohort-mortality-model
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### annuity-function
Sources read: stub and anchor only.
Spends: obj.survival:life.
Collision candidates: obj.discount-factor (canonical v) has actuarial and fin-eng
aliases but no life alias, though life annuity valuation uses the same v. The page
is written without declaring it rather than spending it under a domain the node
does not carry.
Split candidates: none.

### asian-and-lookback-option
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none. Two display blocks used, one per option type named in the
title; each is a single payoff formula, so the page stays as one node.

### asset-return-relationships
Sources read: stub and anchor only.
Spends: obj.asset-correlation:stats.
Collision candidates: none. obj.asset-correlation's own definition is scoped to
"latent asset returns of two obligors" (the Vasicek single-factor credit setting);
this page reuses it for the correlation between two asset-class return series
under its stats alias rho, which is the same statistical object in a broader
application rather than a distinct one.
Split candidates: none.

### assurance-function
Sources read: stub and anchor only.
Spends: obj.survival:life.
Collision candidates: q_{x+k}, the one-year mortality probability, has no matching
object; obj.lifetime-cdf is a cumulative probability of death by time t, not a
one-year rate, so it was left undeclared rather than spent under a mismatched
definition.
Split candidates: none.

### autoencoder
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### available-capital
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### average-cost-per-claim-method
Sources read: stub and anchor only.
Spends: obj.ultimate:gi, obj.cohort-index:gi.
Collision candidates: none.
Split candidates: none.

### bank-balance-sheet
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### bank-income-statement
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### barrier-option
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### basel-i-credit-risk-quantification
Sources read: entities/basel-accord-evolution.
Spends: none.
Collision candidates: none. obj.exposure's credit alias is EAD_i, a Basel II IRB
concept; Basel I's flat risk-weight scheme does not use a modelled exposure at
default, so the page keeps a plain E_i and spends nothing.
Split candidates: none.

### basic-indicator-approach
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

### basis-risk-in-hedging
Sources read: stub and anchor only.
Spends: none.
Collision candidates: none.
Split candidates: none.

## Not landed

- wholesale-funded-bank: qualitative: describes a bank's funding profile; no formula defines or measures the type.
- wholesale-market-funding: qualitative: describes a funding channel; no formula in the standard treatment.
- write-off: qualitative: an accounting derecognition event under IFRS 9, defined by criteria rather than a formula.
- 2008-financial-crisis-and-recovery: qualitative: a historical narrative topic with no formula.
- abstract-vector-space: qualitative: defined by a set of axioms an operation must satisfy, not by a single measuring formula.
- actuarial-model-construction: qualitative: a governance and process topic (objectives, data, operational issues).
- actuarial-model-uses: qualitative: a list of the decisions a model supports, with no formula of its own.
- adapting-to-risk-environment-change: qualitative: a process topic on revising risk management practice.
- advertising-and-demand: qualitative: describes a demand-curve shift and its drivers; the standard IFoA CB2 treatment is conceptual rather than formulaic here.
- aggregate-demand-and-supply: qualitative: the AS-AD framework is graphical equilibrium analysis, not a single defining equation for the item as taught.
- american-option-pricing-methods: qualitative: a comparison of several pricing methods (lattice, finite difference, Longstaff-Schwartz), with no single object formula of its own.
- amortised-cost-classification: qualitative: a classification test (business model plus SPPI) under IFRS 9, defined by criteria rather than a formula.
- artificial-intelligence-model-governance: qualitative: a governance topic extending model risk oversight to AI models.
- assumption-setting: qualitative: a process topic on gathering and validating data for assumptions.
- bank-credit-and-liquidity-risk-channels: qualitative: a list of channels through which risk is taken on, with no formula.
- bank-strategic-plan-lifecycle: qualitative: a process and lifecycle topic.
- basel-ii-shortcomings: qualitative: a list of structural and procyclicality weaknesses exposed by the 2007-08 crisis.
- basel-iii-2017-implementation-timeline: qualitative: a timeline of implementation dates, not a formula.
- basel-iii-liquidity-framework-overview: qualitative: an overview of the LCR and NSFR, whose own formulae belong to their own prerequisite nodes rather than to this overview.

## Vault articles read

entities/basel-accord-evolution.md, regulation/ifrs9-financial-instruments.md,
regulation/eba-machine-learning-irb.md, regulation/pra-ss1-23-model-risk-management.md,
methods/credit-risk-procyclicality.md, regulation/bcbs-liquidity-risk-framework.md.
The last five inform the qualitative reasoning above for amortised-cost-classification,
artificial-intelligence-model-governance, basel-ii-shortcomings and
basel-iii-liquidity-framework-overview but produced no written page since each of those
nodes is qualitative.
