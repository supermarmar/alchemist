---
id: operational-risk-capital-assessment
title: Operational risk capital assessment
domains: [fin-man, regulation]
status: drafted
requires: []
spends: []
anchor: [assa.f207.3.1]
vault_articles: [regulation/operational-risk-capital-approaches]
vault_sources: []
taught_in: null
---

## Definition

Operational risk capital assessment sets the minimum capital a bank must hold against
operational risk, computed under the Basel standardised approach from the bank's income
statement and its own loss history rather than from a bank-specific model.

## The expression

$$
\text{ORC} = \text{BIC} \times \text{ILM}
$$

Here ORC is the minimum operational risk capital, BIC is the Business Indicator Component, a
coefficient applied to a three-year average of the bank's income statement size, and ILM is the
Internal Loss Multiplier, which rises above one where the bank's own ten-year average annual
operational losses exceed the Business Indicator Component and falls to one where a bank has
too little loss history to compute it. A supervisor may also fix the ILM at one for every bank
in its jurisdiction, in which case ORC reduces to the Business Indicator Component alone.

## Why this node exists

The Basel Committee withdrew the modelling option operational risk once had, so a bank can no
longer justify its capital by its own loss distribution, and the formula here is what stands in
its place for every bank above the smallest size bucket. Operational risk internal models needs
this node next, since it is the internal-modelling approach the standardised formula replaced,
and understanding what replaced it explains why the internal approach was withdrawn.
