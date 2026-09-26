---
id: arbitrage-and-hedging
title: Arbitrage and hedging
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [up.wtw364.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Arbitrage is a trading strategy costing nothing to set up that produces a possible profit
with no possibility of loss, and its absence in a market is what makes hedging, the
construction of a position that offsets an existing exposure, a well-posed pricing problem
rather than a bet.

## The expression

$$
V_0 = 0, \quad P(V_T \ge 0) = 1, \quad P(V_T \gt 0) \gt 0
$$

Here $V_0$ is the value of the strategy at outset, $V_T$ is its value at the horizon $T$,
and the three conditions together define an arbitrage: no cost to enter, no chance of a
loss, and some chance of a gain. A market is arbitrage-free precisely when no strategy
satisfying all three exists.

## Why this node exists

A hedge is priced by finding the portfolio that replicates the exposure it offsets, and
that price is only unique where no arbitrage lets two portfolios with the same future
payoff trade today at different values. Ruling arbitrage out here is what the binomial
option pricing model relies on to fix a single price instead of a range of them.
