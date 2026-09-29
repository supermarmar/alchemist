---
id: option-payoff-profile
title: Payoff of a call or put option
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

The payoff of a call option is what its holder receives at exercise, and a European option can
only be exercised at expiry while an American option can be exercised at any time up to expiry.

## The expression

$$
\text{Payoff}_{\text{call}} = \max(S_T - K, 0)
$$

Here $S_T$ is the price of the underlying asset at the exercise date and $K$ is the strike
price fixed in the contract. A call pays the excess of $S_T$ over $K$ where the underlying has
risen above the strike, and nothing otherwise. A put is the mirror image, with payoff
$\max(K - S_T, 0)$, paying out where the underlying has fallen below the strike.

## Why this node exists

Every later result about an option's value or its sensitivities is a statement about the
expectation, under some measure, of this payoff, so nothing about pricing or hedging can be
derived before the payoff itself is fixed. Options on different underlying assets needs this
node next, since the same call and put payoffs recur unchanged once the underlying is an
exchange rate, a commodity or an index rather than a single equity.
