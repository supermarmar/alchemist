---
id: bolzano-weierstrass-and-heine-borel-theorems
title: Bolzano-Weierstrass and Heine-Borel theorems
domains: [maths]
status: drafted
requires: [sequences-and-series]
spends: []
anchor: [up.wtw220.4, up.wtw310.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Bolzano-Weierstrass theorem states that every bounded sequence of real numbers contains a
convergent subsequence. The Heine-Borel theorem characterises the compact subsets of the real
line as exactly those that are closed and bounded.

## The expression

$$
(x_n) \text{ bounded} \implies \exists\,(x_{n_k}) \text{ with } x_{n_k} \to x^*
$$

$$
K \subset \mathbb{R} \text{ compact} \iff K \text{ closed and bounded}
$$

Here $(x_n)$ is a bounded sequence, $(x_{n_k})$ is a subsequence of it indexed by a strictly
increasing sequence of indices $n_k$, $x^*$ is the point that subsequence converges to, and $K$
is a subset of the real line. Boundedness alone guarantees a convergent subsequence exists;
closedness is what guarantees its limit lies back inside the set itself.

## Why this node exists

A function's continuity properties, such as attaining a maximum on a set, hold only where that
set has enough structure to trap a sequence's limit, so it cannot escape or run off to
infinity, and compactness is the property that supplies exactly that structure. Continuous
function properties needs it next, since the extreme value theorem's proof runs a sequence of
points toward a supremum and then invokes these two theorems to guarantee that sequence has a
limit lying inside the set.
