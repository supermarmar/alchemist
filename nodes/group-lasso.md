---
id: group-lasso
title: Group lasso
domains: [credit, ml, stats]
status: stub
requires: [lasso-regularisation]
spends: []
anchor: [eth.dl-actuarial-2026.l08]
vault_articles: []
vault_sources: []
taught_in: null
---

Group lasso applies an unsquared norm penalty to each predefined block of coefficients, such as every level of one categorical covariate, so an entire covariate can be driven to zero together rather than one level at a time. It reproduces the variable-reduction step of scorecard development, dropping whole risk drivers in an order determined by how much predictive weight each carries.
