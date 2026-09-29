---
id: discounted-cashflow-model-pricing
title: Discounted cashflow model for product pricing
domains: [fin-eng, fin-man]
status: drafted
requires: []
spends:
  - {object: obj.discount-factor, domain: fin-eng}
anchor: [assa.f107.3.5-7, assa.f107.5.4-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A discounted cashflow model prices a banking product by discounting its projected future cash
flows to a single present value at a chosen discount factor.

## The expression

$$
PV = \sum_{t=1}^{T} CF_t \, v^t
$$

Here $PV$ is the present value of the product, $CF_t$ is the projected net cash flow in period
$t$, $v$ is the discount factor applied per period, and $T$ is the horizon over which cash
flows are projected.

## Why this node exists

A bank cannot compare a loan's income against its cost of funding, its expected losses and its
capital charge until all three are expressed in the same present-value terms this model
supplies. The discount rate assumption in a discounted cashflow model needs it next, since that
assumption is what fixes the value of $v$ for a given product.
