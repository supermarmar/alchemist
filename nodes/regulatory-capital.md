---
id: regulatory-capital
title: Regulatory capital
domains: [fin-man, regulation]
status: drafted
requires: []
spends: []
anchor: [assa.f107.1.10-1]
vault_articles: [regulation/crr]
vault_sources: []
taught_in: null
---

## Definition

Regulatory capital is the capital a bank is required to hold against its risks
under the prevailing prudential framework, as distinct from the capital it holds
by its own economic assessment. It is measured in layers of decreasing loss-
absorbing quality, and the framework treats each layer differently according to
whether it can absorb a loss while the bank remains a going concern.

## The expression

$$
K_{\text{total}} = K_{\text{CET1}} + K_{\text{AT1}} + K_{\text{T2}}
$$

Here $K_{\text{total}}$ is total regulatory capital, $K_{\text{CET1}}$ is common
equity tier 1 capital, the highest-quality layer, $K_{\text{AT1}}$ is additional
tier 1 capital, and $K_{\text{T2}}$ is tier 2 capital, the layer that absorbs
losses only once the bank is no longer a going concern. The Capital Requirements
Regulation sets minimum ratios of each layer against risk-weighted assets, so this
sum is checked against a risk-weighted denominator rather than held in isolation.

## Why this node exists

A capital ratio cannot be computed, still less compared against a regulatory
minimum, until the numerator it uses is defined layer by layer instead of as one
undifferentiated pool. Tier I capital needs this node next, since the CET1 and AT1
layers it defines only make sense as components of the total this node names.
