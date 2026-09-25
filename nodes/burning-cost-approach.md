---
id: burning-cost-approach
title: Burning cost approach
domains: [gi]
status: drafted
requires: [premium-structure]
spends: []
anchor: [ifoa.sp8.3.5-1]
vault_articles: [methods/reinsurance-pricing]
vault_sources: []
taught_in: null
---

## Definition

The burning cost approach rates a risk from its own historical claims experience, trending
and developing that experience to the level the new period is expected to reach, and works
best where the risk carries enough of its own credible history to support the projection.

## The expression

$$
\text{burning cost} = \frac{\sum_y L_y}{\sum_y P_y}
$$

Here $L_y$ is the layer loss for historical year $y$ once it has been trended for inflation
and developed to an ultimate value, and $P_y$ is the premium or exposure for that same year,
adjusted onto a comparable rating basis. Summing across the years in the experience period and
dividing gives a single loss cost the new period's rate is built from.

## Why this node exists

A risk's own claims history is the most direct evidence of what it is likely to cost, but that
history is only usable once it has been adjusted onto a common basis across years, since raw
historical losses reflect the exposure and price levels of the year they occurred in.
Non-proportional reinsurance pricing needs a loss cost settled this way before it can layer
risk loading and free cover on top of it.
