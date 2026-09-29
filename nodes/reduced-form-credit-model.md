---
id: reduced-form-credit-model
title: Reduced-form credit model
domains: [credit, stats]
status: drafted
requires: []
spends:
  - {object: obj.hazard, domain: credit}
  - {object: obj.survival, domain: credit}
anchor: [assa.f107.6.2-1-3]
vault_articles: [methods/structural-credit-risk-models]
vault_sources: []
taught_in: null
---

## Definition

A reduced-form credit model treats default as a random event governed by an
intensity process rather than derived from a modelled path of the firm's asset
value, so default can occur at any time as a jump governed by that intensity,
without needing a balance sheet at all.

## The expression

$$
S(t) = \exp\left(-\int_0^t h(s)\, ds\right)
$$

Here $h(s)$ is the default hazard at time $s$, called the intensity in this
framework, and $S(t)$ is the resulting survival probability to time $t$, the
probability that the intensity process has not yet triggered default.

## Why this node exists

Calibrating default risk directly to an observed credit spread is what a
reduced-form model is built to do, and it is the route every credit derivative
and valuation adjustment in the corpus that prices to market takes instead of
the structural alternative.
