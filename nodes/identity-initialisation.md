---
id: identity-initialisation
title: Identity initialisation
domains: [ml]
status: drafted
requires: [feed-forward-neural-network]
spends: []
anchor: [ucsc.dl-actuarial-2026.l12]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Identity initialisation sets the weights and bias of an added layer or mechanism's output to
zero at the start of training, so that the surrounding network's output is unchanged by the
addition before any gradient step is taken.

## The expression

$$
y = x + W_2\, \sigma(W_1 x + b_1) + b_2, \qquad W_2 = 0, \ b_2 = 0 \text{ at initialisation}
$$

Here $x$ is the network's existing input to the added block, $y$ is the block's output, $W_1$
and $b_1$ are the added block's first-layer weights and bias, $\sigma$ is its activation
function, and $W_2$ and $b_2$ are the weights and bias of the layer that feeds the block's
contribution back into the residual stream. Setting $W_2$ and $b_2$ to zero at initialisation
leaves $y = x$ regardless of $W_1$ and $b_1$, and training then moves $W_2$ and $b_2$ away
from zero only as far as the data supports.

## Why this node exists

Adding a new mechanism to a trained network ordinarily perturbs its output from the first
forward pass, which confounds a training run with the network's earlier, already-useful
behaviour and makes a fair comparison against the unmodified network impossible. Identity
initialisation removes that confound: training starts from a network that computes exactly
what it computed before the mechanism was added, so any change in performance during training
can be attributed to the mechanism alone. The in-context learning credibility transformer
needs it next, since it adds a mechanism to a pretrained network and depends on starting from
that network's untouched behaviour.
