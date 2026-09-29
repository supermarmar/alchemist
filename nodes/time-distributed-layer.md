---
id: time-distributed-layer
title: Time-distributed layer
domains: [ml]
status: drafted
requires: [feed-forward-neural-network]
spends:
  - {object: obj.coefficients, domain: ml}
anchor: [ucsc.dl-actuarial-2026.l10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A time-distributed layer applies one feed-forward network, with a single shared set of
weights, independently to every time slice of a sequence, so its parameter count is fixed
regardless of how long the sequence is.

## The expression

$$
y_t = f(x_t; \theta), \qquad t = 1, \dots, T
$$

Here $x_t$ is the input at time slice $t$, $\theta$ is the one set of weights (spent here as
coefficients) shared across every slice, $f$ is the feed-forward network the layer wraps,
$y_t$ is the output produced from that slice alone, and $T$ is the sequence length; no term in
the formula depends on any input other than $x_t$ itself.

## Why this node exists

Applying the same network independently to each slice keeps the layer's parameter count fixed
and its computation parallel across time, since no slice's output can influence another's.
That independence is deliberate. A later mechanism built to let information cross between time
slices can only combine what this layer has already reduced each slice to: a fixed-size
representation produced without reference to any other position in the sequence.
