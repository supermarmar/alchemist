---
id: isotonic-regression
title: Isotonic regression
domains: [stats]
status: stub
requires: []
spends: []
anchor: [eth.dl-actuarial-2026.l07]
vault_articles: []
vault_sources: []
taught_in: null
---

Isotonic regression finds the monotone step function closest to a set of observed values in squared error, with no hyperparameter to choose, which makes it the natural way to recalibrate a predictor since the recalibrated function is by construction auto-calibrated on the sample it is fitted to. Fitted on a sample too small to support its own step count, it can overfit the recalibration and cost more out of sample than the miscalibration it was meant to repair.
