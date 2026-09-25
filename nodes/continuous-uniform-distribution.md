---
id: continuous-uniform-distribution
title: Continuous uniform distribution
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.2.1-2, up.wst211.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The continuous uniform distribution places equal probability density on every point of
a bounded interval, so no value in the interval is more likely than another; it is
degenerate wherever the interval collapses to a single point.

## The expression

$$
f(x) = \frac{1}{b-a}, \qquad a \le x \le b
$$

Here $f$ is the probability density function, and $a$ and $b$ are the lower and upper
bounds of the interval on which the distribution is supported, with the density equal
to zero outside it.

## Why this node exists

Simulating any other continuous distribution by inversion starts from a variate drawn
uniformly on the unit interval, so a method that needs a distribution's inverse
cumulative distribution function needs this one first to supply the raw randomness it
transforms. The inverse transform method needs it next.
