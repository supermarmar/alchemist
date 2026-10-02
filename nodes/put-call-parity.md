---
id: put-call-parity
title: Put-call parity
domains: [fin-eng]
status: drafted
requires: [forward-contract-valuation]
spends: []
anchor: [ifoa.cm2.5.1-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Put-call parity is the no-arbitrage relationship linking a European call price to the European put price on the same underlying asset, strike and expiry, through the underlying's current price and the present value of the strike.

## The expression

$$
C - P = S_0 - K e^{-rT}
$$

Here $C$ and $P$ are the call and put prices, $S_0$ is the underlying asset's price today, $K$ is the common strike, $r$ is the risk-free rate, and $T$ is the time to expiry. The relationship follows from valuing two portfolios with identical payoffs at expiry, a call plus cash of $Ke^{-rT}$ against a put plus the underlying, with no assumption needed about how the underlying moves between now and then.

## Why this node exists

A trader who could buy the cheaper side of this identity and sell the dearer would lock in a riskless profit at no cost today, so parity is what stops a call and a put on the same terms from ever being quoted at prices the market itself would arbitrage away. It gives a model-free check on any option pricing model: whatever price a binomial tree or a diffusion model assigns to a call, this identity pins down the same model's put price without a separate calibration.
