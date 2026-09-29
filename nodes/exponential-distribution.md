---
id: exponential-distribution
title: Exponential distribution
domains: [maths, stats]
status: drafted
requires: []
spends:
  - {object: obj.survival, domain: stats}
anchor: [ifoa.cs1.2.1-2, up.wst211.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The exponential distribution is the continuous distribution of the waiting time to a single
event occurring at a constant rate. It is the only continuous distribution with the memoryless
property, that the distribution of remaining waiting time does not depend on how long has already
elapsed.

## The expression

$$
f(x) = \lambda e^{-\lambda x}, \qquad S(x) = e^{-\lambda x}, \qquad x \ge 0
$$

Here $\lambda$ is the constant rate at which the event occurs, $f$ is the density of the waiting
time $x$, and $S$ is the survival function, the probability the event has not yet occurred by
$x$. The rate $\lambda$ is also the distribution's hazard, constant in $x$, which is the algebraic
signature of memorylessness.

## Why this node exists

A constant hazard is the simplest case a survival model can specify, and treating it as a special
case rather than the general rule is what stops an analyst from assuming memorylessness where the
data does not support it. The gamma distribution needs this node next, since it is built by
summing independent exponential waiting times.
