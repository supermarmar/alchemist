---
id: loss-given-default
title: Loss given default
domains: [credit, regulation, stats]
status: drafted
requires: []
spends: []
anchor: [assa.f107.6.1-3-1-2, assa.f107.6.1-9-2, bcbs.d424.irb.para-69]
vault_articles: [regulation/irb-lgd-estimation]
vault_sources: []
taught_in: null
---

## Definition

Loss given default is the proportion of exposure a bank expects not to recover
once a borrower has defaulted, after discounting recoveries and deducting the
cost of resolving the default.

## The expression

$$
LGD = 1 - \frac{\displaystyle\sum_t \text{Recovery}_t\,(1+r)^{-t} - \text{Costs}}{EAD}
$$

Here $EAD$ is the exposure at default, $\text{Recovery}_t$ is the recovery cash
flow received $t$ periods after default, $r$ is the discount rate reflecting the
riskiness and timing of those cash flows, and $\text{Costs}$ covers the direct
and indirect expense of the recovery process, such as workout staff and legal
fees.

## Why this node exists

A default is not the end of the loss calculation until it is known how much of
the exposure comes back, and this node is what turns that recovery process into
a single parameter a capital formula can use. The expected loss amount
calculation needs it next, since it multiplies this loss given default against
the probability of default and the exposure at default to arrive at the loss a
book expects to take.
