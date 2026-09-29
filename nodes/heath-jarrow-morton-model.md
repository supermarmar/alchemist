---
id: heath-jarrow-morton-model
title: Heath-Jarrow-Morton model
domains: [fin-eng, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.3.7-8]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Heath-Jarrow-Morton model specifies the evolution of the entire instantaneous
forward rate curve directly, rather than modelling a single short rate and
deriving the rest of the curve from it. Under this framework, the drift of every
forward rate is fixed by the no-arbitrage condition and cannot be chosen
independently of its volatility.

## The expression

$$
df(t,T) = \alpha(t,T)\,dt + \sigma(t,T)\,dW(t), \qquad
\alpha(t,T) = \sigma(t,T) \int_t^T \sigma(t,s)\,ds
$$

Here $f(t,T)$ is the instantaneous forward rate at time $t$ for maturity $T$,
$\sigma(t,T)$ is its volatility, $W(t)$ is a Brownian motion under the
risk-neutral measure, and $\alpha(t,T)$ is the drift the no-arbitrage condition
forces once the volatility is chosen.

## Why this node exists

A model of the whole curve at once needs infinitely many correlated volatility
functions to specify, which is impractical to calibrate directly against market
instruments quoted on discrete forward rates. The Brace-Gatarek-Musiela model
needs it next, since it restates the same no-arbitrage drift condition in terms
of the discrete forward rates that are actually traded.
