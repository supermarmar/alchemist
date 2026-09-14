---
id: individual-conditional-expectation
title: Individual conditional expectation
domains: [ml, stats]
status: stub
requires: [feed-forward-neural-network]
spends: []
anchor: [ucsc.dl-actuarial-2026.l08]
vault_articles: [methods/icenet-smoothness-and-monotonicity-constraints]
vault_sources: []
taught_in: null
---

An individual conditional expectation curve fixes one observation's covariates, varies a single chosen covariate across a grid of values, and records the fitted model's prediction at each point, showing how that one observation's prediction responds to the chosen covariate on its own. Averaging many such curves gives a partial dependence plot, which can look monotone even where most of the individual curves underneath it are not.
