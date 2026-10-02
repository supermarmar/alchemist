---
id: binomial-and-trinomial-trees
title: Binomial and trinomial trees
domains: [fin-eng]
status: drafted
requires: [binomial-option-pricing-model]
spends: []
anchor: [ifoa.sp6.3.5-1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A trinomial tree extends the binomial lattice by adding a middle branch at each step, so the
underlying asset can move up, down or stay within a band at every date, and this converges to
the continuous-time price faster than a binomial tree with the same number of time steps.

## The expression

$$
V_i = e^{-r\,\Delta t}\bigl(p_u V_{i+1}^{u} + p_m V_{i+1}^{m} + p_d V_{i+1}^{d}\bigr)
$$

Here $V_i$ is the option's value at node $i$, $r$ is the risk-free rate, $\Delta t$ is the
length of one time step, and $V_{i+1}^{u}$, $V_{i+1}^{m}$ and $V_{i+1}^{d}$ are the option's
values at the up, middle and down successor nodes, reached with risk-neutral probabilities
$p_u$, $p_m$ and $p_d$ chosen so that the tree matches the underlying asset's mean and
variance over one step. Working backwards from maturity through this recursion prices the
option at every earlier node in turn.

## Why this node exists

A binomial tree needs more steps to reach a given accuracy than a trinomial one does, since
each binomial step carries only two outcomes to represent a continuum of possible moves.
Adding the middle branch lets the tree hold an early-exercise or barrier feature at a node
positioned exactly on the barrier, which a coarser binomial grid can only approximate, so a
trinomial tree is the practical choice whenever precision matters more than a simpler
recursion.
