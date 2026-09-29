---
id: forward-contract-pricing
title: Pricing a forward contract
domains: [fin-eng]
status: drafted
requires: [risk-neutral-pricing]
spends:
  - {object: obj.discount-factor, domain: fin-eng}
anchor: [assa.f107.5.5-4-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Pricing a forward contract derives its fair price from the spot price of the underlying
asset and the cost of carrying that asset to the contract's maturity, using a no-arbitrage
argument alone, with no model of how the underlying's price might move needed at all.

## The expression

$$
F = \frac{S}{v^T}
$$

Here $F$ is the forward price agreed today for delivery at maturity, $S$ is the spot price
of the underlying today, $v$ is the discount factor for one period, and $T$ is the number
of periods to maturity, so $v^T$ is the present value of one unit payable at maturity.

## Why this node exists

Buying the asset today and carrying it to maturity must cost exactly what agreeing today
to buy it at maturity costs, or an arbitrageur could lock in a risk-free profit from the
gap. That no-arbitrage requirement is what pins the forward price to the spot price and
the cost of carry alone, leaving no room for a forecast of where the underlying will
actually trade to change the answer.
