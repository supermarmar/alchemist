---
id: leverage-ratio
title: Leverage ratio
domains: [fin-man, regulation]
status: drafted
requires: []
spends: []
anchor: [assa.f107.2.3-7, assa.f107.9.3-2, bcbs.d424.lr.para-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The leverage ratio measures a bank's Tier 1 capital against its total exposure
without risk-weighting that exposure, acting as a floor beneath the risk-weighted
capital ratios and not as a substitute for them.

## The expression

$$
LR = \frac{T_1}{E}
$$

Here $T_1$ is Tier 1 capital and $E$ is the total exposure measure, the sum of a
bank's on-balance-sheet assets, derivative exposures and off-balance-sheet items,
each included at its notional or accounting value rather than at a risk-weighted
figure.

## Why this node exists

A risk-weighted ratio can be gamed by a model that understates risk weights
across the book, and the leverage ratio exists precisely because it cannot be:
its denominator does not depend on any risk model at all. The leverage ratio
minimum requirement needs this measure next, since it is the figure that
requirement sets a floor under.
