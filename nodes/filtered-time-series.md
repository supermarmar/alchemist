---
id: filtered-time-series
title: Filtered time series
domains: [stats]
status: drafted
requires: [white-noise-process]
spends: []
anchor: [ifoa.cs2.2.1-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A filtered time series is a stationary series formed by passing a white noise process
through a linear filter, so each observation is a fixed weighted sum of the current and
past white noise terms. Where every weight beyond the first is zero, the filtered series
collapses back to the white noise process itself.

## The expression

$$
X_t = \sum_{j=0}^{\infty} \psi_j\, \varepsilon_{t-j}
$$

Here $X_t$ is the filtered series at time $t$, $\varepsilon_{t-j}$ is the white noise term
$j$ periods before $t$, and $\psi_j$ is the fixed weight the filter places on that term.

## Why this node exists

Writing a series this way gives every stationary process one shared structure to be
studied through, a weighted history of pure noise, with the process's own character
reduced to the particular shape its weights $\psi_j$ take. The autoregressive process and
the moving average process both need it next, since each restricts this general filter to
one specific weight pattern, finite for the moving average and geometrically decaying for
the autoregressive case.
