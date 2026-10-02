---
id: warrant
title: Warrant
domains: [fin-eng]
status: drafted
requires: [option-payoff-profile]
spends: []
anchor: [ifoa.sp6.2.4-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A warrant is a long-dated call option a company issues on its own shares, and exercise
creates new shares, which dilutes every existing shareholder's stake; the payoff is zero
wherever the share price at exercise sits below the strike.

## The expression

$$
W_0 = \frac{n}{n + w}\, C_0
$$

Here $W_0$ is the fair value of one warrant, $C_0$ is the value an otherwise identical
call option would have on an undiluted share, $n$ is the number of shares already in
issue, and $w$ is the number of warrants outstanding. The factor $n/(n+w)$ scales the
undiluted call value down to reflect that the new shares created on exercise are spread
across a larger share count than the option pricing formula alone assumes.

## Why this node exists

Pricing a warrant with the ordinary option formula and no adjustment overstates its
value, because that formula prices a claim on shares already in issue, and a warrant's
exercise instead creates the shares it pays out. Without the dilution adjustment, an
issuer would misstate the cost of a warrant it grants and an investor would overpay for
one it buys.
