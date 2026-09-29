---
id: convertible-bond
title: Convertible bond
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.2.4-6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A convertible bond gives the holder the right, but not the obligation, to exchange it
for a fixed number of the issuer's shares, so its value is at least the greater of what
it would be worth as a straight bond and what it would be worth if converted today.

## The expression

$$
V_{\text{conv}} = r \cdot S
$$

Here $V_{\text{conv}}$ is the conversion value, the amount the bond would be worth if
converted immediately, $r$ is the conversion ratio, the number of shares received per
bond, and $S$ is the current share price; the bond's own value never falls below this
figure once conversion is available.

## Why this node exists

A straight bond's value depends only on the issuer's credit and prevailing interest
rates, and neither explains why a convertible bond's price rises alongside the
issuer's share price. Comparing the bond's market value against its conversion value
is what isolates the embedded option's contribution, and that comparison is the
starting point for pricing the option itself.
