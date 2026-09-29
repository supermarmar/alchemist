---
id: poisson-distribution
title: Poisson distribution
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.2.1-1, up.wst211.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Poisson distribution gives the probability of observing a given count of
independent events in a fixed interval when those events occur at a constant
average rate; it is degenerate at zero, placing all its mass there, only in the
limit as the rate parameter tends to zero.

## The expression

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \qquad k = 0, 1, 2, \dots
$$

Here $X$ is the count of events, $k$ is the particular count whose probability
is wanted, and $\lambda$ is the average rate, which equals both the mean and
the variance of the distribution.

## Why this node exists

Modelling a count over one fixed interval says nothing about how those events
unfold as the interval lengthens or is subdivided, and the Poisson process
needs this node next to describe exactly that: the same constant-rate
assumption, extended across continuous time.
