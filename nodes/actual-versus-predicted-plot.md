---
id: actual-versus-predicted-plot
title: Actual versus predicted plot
domains: [credit, stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l07]
vault_articles: [concepts/balance-property-and-auto-calibration]
vault_sources: []
taught_in: null
---

## Definition

An actual-versus-predicted plot bins held-out observations by their predicted value and
compares, within each bin, the average of what was predicted against the average of what
was observed, so a flexible model is judged on data it was not fitted to.

## The expression

$$
\bar{y}_k = \frac{1}{n_k} \sum_{i \in k} y_i, \qquad \bar{\hat{y}}_k = \frac{1}{n_k} \sum_{i \in k} \hat{y}_i
$$

Here $k$ indexes one bin of the out-of-sample data, $n_k$ is the number of observations it
holds, $y_i$ is the observed outcome for observation $i$, and $\hat{y}_i$ is its predicted
value. A model is well calibrated where the pairs $(\bar{\hat{y}}_k, \bar{y}_k)$ sit on the
diagonal across every bin, and it over-spreads or under-spreads a cohort wherever they do
not.

## Why this node exists

A model can rank risks correctly while still charging one cohort for another's losses, and
overall goodness-of-fit measures such as deviance cannot tell the two failures apart. The
actual-versus-predicted plot separates them by cohort, showing which failure, if either, a
fitted model has, before it is deployed against real exposures.
