---
id: unit-pricing
title: Unit pricing
domains: [life]
status: drafted
requires: [unit-linked-contract]
spends: []
anchor: [ifoa.sp2.2.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Unit pricing sets the value of one unit in an internal unit-linked fund from the fund's
underlying asset value, with a bid price paid to a policyholder cashing in units and a higher
offer price charged to one buying them.

## The expression

$$
\mathrm{UP}_{\text{bid}} = (1-s)\, \frac{V}{N}, \qquad \mathrm{UP}_{\text{offer}} = (1+s)\,
\frac{V}{N}
$$

Here $V$ is the market value of the fund's underlying assets, $N$ is the number of units
currently in issue, $V/N$ is the mid, or net asset, price per unit, and $s$ is the spread
applied above and below it; the bid price is what a policyholder receives on cashing in units
and the offer price is what a new premium buys them at.

## Why this node exists

A fund priced only at its net asset value gives every trade away at the fund's own expense,
since buying or selling units forces the fund manager to trade the underlying assets and meet
the resulting dealing costs. The bid-offer spread recovers those costs from the policyholder
whose transaction caused them, which is the fairness principle the whole unit-pricing
framework exists to protect.
