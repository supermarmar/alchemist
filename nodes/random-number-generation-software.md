---
id: random-number-generation-software
title: Random number generation using software
domains: [data-eng, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.2.1-6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Random number generation in statistical software starts from a stream of
uniform pseudo-random numbers and transforms it into draws from whatever
distribution a simulation needs, most directly through the inverse of that
distribution's own cumulative distribution function.

## The expression

$$
X = F^{-1}(U), \qquad U \sim \mathrm{Uniform}(0,1)
$$

Here $U$ is a draw from the uniform distribution on the unit interval, $F^{-1}$
is the inverse of the target distribution's cumulative distribution function,
and $X$ is the resulting draw from that target distribution.

## Why this node exists

A method that only works where the inverse of the distribution function can be
written down or approximated leaves many distributions unreachable by this
route alone. The simulated comparison against the normal distribution needs
this node next, to check empirically how such generated samples actually
behave against distributional theory.
