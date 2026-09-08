---
id: elastic-net
title: Elastic net
domains: [credit, ml, stats]
status: stub
requires: [lasso-regularisation, ridge-regularisation]
spends: []
anchor: [ucsc.dl-actuarial-2026.l08]
vault_articles: []
vault_sources: []
taught_in: null
---

Elastic net regularisation combines the ridge and lasso penalties in a single objective, so that a group of correlated covariates is shrunk together rather than having lasso pick one member of the group arbitrarily and zero the rest. It is often the better default on data where several covariates proxy for the same underlying quantity.
