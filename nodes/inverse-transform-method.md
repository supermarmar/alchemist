---
id: inverse-transform-method
title: Inverse transform method
domains: [maths, stats]
status: drafted
requires: [continuous-uniform-distribution]
spends: []
anchor: [ifoa.cs1.2.1-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The inverse transform method generates a sample from a target distribution by applying that
distribution's inverse cumulative distribution function to a draw from the standard uniform
distribution. It is degenerate wherever the target distribution places a point mass, where the
inverse function must be defined as the smallest value at which the cumulative distribution
function reaches the drawn probability.

## The expression

$$
X = F^{-1}(U), \qquad U \sim \mathrm{Unif}(0,1)
$$

Here $U$ is a draw from the standard uniform distribution, $F^{-1}$ is the inverse of the target
distribution's cumulative distribution function, and $X$ is the resulting sample, which has
exactly the target distribution.

## Why this node exists

Simulating a distribution by this method needs nothing beyond a uniform random number generator
and a formula, or a numerical routine, for the target distribution's inverse cumulative
distribution function. Where that inverse cannot be written down or computed cheaply, an
actuary or a modeller turns instead to rejection sampling or another simulation method that
avoids inverting the distribution directly.
