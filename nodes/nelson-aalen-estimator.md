---
id: nelson-aalen-estimator
title: Nelson-Aalen estimator
domains: [life, stats]
status: drafted
requires: [censoring, hazard-rate]
spends:
  - {object: obj.hazard, domain: life}
  - {object: obj.hazard, domain: stats}
anchor: [ifoa.cs2.4.2-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Nelson-Aalen estimator estimates the cumulative hazard directly from censored
data, accumulating the ratio of observed events to the size of the risk set at each
event time instead of estimating survival first.

## The expression

$$
\hat{\Lambda}(t) = \sum_{t_j \le t} \frac{d_j}{n_j}
$$

Here $\hat{\Lambda}(t)$ is the estimated cumulative hazard to time $t$, $t_j$ ranges
over the distinct observed event times up to $t$, $d_j$ is the number of events at
$t_j$, and $n_j$ is the number of subjects at risk immediately before $t_j$: the same
counts the Kaplan-Meier estimator multiplies, summed here instead. Each increment
$d_j / n_j$ approximates the instantaneous rate over that short interval, written
$\mu_x$ in the life table and $\lambda(t)$ in general statistical notation.

## Why this node exists

A censored sample gives no single interval over which the hazard can be read off
directly, since the risk set itself is shrinking as subjects fail or leave. Summing the
event-to-risk ratio across every observed event time recovers the cumulative hazard
regardless, and its own variance estimate is available from the same running sum,
letting the two censored-data estimators this corpus builds be checked against each
other.
