---
id: moment
title: Moment
domains: [stats]
status: drafted
requires: [random-variable]
spends: []
anchor: [up.wst111.10, up.wst211.8]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The $k$th moment of a random variable about the origin is the expectation of that
variable raised to the power $k$. The $k$th central moment is the expectation of the
same power applied to the variable's deviation from its mean, and the second central
moment is the variance.

## The expression

$$
\mu_k' = E[X^k], \qquad \mu_k = E\bigl[(X - \mu)^k\bigr]
$$

Here $X$ is the random variable, $E[\cdot]$ is the expectation operator, $\mu = E[X]$
is the mean, $\mu_k'$ is the $k$th moment about the origin, and $\mu_k$ is the $k$th
central moment.

## Why this node exists

A distribution's moments summarise its shape without carrying the whole density
forward, and an estimator built only from sample averages of powers needs no
likelihood to maximise. Method of moments estimation needs it next, matching a
sample's moments against their distributional counterparts to recover a parameter.
