---
id: actuarial-cash-flow-model
title: Actuarial cash-flow model
domains: [actuarial, fin-eng]
status: drafted
requires: []
spends:
  - {object: obj.discount-factor, domain: actuarial}
anchor: [up.ias211.1, up.ias211.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An actuarial cash-flow model represents a financial transaction as a set of payments,
positive or negative, each due at a stated future time, before any discounting is applied
to it.

## The expression

$$
V = \sum_{t} v^{t} \, CF_t
$$

Here $CF_t$ is the net cash flow due at time $t$, positive where the transaction receives
money and negative where it pays it out, $v$ is the discount factor for one period, and $V$
is the value the transaction reduces to once every payment is brought back to a common
point in time.

## Why this node exists

A schedule of payments due at different dates cannot be compared, added or priced until
they are all expressed at the same point in time, and discounting each one by $v^t$ is what
makes that comparison valid. Every reserving, pricing and valuation calculation in the
actuarial syllabus assembles from this template of dated cash flows brought to present
value.
