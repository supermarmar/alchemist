---
id: option-pricing-and-dynamic-hedging
title: Option pricing and dynamic hedging
domains: [fin-eng]
status: drafted
requires: [risk-neutral-pricing]
spends: []
anchor: [assa.f107.5.5-4-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Dynamic hedging holds a position in the underlying asset that is continuously rebalanced, so
that a written option's value and the hedge together carry no risk from a small move in the
underlying's price. The rebalancing ratio is the option's delta, and it changes with the
underlying's price and with time, which is why the hedge is dynamic and not a single trade held
to expiry.

## The expression

$$
\Delta = \frac{\partial V}{\partial S}
$$

Here $V$ is the option's price under the risk-neutral valuation the previous node supplies, $S$
is the underlying's price, and $\Delta$ is the number of units of the underlying a writer must
hold against one written option, so that the combined position's value does not move, to first
order, with a small change in $S$.

## Why this node exists

Risk-neutral pricing supplies a single fair price for the option, but a bank that has sold it
still carries the risk of the underlying moving before expiry, and delta hedging is the
mechanism that removes that risk trade by trade rather than only at the point of sale.
Operational considerations in derivative pricing need this node next, since running a hedge in
practice raises transaction costs, discrete rebalancing intervals and other frictions this
idealised delta ignores.
