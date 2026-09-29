# Batch 04 report

Nodes written: 10
Nodes written from articles: 2
Nodes written without: 8
Nodes not landed: 30

## Nodes written

### demand-and-supply-analysis
- Sources read: stub and anchor only
- Spends: none
- No collision or split candidates

### descriptive-statistics
- Sources read: stub and anchor only
- Spends: none
- No collision or split candidates

### development-factor
- Sources read: methods/chain-ladder-reserving
- Spends: obj.development-factor:gi
- No collision or split candidates. The per-cohort cumulative loss $C_{i,j}$ in the
  expression is not an object in `objects.yaml` and is not spent.

### discounted-cashflow-model-pricing
- Sources read: stub and anchor only
- Spends: obj.discount-factor:fin-eng
- No collision or split candidates. `objects.yaml`'s fin-eng alias for
  obj.discount-factor is used ($v$) rather than a bare discount rate, since the
  object exists in that spelling.

### discrete-uniform-distribution
- Sources read: stub and anchor only
- Spends: none
- No collision or split candidates

### discriminatory-power
- Sources read: methods/discrimination-metrics-auc-and-somers-d,
  methods/classifier-calibration-discrimination
- Spends: none
- No collision candidate raised despite AUC, $D_{xy}$ and the Gini coefficient
  being genuinely cross-domain notation, because `objects.yaml` holds no object
  for any of the three; recorded here as a candidate worth adding
  (proposed id `obj.discrimination`, canonical $D_{xy}$, credit and stats both
  writing $\mathrm{AUC}$ or $D_{xy}$ depending on convention).

### distribution-probability-and-quantile-calculation
- Sources read: stub and anchor only
- Spends: none
- No collision or split candidates. $F$ and $Q$ are generic and not tied to any
  object in `objects.yaml`.

### diversifiable-and-non-diversifiable-risk
- Sources read: stub and anchor only
- Spends: obj.coefficients:stats
- No split candidates. Collision candidate: $\beta_i$ here is a single-index
  market-model slope (asset beta), spent against obj.coefficients, whose
  existing aliases are a GLM's or a scorecard's coefficient vector; the two
  senses share one symbol and one object id but are conceptually distinct
  (a market sensitivity versus a fitted regression vector), worth a second
  object (proposed id `obj.market-beta`) if a future node needs to
  distinguish them.

### downside-semi-variance
- Sources read: stub and anchor only
- Spends: none
- No collision or split candidates

### efficient-markets-hypothesis
- Sources read: stub and anchor only
- Spends: none
- No collision or split candidates

## Not landed

- data-analysis-aims: qualitative: distinguishes descriptive, inferential and predictive aims; no formula.
- data-analysis-lifecycle: qualitative: a sequence of process stages, no formula.
- data-governance-and-ethics: qualitative: governance and ethical obligations, no formula.
- data-leakage: qualitative: a procedural failure mode defined by which rows an estimation step saw, no formula.
- data-protection-regulation-banking: qualitative: a legal regime (GDPR, POPI), no formula.
- data-provenance-and-scale: qualitative: describes origin and scale constraints, no formula.
- data-requirements-for-valuation: qualitative: describes fitness-for-purpose criteria, no formula.
- data-sources-and-characteristics: qualitative: a survey of data sources and their traits, no formula.
- data-visualisation: qualitative: a graphical method, no formula of its own.
- data-wrangling: qualitative: a data transformation process, no formula.
- database-driven-statistical-modelling: qualitative: describes database design and modelling workflow, no formula.
- defining-liquidity: qualitative: a definitional concept (ability to meet cash obligations), no formula.
- definition-of-default: qualitative: confirmed against both vault articles; the definition rests on the 90-day past-due and unlikeliness-to-pay triggers, not a formula.
- demographic-risk: qualitative: names a risk source (mortality, longevity, lapse experience), no formula of its own.
- deposit-insurance-regulation: qualitative: describes a guarantee scheme, no formula.
- deposit-taking: qualitative: describes a funding activity, no formula.
- derivative-hedging-in-banks: qualitative: describes a hedging use case, no single standard hedge formula named in the anchor's scope.
- derivative-investor-objectives: qualitative: a list of investor objectives judged qualitatively against cash-market alternatives, no formula.
- derivatives-market-characteristics: qualitative: describes market features (standardisation, leverage, margin), no formula.
- development-bank: qualitative: describes an institutional purpose, no formula.
- development-economics: qualitative: a field survey with South Africa as a running example, no formula.
- development-finance: qualitative: describes construction and development lending risk qualitatively, no formula.
- discontinuance: qualitative: describes lapse and surrender behaviour and its allowance, no single formula named as the standard treatment at this anchor.
- distributor-conduct-risk: qualitative: describes a conduct risk source, no formula.
- downside-and-upside-risk: qualitative: distinguishes two qualitative directions of outcome, no formula.
- early-warning-indicators: qualitative: confirmed against the vault article; the standard treatment is a list of indicators and supervisory observations, not a formula.
- economic-history-since-the-great-depression: qualitative: a historical survey, no formula.
- economic-influences-on-investment-markets: qualitative: a survey of qualitative drivers, no formula.
- economic-risk: qualitative: describes a risk source (growth, inflation, unemployment), no formula.
- economics-of-government: qualitative: a field survey of public spending, taxation and regulation, no formula.
