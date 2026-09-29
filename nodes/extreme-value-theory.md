---
id: extreme-value-theory
title: Extreme value theory
domains: [stats]
status: drafted
requires: [low-frequency-high-severity-events]
spends: []
anchor: [ifoa.sp9.4.6, up.ias721.14]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Extreme value theory studies the limiting distribution of the maximum of a large sample,
which under mild conditions on the underlying distribution converges to one of a single
family regardless of what that underlying distribution is. The shape parameter of that
family degenerates to the thin-tailed Gumbel case in the limit as it tends to zero.

## The expression

$$
H_\xi(x) = \exp\left\{ -\left(1 + \xi \frac{x - \mu}{\sigma}\right)^{-1/\xi} \right\}
$$

Here $H_\xi$ is the generalised extreme value distribution function, $\xi$ is the shape
parameter that governs how heavy the tail is, and $\mu$ and $\sigma$ are the location and
scale parameters, with the expression defined wherever $1 + \xi(x-\mu)/\sigma$ is positive.

## Why this node exists

A distribution fitted to the bulk of the data, a normal or a lognormal chosen to match the
body, is under no obligation to fit the tail well, and a low-probability, high-severity
loss sits precisely where that mismatch bites hardest. Extreme value theory supplies a
family derived from the extremes themselves, so a tail estimate rests on a limiting result
that holds regardless of which body distribution the practitioner started from.
