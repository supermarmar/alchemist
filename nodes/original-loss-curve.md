---
id: original-loss-curve
title: Original loss curve
domains: [gi]
status: drafted
requires: [frequency-severity-approach]
spends: []
anchor: [ifoa.sp8.3.5-3]
vault_articles: [methods/reinsurance-pricing]
vault_sources: []
taught_in: null
---

## Definition

An original loss curve, also called an increased limit factor curve, gives the
proportion of a fitted severity distribution's expected loss that falls within a
stated claim size, so pricing a policy limit or a reinsurance layer means reading off
the proportion the limit or the layer covers.

## The expression

$$
G(m) = \frac{E[\min(X, m)]}{E[X]}
$$

Here $X$ is the claim severity, $m$ is the claim size at which the curve is
evaluated, $E[\min(X, m)]$ is the expected loss capped at $m$, and $E[X]$ is the
uncapped expected loss, so $G(m)$ is the share of total expected loss that a limit of
$m$ retains.

## Why this node exists

Pricing a layer of loss above a retention needs the expected loss the layer actually
carries, and that figure is the difference between the curve evaluated at the top of
the layer and at its bottom, each read off this one function; without it, a limit or
a layer could only be priced from the treaty's own thin claims history.
