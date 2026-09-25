---
id: white-noise-process
title: White noise process
domains: [stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs2.2.1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A white noise process is a stationary sequence of random variables that share a
common mean and variance and are uncorrelated with each other at every non-zero
lag.

## The expression

$$
E[\epsilon_t] = 0, \qquad \mathrm{Var}(\epsilon_t) = \sigma^2, \qquad \mathrm{Cov}(\epsilon_t,\epsilon_s) = 0 \ (t \neq s)
$$

Here $\epsilon_t$ is the process at time $t$, $\sigma^2$ is its constant variance,
and the zero-covariance condition states that no two terms of the series carry any
linear relationship to each other.

## Why this node exists

A forecaster needs a benchmark for structure that carries no information at all,
and white noise is that benchmark: a model is judged adequate once its residuals
look like this and nothing more can be extracted from them. Random walk needs it
next, since a random walk is nothing but the cumulative sum of a white noise
process.
