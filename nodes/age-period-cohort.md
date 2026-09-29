---
id: age-period-cohort
title: Age-period-cohort identification problem
domains: [stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l01]
vault_articles: [methods/credit-default-outcome-construction]
vault_sources: []
taught_in: null
---

## Definition

The age-period-cohort identification problem is that a panel indexed by an entity's own
age, the calendar period, and the cohort it originated from can identify at most two of
those three axes without an external constraint, because the third is always their sum.

## The expression

$$
t = x + c
$$

Here $x$ is age, $t$ is calendar period, and $c$ is the cohort, so any two of the three
axes fix the value of the remaining one. A model that includes all three as free effects is
therefore collinear by construction, and no amount of data resolves that collinearity
without a constraint the modeller imposes.

## Why this node exists

Fitting age, period and cohort effects separately from data alone is impossible, since the
exact linear dependence between the three axes means infinitely many parameter sets fit
the observations equally well. Recognising the identification problem here is what stops a
modeller reading a spurious cohort trend out of an age-period-cohort mortality model that
has simply absorbed the collinearity into an arbitrary split.
