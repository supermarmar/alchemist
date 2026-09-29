---
id: net-interest-income
title: Net interest income
domains: [fin-man]
status: drafted
requires: []
spends: []
anchor: [assa.f107.1.7-1]
vault_articles: [concepts/eve-and-nii]
vault_sources: []
taught_in: null
---

## Definition

Net interest income is the excess of the interest a bank earns on its banking book assets over
the interest it pays on its banking book liabilities, measured over a stated period.

## The expression

$$
\text{NII} = I_A - I_L
$$

Here NII is net interest income, $I_A$ is interest income earned on the bank's assets over the
period, and $I_L$ is interest expense paid on its liabilities over the same period. NII is an earnings measure, so it is projected over a short forward horizon with the balance
sheet held constant, and maturing positions are assumed replaced by new ones of comparable size
and margin.

## Why this node exists

A bank's profitability from lending cannot be read off the interest it earns alone, since that
income only means something set against what the same balance sheet costs to fund. Without
netting the two, a book with high income and even higher funding costs would look identical to
one earning a genuine margin. Net interest margin and net interest spread need this node next,
since both express net interest income as a proportion rather than as a currency amount.
