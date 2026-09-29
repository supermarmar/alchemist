---
id: standardised-approach-credit-risk
title: Standardised approach for credit risk
domains: [credit, regulation]
status: drafted
requires: [pillar-1-minimum-capital-requirements, risk-weighted-assets, securitisation]
spends:
  - {object: obj.exposure, domain: credit}
  - {object: obj.exposure, domain: regulation}
anchor: [assa.f107.6.1-7-1-1, bcbs.d424.sa.para-1]
vault_articles: [regulation/crr-credit-risk-provisions]
vault_sources: []
taught_in: null
---

## Definition

The standardised approach sets a bank's credit risk capital requirement from risk weights the
regulator prescribes, by exposure class and external rating where one exists. It applies to a
bank without supervisory approval to use its own credit risk models.

## The expression

$$
K = 0.08 \times \mathrm{RWA} = 0.08 \sum_{i=1}^n \mathrm{RW}_i \times \mathrm{EAD}_i
$$

Here $\mathrm{EAD}_i$ is the exposure at default on exposure $i$, $\mathrm{RW}_i$ is the risk
weight the standardised approach prescribes for that exposure's class and rating, $\mathrm{RWA}$
is the risk-weighted total those weights produce, and $K$ is the Pillar 1 minimum capital
requirement, the risk-weighted total scaled by the 8 per cent minimum ratio.

## Why this node exists

A bank without supervisory approval to run its own credit risk models still needs a capital
figure, and the standardised approach supplies one by fixing $\mathrm{RW}_i$ from a published
table keyed to exposure class and external rating. Retail exposure classification and risk
weights needs this node next, applying the same prescribed-weight logic to the specific
categories a retail book is split into.
