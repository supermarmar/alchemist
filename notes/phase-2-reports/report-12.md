# Batch 12 report

Status: complete. 5 of 40 nodes attached at least one article (6 attachments total); 35 uncovered.

## Attached

- **double-lift-chart** (ucsc.dl-actuarial-2026.l07) -> `concepts/balance-property-and-auto-calibration`. The article's own "Lift charts, and what they separate" section states the node's subject directly: "A double lift chart, which bins on the ratio of the two models' predictions and plots both alongside the actuals, resolves the comparison..." Same source lecture as the anchor.
- **deviance-loss** (first anchor ucsc.dl-actuarial-2026.l02) -> `methods/exponential-dispersion-family-and-glm`. Gives the deviance loss's own definition, derivation from the EDF, the Poisson/Gaussian/Bernoulli special cases, and strict consistency (Gneiting 2011). Direct hit on the first-listed anchor; second and third anchors (ifoa.cs1.4.2-6, up.wst311.7) not separately represented.
- **development-factor** (ifoa.cm2.4.2-1) -> `methods/chain-ladder-reserving`. The article's entire subject is built on the development factor: its weighted-average-of-ratios construction and Mack's assumptions on it.
- **discriminatory-power** (ucsc.dl-actuarial-2026.l02, l07) -> `methods/discrimination-metrics-auc-and-somers-d` (AUC as the Wilcoxon probability, Gini/Somers' D as the same family, rank invariance) and `methods/classifier-calibration-discrimination` (a model can rank well and be miscalibrated - the "Bull" archetype - matching the node's second claim exactly).
- **duration-and-convexity** (ifoa.cm1.1.8-1) -> `methods/alm-immunisation`. Redington's paragraph defines duration as the mean term of a payment stream and convexity as the spread of proceeds about that mean, then gives the matching conditions and why residual convexity favours the office. That is a definition plus a use. Flagged initially as too ALM-specific and reversed on review: the article gives the actuarial mean-term/spread formulation rather than the bond price-sensitivity derivative formulation, so `ifoa-cm1-core-reading-2026` stays ledgered for that second treatment.

## Two anchor errors found (direct inspection of vault/markdown/bcbs/d424.md)

- **downturn-lgd-estimation**: anchored to `bcbs.d424.irb.para-229`, which is "Requirements specific to PD estimation" (line 4140), not downturn LGD. The node's own text paraphrases paras 235 (downturn LGD, line 4203), 239 (seven-year corporate minimum, line 4356 area) and 240 (five-year retail minimum, line 4356). No wiki article treats any of these; `regulation/eba-downturn-lgd-estimation` and `methods/lgd-downturn-estimation` were considered and rejected as EU-transposition text (CRR Art. 181, EU 2021/930, EBA/GL/2019/03) rather than the Basel standard itself, per the wave's transposing-regulation guidance.
- **ead-quantification-standards**: anchored to `bcbs.d424.irb.para-241` (the bare EAD definition, line 4245), while the node's text paraphrases paras 245 (12-month fixed horizon, line 4288), 248 (must not be capped, line 4351) and 250-251 (seven/five-year minimums, line 4356-4364). `methods/ifrs9-ead-ccf-modelling` was considered and rejected: it is IFRS 9/CRR3 CCF modelling, not the Basel own-estimate EAD standard.

Both folded into the existing `bcbs-d424-irb-risk-weight-functions` ledger entry alongside `dilution-risk` (anchor `bcbs.d424.irb.para-136` verified correct against line 3455; `regulation/eba-irb-material-model-changes-rts` mentions "dilution risk" only inside a materiality-threshold list, never defining it, so rejected). The merge keeps ledger-07's note over mine, so these paragraph corrections survive only here.

## Third anchor problem: dropout

`dropout`'s anchor, `ucsc.dl-actuarial-2026.l10`, does not cover it. Checked all ten `2026_eth_deep-learning-actuarial-*` extractions for "dropout": it appears only in the bibliographies of Lectures 4-5 and 10-11 (Srivastava 2014, Wager et al. 2013), cited as background reading, never treated in any lecture body. Proposed the primary paper (`srivastava-2014-dropout`) instead of a wiki-article-scope entry, since no lecture teaches the mechanism at all.

