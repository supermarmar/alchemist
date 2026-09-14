---
id: partial-dependence-plot
title: Partial dependence plot
domains: [ml, stats]
status: stub
requires: [individual-conditional-expectation]
spends: []
anchor: [ucsc.dl-actuarial-2026.l08]
vault_articles: [methods/icenet-smoothness-and-monotonicity-constraints]
vault_sources: []
taught_in: null
---

A partial dependence plot is the average of individual conditional expectation curves across every observation in a sample, showing how a fitted model's prediction responds on average to one covariate. Averaging can hide substantial disagreement among the underlying curves, so a plot that is monotone on average can sit above a majority of curves that individually rise and fall.
