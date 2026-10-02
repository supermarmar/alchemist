---
id: nsfr-calculation
title: NSFR calculation
domains: [fin-man, regulation]
status: drafted
requires: [net-stable-funding-ratio]
spends: []
anchor: [assa.f107.10.4-3-1]
vault_articles: [regulation/bcbs-liquidity-nsfr-monitoring-tools]
vault_sources: []
taught_in: null
---

## Definition

Computing the net stable funding ratio means applying a stability weight to every liability and
capital item, and an illiquidity weight to every asset item, before the two weighted totals are
divided against each other.

## The expression

$$
\text{ASF} = \sum_i w_i^{\text{ASF}} L_i, \qquad \text{RSF} = \sum_j w_j^{\text{RSF}} A_j
$$

Here $L_i$ is the carrying amount of liability or capital item $i$ and $w_i^{\text{ASF}}$ is
its available-stable-funding weight, running from 100 per cent for equity and long-dated
liabilities down to 0 per cent for short-term wholesale funding, and $A_j$ is the carrying
amount of asset item $j$ with its required-stable-funding weight $w_j^{\text{RSF}}$, low for an
unencumbered government bond and high for a long-dated illiquid loan.

## Why this node exists

The net stable funding ratio's own definition names available and required stable funding as
single totals, but a supervisor and a bank both need those totals built up item by item before
either can be reported or checked. Applying the two weight schedules to the balance sheet is
the calculation step that turns the ratio's definition into a number a bank actually reports.
Addressing NSFR compliance needs this node next, since closing a shortfall means changing the
specific liability and asset items the weights here are applied to.
