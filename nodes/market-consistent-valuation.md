---
id: market-consistent-valuation
title: Market-consistent valuation
domains: [actuarial, fin-eng, fin-man, life, regulation]
status: drafted
requires: []
spends: []
anchor: [ifoa.cp1.4.5-2, ifoa.cp1.4.5-5, ifoa.sp1.4.4-1, ifoa.sp2.4.4-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A market-consistent valuation prices a cash flow at what a replicating portfolio
of traded instruments would cost today, so the valuation moves with observed
market prices rather than with an assumption chosen independently of the market.

## The expression

$$
V_0 = \mathbb{E}^{Q}\!\left[e^{-rT} X_T\right]
$$

Here $V_0$ is the market-consistent value placed on the cash flow today, $X_T$ is
the cash flow paid at time $T$, $r$ is the risk-free rate, and $\mathbb{E}^{Q}$ is
expectation taken under the risk-neutral measure, the probability weighting under
which every traded asset's price already equals its own discounted expected
payoff.

## Why this node exists

A valuation set independently of market prices can be checked against nothing,
whereas a market-consistent one can be tested directly against the price of a
traded instrument with the same cash flows. Reserve and capital interplay needs
this valuation next, since a reserve figure that moves with the market is what
lets capital be measured as the buffer sitting above it.
