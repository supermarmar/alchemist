---
id: grouped-binomial-regression
title: Grouped binomial regression
domains: [stats]
status: stub
requires: [glm]
spends: []
anchor: [ucsc.dl-actuarial-2026.l02]
vault_articles: []
vault_sources: []
taught_in: null
---

Fitting a Bernoulli generalised linear model on one row per observation and fitting it on one row per covariate cell, using the cell's event rate as the response and its observation count as a weight, are the same maximum likelihood problem and return identical coefficient estimates. The equivalence lets a model be fitted on aggregated cohort tables where individual-level records no longer exist.
