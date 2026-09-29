---
id: feed-forward-neural-network
title: Feed-forward neural network
domains: [ml]
status: drafted
requires: [activation-function]
spends: []
anchor: [ucsc.dl-actuarial-2026.l04]
vault_articles: [methods/feed-forward-networks-claim-frequency]
vault_sources: []
taught_in: null
---

## Definition

A feed-forward neural network composes several layers, each an affine map followed by a
non-linear activation, into a feature extractor whose output feeds a linear readout. With
no hidden layer at all, the composition degenerates to the linear predictor of an ordinary
generalised linear model.

## The expression

$$
h^{(l)} = \sigma\bigl(W^{(l)} h^{(l-1)} + b^{(l)}\bigr)
$$

Here $h^{(l)}$ is the output of layer $l$, with $h^{(0)}$ the raw covariate vector, $W^{(l)}$
and $b^{(l)}$ are that layer's weight matrix and bias vector, and $\sigma$ is the
activation function applied to each entry of the affine map's output.

## Why this node exists

Stacking affine maps and activations is what lets the network learn its own interactions
and functional forms from the data, and it is a strict generalisation of the generalised
linear model, recovered exactly when the composition has no hidden layer. However, fitting the many weight matrices and bias
vectors this stack accumulates needs an algorithm that can differentiate the whole
composition efficiently. Backpropagation needs it next, since it is the chain rule applied
recursively through exactly this layer-by-layer structure that makes fitting a deep
network computationally possible.
