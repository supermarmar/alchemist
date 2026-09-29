---
id: convolutional-neural-network
title: Convolutional neural network
domains: [ml]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l03]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A convolutional layer applies the same filter, a small set of weights, at every
position of its input, so it responds to a local pattern wherever that pattern occurs
instead of only at the position it was learned from.

## The expression

$$
y_i = \sum_{m=1}^{k} w_m \, x_{i+m}
$$

Here $x$ is the input sequence, $w_1,\ldots,w_k$ are the $k$ weights of the filter,
shared across every position $i$, and $y_i$ is the output at position $i$, the
weighted sum of the $k$ input values the filter currently overlaps.

## Why this node exists

A fully connected layer gives every input position its own weight, so a delinquency
shape that appears three months later than the layer was trained on falls on weights
that never learned it. Sharing one filter across every position removes that
dependence on where the pattern sits, and it is what lets a network built this way
generalise across accounts whose histories share a shape but not a length.
