---
id: order-statistic
title: Order statistic
domains: [stats]
status: drafted
requires: [random-variable]
spends: []
anchor: [up.wst211.19]
vault_articles: [methods/eba-pd-backtesting-methodology]
vault_sources: []
taught_in: null
---

## Definition

The $k$th order statistic of a sample is the $k$th smallest of its values once the
sample is arranged in increasing order, and its own distribution can be derived from
the distribution of the underlying random variable the sample was drawn from.

## The expression

$$
F_{(k)}(x) = \sum_{j=k}^{n} \binom{n}{j} \bigl[F(x)\bigr]^j \bigl[1 - F(x)\bigr]^{n-j}
$$

Here $F$ is the distribution function of the underlying random variable, $n$ is the
sample size, $k$ is the rank of the order statistic, and $F_{(k)}$ is the
distribution function of the $k$th order statistic, the probability that at least $k$
of the $n$ sample values fall at or below $x$.

## Why this node exists

A model validated only on its average behaviour can still be badly wrong at its
extremes, and a backtest that wants to know how unusual the worst or second-worst
observed default rate in a run of years really is needs the distribution of that
extreme value, not the distribution of a typical one, which is exactly what an order
statistic supplies.