## Other close calls rejected

- `diversifiable-and-non-diversifiable-risk`: `methods/asrf-capital-foundation` names "systematic risk factor" and "idiosyncratic risk" but only inside Gordy's single-factor regulatory-capital derivation, a narrower and different subject from the general CM2/CP1/SP9 concept. Shared vocabulary, not shared subject.
- `discounting-of-expected-credit-losses`: `concepts/ifrs9-poci-assets` covers half the node (credit-adjusted EIR for POCI, B5.5.45) substantively, but nothing covers the load-bearing first half, B5.5.44's "discounted to the reporting date, not to the expected default date." Ledgered under the existing `iasb-ifrs9-standard-cash-shortfall-and-hedge-types` id (same underlying standard, different paragraphs).
- `direct-versus-reinsurance-pricing`: `methods/reinsurance-pricing` is a rich, direct treatment of reinsurance pricing methodology alone, but never compares it against direct pricing, which is this node's actual subject.
- `direct-reinsurance-reserving`: `methods/chain-ladder-reserving` and `methods/bornhuetter-ferguson-reserving` never mention reinsurance.

## Where vault strength landed, and where it didn't

The credit-model-validation cluster (discriminatory-power, double-lift-chart) and the GLM/reserving cluster (deviance-loss, development-factor) attached cleanly on the vault's strongest ground, plus one actuarial ALM hit (duration-and-convexity). Everything else in this batch sat in pure mathematics (determinant, diagonalisability, differential calculus, direct methods for linear systems, discrete uniform distribution, distribution function, distribution/quantile calculation, descriptive statistics), general economics (determinants of economic growth, development economics), general banking/actuarial exam material (development bank/finance, discontinuance x3, distributor conduct risk, dividend-growth valuation, downside/upside risk, downside semi-variance, diversification benefit, duration-dependent Markov process, duplicate-policy test adjustment, dynamic FTP/liability benchmarks, discrete dividend option valuation, discounted cashflow pricing), or GI reinsurance mechanics never treated in the vault's reserving articles - all zero, as expected for this mix.

## Ledger documents proposed (see ledger-12.yaml for full entries)

New: `up-wst111-course-notes` (descriptive-statistics), `up-wtw114-course-notes` (differential calculus), `up-wtw383-course-notes` (direct methods for linear systems), `up-ekn120-course-notes` (development economics - note: another concurrent batch independently minted this same id for a different EKN120 chapter; the merge keeps mine since ledger-12 sorts first, non-blocking), `srivastava-2014-dropout` (dropout, primary paper).

Reused with a new note (none existed yet): `up-wtw124-course-notes` (determinant, WTW124's matrix-determinant chapter), `ifoa-sp8-core-reading-2026` (direct-versus-reinsurance-pricing, SP8 4.4).

Reused, note omitted per ledger-07's precedent (each already carries an earlier batch's note): `bcbs-d424-irb-risk-weight-functions`, `iasb-ifrs9-standard-cash-shortfall-and-hedge-types`, `dl-actuarial-2026-l04-05-fnn`, `up-wst211-course-notes`, `up-wtw221-course-notes`, `up-ias712-course-notes`, `ifoa-cs1/cs2/cm1/cm2/cb2/sp1/sp2/sp5/sp6/sp7/sp9-core-reading-2026`, `assa-f107/f207-study-material-2026`.

## check.py

`1560 nodes, 13 paths, 0 failures` - all eleven checks pass, including check 11 on all six attached slugs (concepts/balance-property-and-auto-calibration, methods/exponential-dispersion-family-and-glm, methods/chain-ladder-reserving, methods/discrimination-metrics-auc-and-somers-d, methods/classifier-calibration-discrimination, methods/alm-immunisation).

## Brief ambiguity

None found blocking. The "fold vs new id" choice for a document's further distinct subject (lesson/ledger-07 precedent) reads as the house style now, so I followed it throughout rather than minting `bcbs-d424-*` variants per paragraph cluster.
