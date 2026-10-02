---
id: cointegration
title: Cointegration
domains: [eco, stats]
status: drafted
requires: [integrated-time-series]
spends: []
anchor: [ifoa.cs2.2.1-8]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Two or more integrated time series are cointegrated when some linear combination of them is
itself stationary, even though each series individually carries a stochastic trend. Cointegrated
series tend to move together over the long run, which is the property that makes the
relationship worth modelling separately from either series alone.

## The expression

$$
u_t = y_t - \beta x_t, \qquad u_t \sim I(0)
$$

Here $y_t$ and $x_t$ are each integrated series, $\beta$ is the cointegrating coefficient, and
$u_t$ is the residual from subtracting $\beta x_t$ from $y_t$. The series are cointegrated
exactly where this residual is stationary, written $I(0)$, despite $y_t$ and $x_t$ themselves
being non-stationary.

## Why this node exists

Regressing one non-stationary series on another can produce a fit with a high $R^2$ and
significant coefficients even where the two series have no genuine relationship, a hazard
that motivates checking for cointegration before the regression is trusted at all. Time series applications to security prices and economic variables need it next, since a cointegrating
relationship between two prices or two economic series is exactly the long-run equilibrium a
trading or forecasting model built on that pair depends on.
