---
id: binomial-and-poisson-exposure-models
title: Binomial and Poisson exposure models
domains: [life, stats]
status: drafted
requires: [survival-model]
spends:
  - {object: obj.hazard, domain: life}
  - {object: obj.lifetime-cdf, domain: life}
anchor: [up.ias382.4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The binomial and Poisson exposure models are two competing ways of counting the deaths an
investigation observes against the time each member of a population was exposed to the risk
of dying, and they differ in whether that exposure is measured to the exact moment of death
or only to the end of the observation period.

## The expression

$$
D \sim \mathrm{Binomial}\bigl(n,\; {}_{1}q_x\bigr), \qquad D \sim \mathrm{Poisson}\bigl(E^{c}_x \, \mu_x\bigr)
$$

Here $D$ is the observed number of deaths, $n$ is the initial number of lives exposed to
risk, ${}_{1}q_x$ is the probability that a life aged $x$ dies within the year, often
abbreviated $q_x$, $E^{c}_x$ is the central exposed to risk, the time each life was actually
observed, and $\mu_x$ is the force of mortality. The binomial form counts deaths against
lives at risk at the start of the period; the Poisson form counts them against the exact time
exposed, which is why it pairs with the force of mortality and not the one-year mortality
probability.

## Why this node exists

A mortality investigation cannot compare observed deaths against expected deaths until it has
settled which of these two exposure conventions it is using, since the two give different
answers for lives that die, withdraw or enter partway through the period. The choice between
them is what a graduation of the resulting rates has to carry forward consistently.
