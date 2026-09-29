---
id: basis-risk-reference-rates
title: Basis risk from differing reference rates
domains: [fin-eng]
status: drafted
requires: [forms-of-interest-rate-risk]
spends: []
anchor: [assa.f107.7.2-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Basis risk from differing reference rates is the risk that an asset and a matched liability
still fail to move together in cost, because each is indexed to a different reference rate
whose spread over the other is not fixed.

## The expression

$$
b_t = r^{(1)}_t - r^{(2)}_t
$$

Here $r^{(1)}_t$ and $r^{(2)}_t$ are the two reference rates an asset and its matched liability
reprice against at time $t$, and $b_t$ is the basis between them. A hedge or a matched book
that assumes $b_t$ is constant remains exposed to any change in $b_t$, even where the
repricing dates of the asset and the liability line up exactly.

## Why this node exists

Matching the tenor and the repricing date of an asset against a liability removes the risk
that the two reprice at different times, but the two reference rates can still drift apart in
level even when they reset on the same day. A loan priced off one reference rate and funded by
a deposit priced off another is the clearest case: managing the exposure means hedging the
spread $b_t$ itself, separately from the interest rate level either reference rate carries.
