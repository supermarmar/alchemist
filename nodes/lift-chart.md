---
id: lift-chart
title: Lift chart
domains: [credit, gi, stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l07]
vault_articles: [concepts/balance-property-and-auto-calibration]
vault_sources: []
taught_in: null
---

## Definition

A lift chart bins observations by predicted value and plots the average
prediction and the average actual outcome within each bin against the bin's
position, letting the reader read calibration, monotonicity, and discrimination
off the same picture.

## The expression

$$
\left(\bar{\hat{y}}_k,\ \bar{y}_k\right), \qquad k = 1, \dots, K
$$

Here $K$ is the number of bins the observations are partitioned into by predicted
value, $\bar{\hat{y}}_k$ is the mean prediction within bin $k$, and $\bar{y}_k$ is
the mean observed outcome within the same bin. Predictions and actuals
coinciding across bins indicates calibration, actuals rising with $k$ indicates
correct risk ranking, and the spread between the lowest and highest bin measures
discrimination.

## Why this node exists

A single loss statistic can improve while a model's pricing becomes less fair
across cohorts, and the lift chart is what exposes that split by showing
calibration and discrimination as two separate readings. The double lift chart
needs it next, since it re-bins the same comparison on the ratio of two models'
predictions to decide between them where their single lift charts disagree.
