---
id: non-proportional-reinsurance-pricing
title: Non-proportional reinsurance pricing
domains: [gi]
status: drafted
requires: [burning-cost-approach, reinsurance-product]
spends: []
anchor: [ifoa.sp8.4.5-2]
vault_articles: [methods/reinsurance-pricing]
vault_sources: []
taught_in: null
---

## Definition

Burning cost pricing sets a reinsurance layer's rate as the ratio of that layer's
trended and developed historical losses to the adjusted premium base they arose
from, so the rate is read directly off the treaty's own claims experience.

## The expression

$$
\text{burning cost rate} = \frac{\sum_i L_i^{\text{layer}}}{\sum_i P_i^{\text{adj}}}
$$

Here $L_i^{\text{layer}}$ is the loss from historical year $i$ that falls within the
layer once trended for inflation and developed to ultimate, and $P_i^{\text{adj}}$ is
that year's premium, adjusted to a common exposure basis.

## Why this node exists

A treaty's own loss history carries little credibility for the top of a high layer,
where few historical losses have ever reached, and exposure rating exists precisely
because burning cost alone cannot price that region. This node states the
experience-rating half of that pairing, the anchor an exposure curve's relativities
are commonly reconciled against for the layer's lower part.
