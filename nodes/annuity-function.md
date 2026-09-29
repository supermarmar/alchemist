---
id: annuity-function
title: Annuity function
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

An annuity function values a series of payments contingent on survival, combining
the probability of surviving to each payment date with the time value of money
applied to that date.

## The expression

$$
a_x = \sum_{k=0}^{\infty} v^k \, {}_k p_x
$$

Here $a_x$ is the value of the annuity to a life aged $x$, $v$ is the discount
factor applied over one year, and ${}_k p_x$ is the probability that a life aged
$x$ survives a further $k$ years. Each term discounts one payment to today and
weights it by the chance the life is still alive to receive it.

## Why this node exists

A benefit payable only while someone is alive cannot be valued by discounting alone,
since discounting says nothing about whether the payment is ever made, so the
annuity function is what combines the two ingredients into one value. Joint-life
annuity and assurance needs it next, since it extends the same summation to a
benefit contingent on the survival of more than one life.
