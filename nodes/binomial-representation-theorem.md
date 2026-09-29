---
id: binomial-representation-theorem
title: Binomial representation theorem
domains: [fin-eng, stats]
status: drafted
requires: [filtration]
spends: []
anchor: [ifoa.sp6.3.2-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The binomial representation theorem states that, in a binomial model, the discounted gains
process of any previsible trading strategy can be written as a stochastic sum against the
discounted asset price's own martingale increments, so that no traded strategy can generate
gains from anything the asset price's increments do not themselves carry.

## The expression

$$
G_n = G_0 + \sum_{i=1}^{n} \phi_i \, \Delta M_i
$$

Here $G_n$ is the discounted gains process at step $n$, $\phi_i$ is the previsible number of
units of the risky asset held over step $i$, known before that step's outcome is revealed,
and $\Delta M_i$ is the increment of the discounted asset price, which is a martingale under
the risk-neutral measure. Every discounted gains process in the model is built from these
same increments, only the holding $\phi_i$ differing between strategies.

## Why this node exists

A claim can only be replicated by trading the underlying asset if every possible pattern of
gains a strategy could produce is already spanned by that asset's own price movements, and
this theorem is what guarantees that span in the binomial model. Without it, a replicating
strategy could exist without anything establishing that one always does.
