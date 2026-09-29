---
id: time-series-operator-notation
title: Time series operator notation
domains: [stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs2.2.1-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The backward shift operator and the backward difference operator let a time series model be
written and manipulated algebraically, so that a model's stationarity can be read off the roots
of its characteristic equation rather than derived afresh each time.

## The expression

$$
LX_t = X_{t-1}, \qquad \nabla X_t = (1 - L)X_t = X_t - X_{t-1}
$$

Here $X_t$ is the series at time $t$, $L$ is the backward shift operator, which steps a series
back by one period, and $\nabla$ is the backward difference operator, defined as $1 - L$, whose
effect is to subtract each observation from the one before it. A model's autoregressive part
can be written as a polynomial in $L$, and the roots of that polynomial, set equal to zero,
form its characteristic equation.

## Why this node exists

Deriving a time series model's stationarity condition from first principles every time it is
written down is unworkable once the model has more than one or two lags, and this notation
turns that derivation into an algebraic check on where the characteristic equation's roots lie.
Every autoregressive and moving average model in the corpus is stated and manipulated in this
notation from here on.
