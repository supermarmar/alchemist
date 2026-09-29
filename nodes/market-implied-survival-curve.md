---
id: market-implied-survival-curve
title: Market-implied survival curve
domains: [credit, fin-eng]
status: drafted
requires: [survival-model-credit-risk]
spends:
  - {object: obj.hazard, domain: credit}
anchor: [assa.f107.3.5-4, assa.f107.6.3-5-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A market-implied survival curve backs a reference entity's hazard rate out of a traded credit
spread, treating the market price itself as the source of the probability.

## The expression

$$
h_{\text{mkt}}(t) = \frac{s(t)}{1 - \delta}
$$

Here $s(t)$ is the par credit spread observed at maturity $t$, most often read off a credit
default swap curve, $\delta$ is the recovery rate assumed on the reference obligation, and
$h_{\text{mkt}}(t)$ is the market-implied hazard rate at $t$. A wider spread at a given maturity
implies a higher hazard, and an assumed recovery closer to par implies a proportionately higher
hazard for the same spread, since less of the exposure is assumed lost on default.

## Why this node exists

A hazard estimated from historical default experience answers what has happened to obligors
like this one in the past, while a trading desk pricing a new position needs what the market is
paying for protection today, which can move on news the historical data has not yet caught up
with. Backing the hazard out of the traded spread gives that forward-looking curve directly.
Closed-form approximation versus Monte Carlo simulation for survival curves needs this node
next, comparing how that curve is then computed in practice once obligors are correlated.
