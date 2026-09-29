---
id: available-capital
title: Available capital
domains: [fin-man]
status: drafted
requires: [regulatory-capital]
spends: []
anchor: [assa.f107.1.10-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Available capital is the capital a bank actually holds on its balance sheet,
summed across its regulatory tiers, as distinct from the capital a rule or a model
says it needs.

## The expression

$$
C_{\text{available}} = \mathrm{CET1} + \mathrm{AT1} + \mathrm{T2}
$$

Here $\mathrm{CET1}$ is common equity tier 1 capital, $\mathrm{AT1}$ is additional
tier 1 capital, and $\mathrm{T2}$ is tier 2 capital. Their sum is the book capital
held against the risks a regulatory capital requirement is measured against.

## Why this node exists

A capital ratio has a numerator as well as a denominator, and until the numerator
is fixed as the capital the bank actually holds, no ratio can be compared against
a requirement built on risk-weighted assets. Impact of pension risk on available
capital needs it next, since a pension deficit is deducted directly from this same
total before the ratio is struck.
