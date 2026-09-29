---
id: retail-exposure-classification-and-risk-weights
title: Retail exposure classification and risk weights
domains: [credit, regulation]
status: drafted
requires: [standardised-approach-credit-risk]
spends:
  - {object: obj.exposure, domain: credit}
  - {object: obj.exposure, domain: regulation}
anchor: [bcbs.d424.sa.para-54]
vault_articles: [regulation/eba-retail-diversification]
vault_sources: []
taught_in: null
---

## Definition

An exposure to an individual or a small business qualifies for the preferential retail risk weight only where it also passes a granularity test: no single counterparty may account for more than a fixed share of the total exposures in the portfolio the test is measured against.

## The expression

$$
\frac{\mathrm{EAD}_i}{\sum_j \mathrm{EAD}_j} \le 0.2\%
$$

Here $\mathrm{EAD}_i$ is counterparty $i$'s exposure at default, $\sum_j \mathrm{EAD}_j$ is the total exposure at default across the retail portfolio the counterparty sits in, and the 0.2 per cent threshold is the granularity criterion the portfolio must satisfy before any exposure within it can carry the reduced weight. A portfolio that fails the test loses the preferential treatment across the whole book, including exposures far from the concentrated name.

## Why this node exists

A flat preferential weight for every small exposure would let a bank concentrate its retail book in a handful of large names and still claim the diversification benefit the weight is meant to reward. The granularity test closes that gap by capping each counterparty's exposure as a share of the whole retail portfolio, which ties the reduced weight to diversification that is actually present. Unhedged foreign currency retail exposure risk weight needs it next, since it starts from a retail exposure that has already cleared this classification and asks what a currency mismatch does to the weight from there.
