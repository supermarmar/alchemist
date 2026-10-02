---
id: integrated-time-series
title: Integrated time series
domains: [stats]
status: drafted
requires: [stationary-time-series]
spends: []
anchor: [ifoa.cs2.2.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A time series is integrated of order $d$, written $I(d)$, when it must be differenced $d$ times
before the result is stationary, so the series itself carries a stochastic trend that
differencing removes. It is degenerate at $d = 0$, where the series is already stationary and no
differencing is needed.

## The expression

$$
\Delta X_t = X_t - X_{t-1}, \qquad \Delta^d X_t \sim I(0)
$$

Here $X_t$ is the series at time $t$, $\Delta X_t$ is the first difference, and $d$ is the
number of times that differencing must be applied before the result, $\Delta^d X_t$, is a
stationary, $I(0)$, series.

## Why this node exists

A model fitted to a series without first removing its stochastic trend produces spurious
relationships between variables that share no real connection beyond drifting together, so the
order of integration has to be established before any regression on the series is trusted. ARIMA
needs it next, since fitting an ARIMA model starts by choosing the differencing order that
returns the series to stationarity.
