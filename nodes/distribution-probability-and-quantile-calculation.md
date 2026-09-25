---
id: distribution-probability-and-quantile-calculation
title: Probability and quantile calculation for a distribution
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.2.1-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Once a distribution's parameters are fixed, a probability is found by evaluating its
distribution function at a point, and a quantile is found by inverting that same function at a
probability.

## The expression

$$
P(X \le x) = F(x), \qquad Q(p) = F^{-1}(p)
$$

Here $X$ is the random variable, $F$ is its distribution function, $x$ is the point at which a
probability is wanted, $p$ is a probability level, and $Q(p)$ is the quantile function, the
value $x$ for which $F(x) = p$.

## Why this node exists

A named distribution is only useful once a specific probability or a specific quantile can be
pulled out of it, whether by direct calculation for a simple distribution or by numerical
inversion for a more complicated one. Every downstream question, such as the probability a loss
exceeds a threshold or the level a capital requirement should be set at, is answered by
evaluating $F$ or $F^{-1}$ at the point in question.
