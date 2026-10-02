---
id: forward-contract-valuation
title: Forward contract valuation
domains: [fin-eng]
status: drafted
requires: [arbitrage-and-market-completeness, forward-futures-payoff]
spends:
  - {object: obj.discount-factor, domain: fin-eng}
anchor: [ifoa.cm2.5.1-3, ifoa.sp6.2.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Once a forward has been entered at a delivery price $K$, valuing it at a later date means
comparing that fixed price against the forward price the market now quotes for the same
maturity, discounted back to today. At inception, when $K$ is set to the prevailing
forward price, the contract's value is exactly zero.

## The expression

$$
V_t = S_t - K\, v^{T-t}
$$

Here $V_t$ is the value at time $t$ of a long position in the forward, $S_t$ is the spot
price of the underlying at $t$, $K$ is the delivery price fixed when the contract was
entered, $v$ is the discount factor for one period, and $T - t$ is the remaining term to
maturity.

## Why this node exists

A forward carries zero value only at the moment it is struck; as the spot price and the
arbitrage-free forward price move away from $K$ over the contract's life, the position
accrues a mark-to-market value that this formula prices without needing a new model built
each time it is asked for. Put-call parity needs it next, since the same no-arbitrage
replication of a forward's payoff from a call and a put option is what the parity relation
is built on.
