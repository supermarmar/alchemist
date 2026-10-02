---
id: continuous-function-properties
title: Continuous function properties
domains: [maths]
status: drafted
requires: [topological-properties-of-euclidean-space]
spends: []
anchor: [up.wtw310.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A continuous function inherits several properties directly from the topological structure of
its domain, the most important being that a continuous function attains a maximum and a minimum
on any compact set.

## The expression

$$
f \text{ continuous on compact } K \implies \exists\, x^* \in K:\ f(x^*) = \sup_{x \in K} f(x)
$$

Here $f$ is a real-valued function, $K$ is a compact subset of its domain, and $x^*$ is a point
in $K$ at which $f$ actually reaches its supremum over $K$, and not merely approaches it.
The same argument applied to $-f$ gives the corresponding result for the minimum.

## Why this node exists

A function continuous on a set that is not compact can approach a supremum without ever
reaching it, so an optimisation problem posed over an unbounded or open domain can fail to have
a solution at all, and this extreme value theorem is what guarantees an optimum exists once the
domain is compact. The Bolzano-Weierstrass and Heine-Borel theorems supply the underlying
guarantee, that a bounded sequence in a closed set has a limit lying back inside that set,
which this theorem's own proof relies on directly.
