---
id: initial-measurement-at-fair-value
title: Initial measurement at fair value
domains: [fin-man, regulation]
status: drafted
requires: [transaction-costs]
spends: []
anchor: [iasb.ifrs9.5.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A financial asset or liability is initially measured at its fair value at the transaction date,
adjusted by the transaction costs directly attributable to its acquisition or issue, unless it
is measured at fair value through profit or loss, in which case those costs are expensed
immediately. It is degenerate for an instrument at fair value through profit or loss, where the
initial carrying amount is fair value alone.

## The expression

$$
C_0 = FV_0 + TC
$$

Here $C_0$ is the instrument's initial carrying amount, $FV_0$ is its fair value at the
transaction date, and $TC$ is the transaction costs added for an instrument outside the fair
value through profit or loss category, or omitted, expensed instead, for one inside it.

## Why this node exists

Every later measurement of the instrument, whether at amortised cost or at fair value, starts
from this initial carrying amount, so an error here propagates through every subsequent period.
Effective interest method needs it next, since the rate that spreads the instrument's income
over its life is the one that discounts its contractual cash flows back to exactly this carrying
amount.
