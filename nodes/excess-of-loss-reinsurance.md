---
id: excess-of-loss-reinsurance
title: Excess of loss reinsurance
domains: [gi]
status: drafted
requires: [excess-and-retention-limit]
spends: []
anchor: [ifoa.cs2.1.1-3]
vault_articles: [concepts/reinsurance, methods/reinsurance-pricing]
vault_sources: []
taught_in: null
---

## Definition

Excess of loss reinsurance pays the part of a loss that sits above the cedant's retention,
up to whatever upper limit the treaty sets. Below the retention and above the limit the
cedant carries the loss alone, so the treaty responds only to the slice of each loss
falling inside its layer.

## The expression

$$
Y = \min\bigl(\max(X - M,\ 0),\ L\bigr)
$$

Here $Y$ is the amount the reinsurer pays on a given loss, $X$ is the size of that loss,
$M$ is the cedant's retention, and $L$ is the layer's limit, so the treaty covers losses
from $M$ up to $M + L$.

## Why this node exists

Paying only the slice above $M$ is what ties the reinsurer's result to the shape of the
tail of the severity distribution: two portfolios with the same average claim size can
leave the reinsurer very different bills if one has a heavier tail than the other, even
though the cedant sees near-identical expected losses. Insurer and reinsurer loss
distribution needs it next, since it is this split of $X$ into a retained piece and a
ceded piece that the two parties' separate loss distributions are built from.
