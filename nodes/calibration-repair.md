---
id: calibration-repair
title: Calibration repair
domains: [credit, regulation]
status: stub
requires: [balance-property, isotonic-regression]
spends: []
anchor: [eth.dl-actuarial-2026.l07]
vault_articles: []
vault_sources: []
taught_in: null
---

Two repairs sit in a hierarchy after a model is fitted, an intercept shift that restores the balance property exactly in one parameter, and an isotonic recalibration that restores auto-calibration at the cost of estimating one step height per cohort. Neither can correct a ranking error, since both are monotone in the original score, and any production recalibration needs a floor and a cap, since an unconstrained isotonic fit can assign a probability of exactly zero.
