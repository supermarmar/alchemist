---
id: beta-distribution
title: Beta distribution
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.2.1-2, up.wst221.6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The beta distribution is the continuous distribution on the unit interval whose two shape parameters let its density range from uniform through to sharply skewed towards zero or one. It reduces to the uniform distribution on $(0,1)$ when both parameters equal one.

## The expression

$$
f(x) = \frac{x^{\alpha - 1}(1-x)^{\beta - 1}}{B(\alpha, \beta)}, \qquad 0 \lt x \lt 1
$$

Here $f(x)$ is the density at $x$, $\alpha$ and $\beta$ are the two shape parameters, and $B(\alpha, \beta)$ is the beta function, the normalising constant that makes the density integrate to one over the unit interval.

## Why this node exists

A proportion or a probability is bounded between zero and one, so any prior placed on it needs a distribution supported on the same interval. Without this node, a Bayesian update on a Bernoulli success probability would have no conjugate prior living on the interval the probability itself occupies.
