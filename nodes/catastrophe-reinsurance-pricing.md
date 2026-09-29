---
id: catastrophe-reinsurance-pricing
title: Property catastrophe reinsurance pricing
domains: [gi]
status: drafted
requires: [catastrophe-model-structure, reinsurance-product]
spends: []
anchor: [ifoa.sp8.4.5-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Property catastrophe reinsurance pricing sets a premium for losses arising from a catastrophic
event, typically drawn from the output of a catastrophe model, since a genuine catastrophe occurs too rarely for the insurer's own
own claims history, since a genuine catastrophe occurs too rarely for historical experience
alone to price it reliably.

## The expression

$$
\Pi = \mathrm{AAL} + k\,\sigma(L)
$$

Here $\Pi$ is the premium charged for the reinsurance layer, $\mathrm{AAL}$ is the average
annual loss the catastrophe model assigns to that layer, $\sigma(L)$ is the standard deviation
of the layer's simulated loss, and $k$ is a loading multiplier reflecting the reinsurer's cost
of capital and appetite for the layer's volatility. The loading term compensates the reinsurer
for variability the average annual loss alone does not capture.

## Why this node exists

A catastrophe loss is rare enough that an insurer's own claims history rarely contains an
example of the event actually occurring, so a pricing method built on historical loss ratios
has nothing to estimate from. The catastrophe model supplies a simulated loss distribution in
its place, and the reinsurer's own risk appetite, expressed through the loading multiplier,
is what turns that distribution into a premium it is willing to write the layer at.
