---
id: recurrent-neural-network
title: Recurrent neural network
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

A recurrent neural network processes a sequence one step at a time, updating a
hidden state at each step from the current input and the state's own value at
the previous step, so that the hidden state at any point summarises everything
the network has seen so far in the sequence.

## The expression

$$
h_t = f(W x_t + U h_{t-1} + b)
$$

Here $x_t$ is the input at step $t$, $h_{t-1}$ is the hidden state carried
forward from the previous step, $W$ and $U$ are weight matrices applied to the
input and the previous state respectively, $b$ is a bias term, and $f$ is a
nonlinear activation function producing the updated hidden state $h_t$.

## Why this node exists

A network built only from independent, fixed-width inputs has no way to let
information from early in a sequence reach a prediction made much later, which
is precisely the limitation plain recurrence still has over long sequences and
the reason the gated architectures built on top of it exist.
