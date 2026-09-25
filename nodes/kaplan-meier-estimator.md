---
id: kaplan-meier-estimator
title: Kaplan-Meier estimator
domains: [life, stats]
status: drafted
requires: [censoring, empirical-survival-function]
spends:
  - {object: obj.survival, domain: life}
  - {object: obj.survival, domain: stats}
anchor: [ifoa.cs2.4.2-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Kaplan-Meier estimator is the product-limit estimate of the survival function,
built by multiplying conditional survival probabilities across every observed event
time, so a subject censored after a given time still contributes to the risk set up to
the point it left.

## The expression

$$
\hat{S}(t) = \prod_{t_j \le t} \left(1 - \frac{d_j}{n_j}\right)
$$

Here $\hat{S}(t)$ is the Kaplan-Meier estimate of survival past $t$, $t_j$ ranges over
the distinct observed event times up to $t$, $d_j$ is the number of events occurring at
$t_j$, and $n_j$ is the number of subjects still at risk immediately before $t_j$. Each
factor is a conditional survival probability over one short interval, and the product
carries the same $S(t)$ statistics already names forward through every censored
subject that interval passes over; life table notation would read the same estimate
as ${}_tp_x$, built here from observed events rather than a tabulated $l_x$.

## Why this node exists

A censored sample has no time at which the raw proportion still event-free can simply
be counted, since some subjects have left the risk set without their outcome ever being
resolved. Multiplying conditional probabilities across the risk set as it shrinks
recovers a consistent survival curve regardless, and Greenwood's formula then supplies
the estimator's own standard error from the same $d_j$ and $n_j$ this node already
needs.
