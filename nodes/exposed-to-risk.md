---
id: exposed-to-risk
title: Exposed to risk
domains: [life]
status: drafted
requires: [survival-model]
spends: []
anchor: [up.ias382.5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Exposed to risk measures the total time each member of a population was observed and at
risk of the event a mortality investigation studies, summed across the population aged
exactly $x$ during the period under investigation. A life who enters and leaves the
observation on the same day contributes zero exposure.

## The expression

$$
E_x^c = \sum_i d_i
$$

Here $E_x^c$ is the central exposed to risk at age $x$, and $d_i$ is the duration, in
years, that individual $i$ was observed while aged $x$ during the investigation period.

## Why this node exists

An observed count of deaths says nothing about a rate on its own, since the same number of
deaths in a population observed for one year and one observed for ten years imply very
different mortality. Exposed to risk supplies the denominator that turns the count into a
rate, and every mortality rate the corpus later estimates is built on this same time-at-risk
sum.
