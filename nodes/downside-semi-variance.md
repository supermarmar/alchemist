---
id: downside-semi-variance
title: Downside semi-variance
domains: [fin-eng, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cm2.2.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Downside semi-variance measures the dispersion of returns that fall short of a target level,
treating every observation at or above that target as contributing no risk at all.

## The expression

$$
SV = \frac{1}{n}\sum_{i=1}^n \min(0, x_i - \tau)^2
$$

Here $SV$ is the downside semi-variance, $x_i$ is the $i$-th of $n$ observed returns, and
$\tau$ is the target return below which a shortfall is penalised.

## Why this node exists

Ordinary variance penalises a return above the target exactly as heavily as one below it, which
misrepresents an investor who welcomes the upside and fears only the downside. Comparing
investment risk measures needs this asymmetric measure next, so that a symmetric and an
asymmetric view of the same return series can be set side by side.
