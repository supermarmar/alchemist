---
id: cost-and-contribution-determination
title: Cost and contribution determination
domains: [actuarial, fin-man, gi, life]
status: drafted
requires: []
spends:
  - {object: obj.discount-factor, domain: actuarial}
anchor: [ifoa.cp1.4.3-1, ifoa.cp1.4.3-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The cost of a contingent-event benefit is its expected present value, the sum over
every future outcome of the probability that it occurs, weighted by the benefit paid
and discounted back to the valuation date; the contribution is set so that the
expected present value of the contributions charged over time matches that cost.

## The expression

$$
\text{EPV} = \sum_{x} q_x \, B_x \, v^x
$$

Here $\text{EPV}$ is the expected present value of the benefit, $q_x$ is the
probability that the contingent event occurs at time $x$, $B_x$ is the benefit paid if
it does, and $v$ is the discount factor for one period, so that $v^x$ discounts a
payment at time $x$ back to today.

## Why this node exists

A benefit promised without reference to its expected present value leaves nothing for
the contribution to be set against, and a scheme could then charge too little in early
years and rely on later contributions to close a gap it never measured. Fixing the
cost first is what lets the contribution schedule be checked for adequacy, and capital
and provisioning's influence on pricing needs this measured cost next.
