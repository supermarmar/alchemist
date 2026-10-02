---
id: dropout
title: Dropout
domains: [ml]
status: drafted
requires: [feed-forward-neural-network]
spends: []
anchor: [ucsc.dl-actuarial-2026.l04]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Dropout regularises a neural network by randomly zeroing a fraction of a layer's units at
every training step, with a fresh random selection drawn each time, so that no unit can rely
on any other specific unit being present.

## The expression

$$
\tilde{a} = \frac{m \odot a}{1 - p}, \qquad m_i \sim \mathrm{Bernoulli}(1 - p)
$$

Here $a$ is the layer's activation vector before dropout, $m$ is a mask vector of
independent Bernoulli draws with survival probability $1 - p$, $p$ is the dropout rate, and
$\odot$ denotes elementwise multiplication. Dividing by $1 - p$ rescales the surviving
activations so that the expected output matches the undropped activation, which is what lets
the same network be run without dropout, and without rescaling, at prediction time.

## Why this node exists

A feed-forward network trained without dropout can fit its training set by having units
co-adapt, each compensating for the specific errors of its neighbours, and that co-adaptation
does not generalise to unseen data. Forcing every unit to be independently useful, since any
of its neighbours might be absent on a given step, is what stops that co-adaptation forming,
and the network that results behaves at prediction time like an implicit average over many
thinned sub-networks trained together.
