---
id: options-hedging
title: Options
domains: [fin-eng]
status: drafted
requires: [hedging, option-pricing-and-dynamic-hedging]
spends: []
anchor: [assa.f107.7.5-4-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An option gives its holder the right, but not the obligation, to transact at a fixed
strike price, so a hedger can buy protection against an adverse move in the
underlying while keeping the upside a forward or a swap would give away.

## The expression

$$
\Pi_T = S_T + \max(K - S_T, 0)
$$

Here $\Pi_T$ is the value at maturity of a protective put position, $S_T$ is the
underlying's price at maturity, and $K$ is the option's strike price, so the position
floors the holder's payoff at $K$ while leaving full participation in any rise in
$S_T$ above it.

## Why this node exists

A forward hedge fixes a single future price and removes both the downside and the
upside together, and an option hedge is what a business wants instead whenever it
needs protection against loss without giving up a favourable move: a bank hedging its
own funding cost, or a corporate hedging a foreign receivable, both reach for
exactly this asymmetry.
