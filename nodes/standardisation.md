---
id: standardisation
title: Standardisation
domains: [ml, stats]
status: stub
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l06, ucsc.dl-actuarial-2026.l08]
vault_articles: []
vault_sources: []
taught_in: null
---

Standardisation rescales a covariate to mean zero and unit variance, estimating the mean and standard deviation on the training data alone, which gradient-based fitting needs because it shares one learning rate across covariates that may otherwise sit on wildly different scales. A heavy-tailed monetary covariate can still dominate a standardised design matrix, so censoring or a logarithmic transform is usually applied before scaling rather than instead of it.
