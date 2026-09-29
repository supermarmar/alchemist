---
id: property-derivative
title: Property derivative
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.2.4-7]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A property derivative is a contract whose payoff is linked to the level of a
property price index, giving exposure to, or protection from, movements in the
property market without the parties holding or transacting the underlying real
estate.

## The expression

$$
\pi = N \times \frac{I_T - I_0}{I_0}
$$

Here $N$ is the contract's notional amount, $I_0$ is the index level at
inception, $I_T$ is the index level at the contract's maturity, and $\pi$ is
the payoff to the party receiving the index return.

## Why this node exists

Defining the payoff against an index rather than against an individual property
leaves open how that index itself should be valued when the contract is
written. Pricing a property swap needs this node next to address the
illiquidity and smoothing that make the index harder to value than the payoff
formula alone suggests.
