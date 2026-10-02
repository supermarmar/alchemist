---
id: double-lift-chart
title: Double lift chart
domains: [credit, gi, stats]
status: drafted
requires: [lift-chart]
spends: []
anchor: [ucsc.dl-actuarial-2026.l07]
vault_articles: [concepts/balance-property-and-auto-calibration]
vault_sources: []
taught_in: null
---

## Definition

A double lift chart compares two competing models by binning observations on the ratio of their
predictions, so the bins are chosen exactly where
the two models disagree, and it plots both models' mean predictions against the mean observed
outcome within each bin.

## The expression

$$
r_i = \frac{\hat y^{(1)}_i}{\hat y^{(2)}_i}, \qquad \left(\bar{\hat y}^{(1)}_k,\ \bar{\hat y}^{(2)}_k,\ \bar y_k\right), \quad k = 1, \dots, K
$$

Here $\hat y^{(1)}_i$ and $\hat y^{(2)}_i$ are the two models' predictions for observation $i$,
$r_i$ is their ratio, the quantity observations are binned on, $K$ is the number of bins, and
$\bar{\hat y}^{(1)}_k$, $\bar{\hat y}^{(2)}_k$, and $\bar y_k$ are the mean of each model's
predictions and the mean observed outcome within bin $k$.

## Why this node exists

A lift chart built on either model's own predictions bins the data where that model draws its
own distinctions, so it can only ever show whether a model agrees with itself, and it says
nothing about the region where the two models actually differ. Binning on the ratio instead puts
every observation where the two models disagree most into the same handful of bins, and the observed outcome in each bin then shows which model was closer precisely there.
