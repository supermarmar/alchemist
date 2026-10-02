---
id: backpropagation
title: Backpropagation
domains: [ml]
status: drafted
requires: [feed-forward-neural-network, gradient-descent]
spends: []
anchor: [ucsc.dl-actuarial-2026.l04]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Backpropagation computes the gradient of a network's loss with respect to every weight
by applying the chain rule layer by layer from the output back to the input, reusing each
layer's own gradient in the computation for the layer before it.

## The expression

$$
\frac{\partial L}{\partial w^{(l)}} = \frac{\partial L}{\partial z^{(l)}}\,
\frac{\partial z^{(l)}}{\partial w^{(l)}}, \qquad
\frac{\partial L}{\partial z^{(l)}} = \left(\frac{\partial z^{(l+1)}}{\partial z^{(l)}}\right)^{\!\top} \frac{\partial L}{\partial z^{(l+1)}}
$$

Here $L$ is the loss, $z^{(l)}$ is the pre-activation input to layer $l$, $w^{(l)}$ is the
weight matrix of layer $l$, and the second equation is the recursion that carries the
gradient $\partial L / \partial z^{(l+1)}$ already computed at the later layer back to
layer $l$, so that no layer's gradient is recomputed from scratch.

## Why this node exists

A network of any real depth has too many weights for its gradient to be derived by hand
one weight at a time, and backpropagation's layer-by-layer recursion is what makes fitting
such a network by gradient descent computationally feasible in the first place, since each
layer's gradient costs no more to compute than that layer's own forward pass.
