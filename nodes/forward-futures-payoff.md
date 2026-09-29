---
id: forward-futures-payoff
title: Payoff of a forward or futures contract
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.2.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The payoff to the long side of a forward or futures contract at maturity is the difference between
the settlement price and the price agreed at inception, since no premium changes hands when the
contract is struck.

## The expression

$$
\Pi_T = S_T - K
$$

Here $S_T$ is the settlement price of the underlying at maturity $T$, $K$ is the delivery price
agreed when the contract was struck, and $\Pi_T$ is the payoff to the long position. The short
side's payoff is $K - S_T$, the mirror image, since a forward is a zero-sum exchange between the
two parties.

## Why this node exists

An option's payoff is capped on the downside by the premium the holder paid; a forward's is not,
since neither side paid anything up front and both remain fully exposed to the settlement price.
Forward contract valuation needs this node next, since valuing an open forward before maturity
starts from what its payoff will be once maturity arrives.
