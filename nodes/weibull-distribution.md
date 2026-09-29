---
id: weibull-distribution
title: Weibull distribution
domains: [maths, stats]
status: drafted
requires: [exponential-distribution]
spends:
  - {object: obj.hazard, domain: stats}
  - {object: obj.survival, domain: stats}
anchor: [up.wst211.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A Weibull-distributed duration has a hazard rate that varies as a power of elapsed time
rather than staying constant, and it degenerates to the exponential distribution exactly
when that power is one.

## The expression

$$
S(t) = \exp\!\left[-\left(\frac{t}{\theta}\right)^{k}\right], \qquad
h(t) = \frac{k}{\theta}\left(\frac{t}{\theta}\right)^{k-1}
$$

Here $S(t)$ is the survival function, $h(t)$ is the hazard rate at $t$, $\theta$ is the
scale parameter, and $k$ is the shape parameter that governs how the hazard moves with
time: $k \gt 1$ gives a hazard that rises with age, $k \lt 1$ gives one that falls, and
$k = 1$ recovers the exponential's constant hazard.

## Why this node exists

The exponential distribution's constant hazard cannot represent a component that wears
out or a borrower whose default risk peaks partway through a loan's life, and the
Weibull's shape parameter is what lets the same family of distributions fit a hazard that
rises, falls or stays flat without changing which distribution is being fitted.
