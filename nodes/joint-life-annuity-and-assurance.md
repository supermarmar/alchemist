---
id: joint-life-annuity-and-assurance
title: Joint-life annuity and assurance
domains: [life]
status: drafted
requires: [annuity-function, assurance-function]
spends:
  - {object: obj.discount-factor, domain: life}
  - {object: obj.survival, domain: life}
anchor: [up.ias353.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A joint-life annuity on the last-survivor status values a series of payments contingent on at
least one of two lives surviving, and requires a joint survival probability built jointly from
both lives' individual survival probabilities.

## The expression

$$
{}_k p_{xy} = {}_k p_x \cdot {}_k p_y, \qquad a_{xy} = \sum_{k=0}^{\infty} v^k \, {}_k p_{xy}
$$

Here ${}_k p_x$ and ${}_k p_y$ are the individual probabilities that lives aged $x$ and $y$
respectively survive a further $k$ years, ${}_k p_{xy}$ is the probability that both survive
that same $k$ years, assumed independent so that the joint probability factorises into the
product of the two individual ones, $v$ is the discount factor applied over one year, and
$a_{xy}$ is the value of an annuity payable while both lives remain alive.

## Why this node exists

A benefit written on two lives together, such as a pension continuing to a surviving spouse,
cannot be valued from either life's own survival probability on its own, since the event the
benefit depends on is the joint or the last-survivor status of the pair, a status neither
individual's survival alone determines. Building the joint survival probability from the two individual
probabilities extends the single-life annuity and assurance functions to exactly the pair of
lives the benefit is actually written on.
