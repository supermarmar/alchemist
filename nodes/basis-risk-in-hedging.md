---
id: basis-risk-in-hedging
title: Basis risk in a hedging strategy
domains: [fin-eng]
status: drafted
requires: [hedging]
spends: []
anchor: [ifoa.sp6.4.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Basis risk is the residual risk left once a hedge is in place, arising wherever the
hedging instrument's price does not move exactly in line with the exposure it is
meant to offset.

## The expression

$$
b = S - F
$$

Here $S$ is the spot price of the exposure being hedged, $F$ is the price of the
hedging instrument, typically a futures contract, and $b$ is the basis. It is the
change in $b$ over the life of the hedge, rather than its level at any one date,
that leaves the hedger exposed.

## Why this node exists

A hedge built from an instrument that only approximates the exposure it offsets
can never eliminate risk entirely, and basis risk is the name for exactly the gap
that remains. However carefully the hedge ratio is chosen, a change in the basis
between the hedge's inception and its close still passes straight through to the
hedger's result.
