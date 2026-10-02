---
id: attention-mechanism
title: Attention mechanism
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

An attention layer gives every element of a sequence a query, a key, and a value vector,
and computes each element's output as a weighted average of every element's value, with
the weight on each contribution set by how closely that element's key matches the
querying element's query.

## The expression

$$
\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right) V
$$

Here $Q$, $K$, and $V$ are matrices whose rows are the query, key, and value vectors of
every element in the sequence, $QK^{\top}$ scores every query against every key, $d_k$ is
the dimension of the key vectors, and the softmax turns each row of scores into a set of
weights that sum to one before they are applied to $V$.

## Why this node exists

A recurrent or convolutional layer lets two elements of a sequence interact only through
a chain of intermediate steps, so their influence on each other weakens with distance,
and attention is what lets any two elements interact in a single step regardless of how
far apart they sit. Multi-head attention needs it next, since running several attention
computations in parallel is how the mechanism captures more than one kind of relationship
between elements at once.
