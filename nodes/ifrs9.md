---
id: ifrs9
title: IFRS 9
domains: [fin-man, regulation]
status: drafted
requires: []
spends: []
anchor: [assa.f107.2.6-1]
vault_articles: [regulation/ifrs9-financial-instruments]
vault_sources: []
taught_in: null
---

## Definition

Instead of waiting for objective evidence of impairment to arise, International Financial
Reporting Standard 9 (IFRS 9) requires a lender to recognise an allowance for expected
credit losses on a financial asset from the date it is first recognised. The size of the
allowance depends on whether the asset's credit risk has increased significantly since
origination, which the standard resolves through a three-stage classification.

## The expression

$$
\mathrm{ECL} = \sum_t \mathrm{PD}_t \times \mathrm{LGD}_t \times \mathrm{EAD}_t \times v_t
$$

Here $\mathrm{PD}_t$ is the probability of default in period $t$,
$\mathrm{LGD}_t$ is the loss given default, $\mathrm{EAD}_t$ is the exposure at
default, and $v_t$ discounts the resulting loss back to the reporting date at the
asset's effective interest rate. Stage 1 assets sum this expression over the
twelve months following the reporting date; Stage 2 and Stage 3 assets sum it
over the asset's full remaining lifetime.

## Why this node exists

A single expected-loss number says nothing about which of the three stages a
given asset should sit in, and stage allocation exists to determine the accounting
consequence of that placement, which is a twelve-month sum or a lifetime one.
IFRS 9 stage allocation needs it next, since it decides which horizon this
expression is summed over for a given asset.
