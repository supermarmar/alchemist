---
id: basel-i-credit-risk-quantification
title: Basel I credit risk quantification
domains: [credit, regulation]
status: drafted
requires: [risk-weighted-assets]
spends: []
anchor: [assa.f107.2.1-1]
vault_articles: [entities/basel-accord-evolution]
vault_sources: []
taught_in: null
---

## Definition

Basel I's approach to credit risk quantification assigns each on-balance-sheet
exposure to one of five risk-weight buckets by counterparty type, so a bank's
risk-weighted assets are a coarse rescaling of raw exposure, and two borrowers
of the same counterparty type carry the same weight whatever their creditworthiness.

## The expression

$$
\mathrm{RWA}_i = w_i \times E_i
$$

Here $E_i$ is the exposure amount for asset $i$, $w_i$ is the risk weight assigned
to its counterparty type, one of 0, 10, 20, 50, or 100 per cent under the 1988
Accord, and $\mathrm{RWA}_i$ is the resulting risk-weighted asset amount.

## Why this node exists

Without a way to rescale assets by riskiness, a capital ratio has nothing but raw
balance sheet size to sit against, and this bucketed weighting is what the 1988
Accord used to supply that rescaling before any internal model existed to do it
more finely. Basel I minimum capital requirements needs it next, since the 8 per
cent minimum ratio is applied directly to the sum of these risk-weighted amounts.
