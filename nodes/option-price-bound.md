---
id: option-price-bound
title: Bounds on option price
domains: [fin-eng]
status: drafted
requires: [arbitrage-and-market-completeness]
spends: []
anchor: [ifoa.cm2.5.1-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

No-arbitrage restricts a European call's price to lie between two bounds set purely by the
underlying's spot price and the discounted strike, without appeal to any pricing model. The
lower bound collapses to zero exactly when the discounted strike exceeds the spot price, since
a call can never be worth less than nothing.

## The expression

$$
\max\bigl(S_0 - Ke^{-rT},\, 0\bigr) \le C_0 \le S_0
$$

Here $S_0$ is the underlying's spot price, $K$ is the strike, $r$ is the risk-free rate, $T$ is
the time to expiry, and $C_0$ is the call's price today. A violation of either bound would let a
trader buy the cheaper side and sell the dearer, locking in a riskless profit at no cost today.

## Why this node exists

A pricing model can be checked against these bounds before it is trusted for anything more
precise, since any model that prices a call outside them carries an arbitrage regardless of how
its other inputs were estimated. The bounds hold on the spot price and the discounted strike
alone, asking nothing of volatility or the underlying's future distribution, which is what
lets them survive every model built afterwards.
