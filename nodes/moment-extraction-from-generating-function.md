---
id: moment-extraction-from-generating-function
title: Moment extraction from a generating function
domains: [maths, stats]
status: drafted
requires: [moment-generating-function]
spends: []
anchor: [ifoa.cs1.2.4-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Moment extraction from a generating function recovers a distribution's moments by
differentiating the moment generating function repeatedly and evaluating each derivative at
the origin, turning a single expression into the whole sequence of moments it encodes.

## The expression

$$
E[X^k] = M_X^{(k)}(0)
$$

Here $X$ is the random variable, $M_X$ is its moment generating function, $M_X^{(k)}$ is the
$k$th derivative of $M_X$ with respect to $t$, and $E[X^k]$ is the $k$th moment of $X$. Taking
$k=1$ recovers the mean and $k=2$ the second moment, from which the variance follows as
$E[X^2] - (E[X])^2$.

## Why this node exists

A moment generating function is only useful once its moments can actually be pulled back out
of it, and differentiating at the origin is the mechanical operation that does that: the
generating function is defined precisely so this operation works term by term on its power
series expansion. Without this extraction step, naming $M_X$ would fix a distribution's shape
without supplying any of the summary quantities, mean, variance, skewness, that a model
actually reports.
