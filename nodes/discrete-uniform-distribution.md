---
id: discrete-uniform-distribution
title: Discrete uniform distribution
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

The discrete uniform distribution places equal probability on every value in a finite,
evenly spaced set. It degenerates to certainty on a single value wherever that set has only
one member.

## The expression

$$
P(X = x) = \frac{1}{n}, \qquad x \in \{a, a+1, \ldots, b\}
$$

Here $X$ is the random variable, $x$ is one of the values it can take, $a$ and $b$ are the
lower and upper bounds of the set, and $n = b - a + 1$ is the number of equally likely values
between them.

## Why this node exists

Every other discrete distribution assigns unequal probability to at least some of its outcomes,
and the discrete uniform is the reference point that difference is measured against: it is the
distribution a fair die or a random draw from a finite list already follows, with no further
assumption needed.
