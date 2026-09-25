---
id: stationary-time-series
title: Stationary time series
domains: [stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs2.2.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A time series is weakly stationary when its mean and its autocovariance structure do not
change with the point in time at which they are measured, so that only the lag between two
observations, not their calendar position, determines how they covary.

## The expression

$$
E[X_t] = m, \qquad \mathrm{Cov}(X_t, X_{t+h}) = \gamma(h)
$$

Here $X_t$ is the series at time $t$, $m$ is its constant mean, $h$ is the lag between two
observations, and $\gamma(h)$ is their covariance, which depends on $h$ alone and not on $t$
itself. A series meeting both conditions is written $I(0)$, since it needs no differencing to
reach stationarity.

## Why this node exists

Every standard time series result, from the autocorrelation function to the fitted model's
own confidence intervals, assumes that the process generating the data behaves the same way at
every point in the sample, and stationarity is the condition that makes that assumption
precise rather than implicit. A series failing it has a mean or a variance that drifts with
time, and integrated time series is what supplies the differencing operator that removes that
drift and returns a stationary series to work with.
