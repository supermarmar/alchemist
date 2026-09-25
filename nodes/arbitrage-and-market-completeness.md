---
id: arbitrage-and-market-completeness
title: Arbitrage and market completeness
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.cm2.5.1-1, ifoa.sp5.3.2-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A market is complete when every payoff available at the horizon can be replicated by
trading the assets on offer, so that a claim with no traded twin simply does not arise.

## The expression

$$
\exists\, \phi : V_T(\phi) = X
$$

Here $X$ is the payoff to be priced, $\phi$ is a self-financing trading strategy in the
assets available, and $V_T(\phi)$ is that strategy's value at the horizon $T$. Completeness
holds when a strategy $\phi$ satisfying this equation exists for every payoff $X$ that
could be written on the market's underlying assets.

## Why this node exists

Arbitrage-free pricing gives a single price to a payoff only once a replicating strategy
for it has been found, so completeness is what guarantees that a replicating strategy
exists at all rather than leaving some payoffs unpriced. A forward contract is the simplest
case in which the replicating strategy can be written down directly, which is what forward
contract valuation goes on to do.
