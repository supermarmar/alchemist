---
id: investment-risk-budgeting
title: Investment risk budgeting
domains: [fin-eng, fin-man]
status: drafted
requires: [value-at-risk]
spends: []
anchor: [ifoa.cp1.4.6-3, ifoa.sp5.7.7-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Risk budgeting allocates a portfolio's total Value at Risk across its constituent assets by
each asset's marginal contribution to that total, so that the portfolio manager can compare
and constrain risk-taking asset by asset rather than only at the portfolio level.

## The expression

$$
\mathrm{VaR}_p = \sum_{i=1}^{n} w_i \cdot \mathrm{MVaR}_i, \qquad \mathrm{MVaR}_i = \frac{\partial \, \mathrm{VaR}_p}{\partial w_i}
$$

Here $\mathrm{VaR}_p$ is the portfolio's total Value at Risk, $w_i$ is the weight of asset $i$
in the portfolio, and $\mathrm{MVaR}_i$ is asset $i$'s marginal Value at Risk, the rate at
which the portfolio's VaR changes as that asset's weight increases. Because VaR is homogeneous
of degree one in the portfolio weights, the component contributions $w_i \cdot \mathrm{MVaR}_i$
sum exactly to $\mathrm{VaR}_p$, so each asset's component VaR is a well-defined share of the
portfolio's total risk that a risk budget can be set against.

## Why this node exists

A single portfolio-level VaR figure says how much the portfolio could lose but not which
positions are driving that figure, so a manager cannot tell from VaR alone where to cut
exposure if the total needs to come down. Decomposing VaR into each asset's component
contribution gives the manager a figure to set a budget against and to monitor asset by asset,
turning a single risk constraint on the portfolio into a set of constraints the manager can
actually act on when allocating capital across the book.
