---
id: cash-flow-hedge
title: Cash flow hedge
domains: [fin-man, regulation]
status: drafted
requires: [hedge-accounting]
spends: []
anchor: [iasb.ifrs9.6.5-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A cash flow hedge offsets the exposure to variability in future cash flows, such as interest
payments on variable-rate debt or a highly probable forecast transaction, that is
attributable to a particular risk and could affect profit or loss, and it is one of the three
hedging relationships IFRS 9 recognises for hedge accounting.

## The expression

$$
R = \min\bigl( |\text{cumulative gain or loss on the hedging instrument}|,\ |\text{cumulative change in fair value of the hedged item}| \bigr)
$$

Here $R$ is the amount recognised in the cash flow hedge reserve within other comprehensive
income, taking the lower of the two magnitudes so that any excess volatility from an
overhedged position is pushed to profit or loss instead of parked in equity. IFRS 9 paragraph
6.5.11(a) fixes this as the reserve's defining measure.

## Why this node exists

Without a rule tying the hedging instrument's gain or loss to the hedged item's change in
value, a bank hedging a forecast transaction would recognise the derivative's volatility in
profit or loss immediately while the transaction it hedges has not yet occurred, defeating the
purpose of hedging at all. Hedge accounting only achieves its aim of matching timing once this
reserve mechanism is in place.
