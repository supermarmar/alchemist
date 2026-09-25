---
id: survival-model-credit-risk
title: Survival models for credit risk management
domains: [credit, stats]
status: drafted
requires: []
spends:
  - {object: obj.lifetime-cdf, domain: credit}
  - {object: obj.lifetime-cdf, domain: stats}
  - {object: obj.survival, domain: credit}
  - {object: obj.survival, domain: stats}
anchor: [assa.f107.3.5-3]
vault_articles: [methods/survival-analysis-macroeconomic-pd]
vault_sources: []
taught_in: null
---

## Definition

A survival model for credit risk estimates the time until a borrower defaults as the
object of interest, giving a full curve over the loan's life instead of a single
probability measured at one fixed horizon.

## The expression

$$
F(t) = 1 - S(t)
$$

Here $F(t)$ is the cumulative probability that default has occurred by time $t$, and
$S(t)$ is the probability that it has not; both are spelled identically in credit risk
and in general statistics. A fixed-horizon probability of default measures $F(t)$ at
one chosen $t$ and stops there, whereas the survival-based view carries the curve
joining every other value of $t$ as well.

## Why this node exists

A single twelve-month probability cannot say whether a portfolio's risk is concentrated
in its first year on book or spread evenly across its life, and cannot be re-priced
against a stressed economic scenario without being refitted from scratch at that one
horizon. Bellotti and Crook's Cox model with time-varying macroeconomic covariates
solves both problems at once: because the covariates enter as explicit series rather
than fixed-at-origination characteristics, a scenario forecast can simply be substituted
for its historical values to generate a stressed default curve. The market-implied
survival curve needs this framing next, reading the same curve off traded prices
instead of a fitted hazard model.
