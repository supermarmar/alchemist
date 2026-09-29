---
id: moving-average-process
title: Moving average process
domains: [stats]
status: drafted
requires: [filtered-time-series]
spends: []
anchor: [ifoa.cs2.2.1-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A moving average process of order $q$ writes each observation as a fixed mean plus a
weighted sum of the current and the $q$ most recent white noise terms. It is
stationary for any choice of weights, because it is already a finite filter applied
to a stationary input.

## The expression

$$
X_t = \mu + \varepsilon_t + \sum_{i=1}^{q} \theta_i \varepsilon_{t-i}
$$

Here $X_t$ is the process at time $t$, $\mu$ is its constant mean, $\varepsilon_t$ is
white noise at time $t$, and $\theta_i$ is the weight on the noise term $i$ periods
in the past.

## Why this node exists

An autoregressive process explains persistence through the series' own past values,
and a moving average process explains it through a short memory of past shocks
instead, so a model that only allows the first cannot describe a series whose
correlations vanish sharply after a fixed number of lags. Autoregressive moving
average process needs it next, combining the two mechanisms into one model.
