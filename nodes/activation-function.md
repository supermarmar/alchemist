---
id: activation-function
title: Activation function
domains: [ml]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l04]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An activation function applies a fixed non-linear transformation to a neuron's affine
input, and without it a network of any depth collapses to a single linear map, since a
composition of linear functions is itself linear.

## The expression

$$
a = \sigma(z), \qquad \sigma(z) = \frac{1}{1 + e^{-z}}
$$

Here $z$ is the affine input a neuron receives from the layer before it, $\sigma$ is the
activation function, taken here as the logistic sigmoid, and $a$ is the neuron's output
passed forward to the next layer. The hyperbolic tangent and the rectified linear unit
replace $\sigma$ with a different fixed shape, and each shape governs how a gradient
computed at the output propagates back through the neuron during training.

## Why this node exists

A stack of affine layers with no non-linearity between them is algebraically a single
affine layer, so depth buys nothing without an activation function breaking the
composition. Choosing which shape to use, and how each one saturates or dies at its
extremes, is the concern the feed-forward neural network needs settled before it can be
assembled.
