---
id: mortality-graduation
title: Mortality graduation
domains: [life, stats]
status: drafted
requires: [lifetime-distribution-estimation]
spends: []
anchor: [up.ias382.6, up.ias382.7]
vault_articles: [methods/mortality-modelling]
vault_sources: []
taught_in: null
---

## Definition

Mortality graduation smooths a set of crude, experience-based mortality rates into a
table suitable for pricing and reserving, then tests statistically whether the
smoothed table remains an adequate fit to the experience it was drawn from.

## The expression

$$
\chi^2 = \sum_{x} \frac{(\theta_x - \theta_x^g)^2}{\theta_x^g (1 - \theta_x^g)} E_x
$$

Here $\theta_x$ is the crude mortality rate observed at age $x$, $\theta_x^g$ is the
graduated rate at the same age, and $E_x$ is the central exposure at age $x$; the
statistic sums the squared, exposure-weighted deviation of the crude rates from the
graduated table across every age and is compared against a chi-squared distribution
to test the fit.

## Why this node exists

A crude rate estimated from a thin cohort of deaths is too noisy to price or reserve
against directly, and graduation is what trades that noise for a smooth,
statistically tested table a pricing or reserving basis can rest on. Without the
test, smoothing would have no defence against having erased a genuine trend along
with the sampling noise.
