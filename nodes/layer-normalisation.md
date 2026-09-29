---
id: layer-normalisation
title: Layer normalisation
domains: [ml]
status: drafted
requires: [feed-forward-neural-network]
spends: []
anchor: [ucsc.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Layer normalisation standardises one observation's activations across the units of a single
layer, using a mean and variance computed from that observation's own slice alone, and then
rescales the result with trainable parameters.

## The expression

$$
\mu = \frac{1}{H} \sum_{i=1}^{H} x_i, \qquad \sigma^2 = \frac{1}{H} \sum_{i=1}^{H} (x_i - \mu)^2
$$

$$
y_i = \gamma \, \frac{x_i - \mu}{\sqrt{\sigma^2 + \epsilon}} + \beta
$$

Here $x_1, \dots, x_H$ are the $H$ activations of one observation's slice, $\mu$ and
$\sigma^2$ are their mean and variance, computed across those $H$ units alone and not across
other members of a mini-batch. $\epsilon$ is a small constant added for numerical stability,
and $\gamma$ and $\beta$ are trainable scale and shift parameters, shared across observations,
that let the network recover a different scale and location than the raw standardisation would
leave it with. $y_i$ is the normalised and rescaled output for unit $i$.

## Why this node exists

A network's activations can drift in scale from layer to layer as training proceeds, which
slows convergence and makes the choice of learning rate harder to get right. Standardising
each observation's own slice keeps that scale under control without introducing any dependence
on which other observations happen to share a training batch, which is what makes layer
normalisation suited to sequence models and small batches where batch normalisation's
cross-observation statistics are unreliable or unavailable.
