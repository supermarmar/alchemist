---
id: assurance-function
title: Assurance function
domains: [life]
status: drafted
requires: [survival-model, time-value-of-money]
spends:
  - {object: obj.survival, domain: life}
anchor: [up.ias221.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An assurance function values a benefit payable on death, combining the probability
of dying in a given year with the time value of money applied to the date the
benefit is paid.

## The expression

$$
A_x = \sum_{k=0}^{\infty} v^{k+1} \, {}_k p_x \, q_{x+k}
$$

Here $A_x$ is the value of the assurance to a life aged $x$, $v$ is the discount
factor applied over one year, ${}_k p_x$ is the probability that the life survives
$k$ years, and $q_{x+k}$ is the probability that a life aged $x+k$ dies within the
following year. Each term discounts one possible death benefit to today and
weights it by the chance the death happens in that particular year.

## Why this node exists

A benefit payable only on death cannot be valued by discounting alone, since
discounting says nothing about when, or whether within the modelled term, the
payment falls due, so the assurance function is what supplies that weighting.
Joint-life annuity and assurance needs it next, since it extends the same
weighting of survival, death and discounting to a benefit contingent on more than
one life.
