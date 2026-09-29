---
id: sequences-of-functions
title: Sequences of functions
domains: [maths]
status: drafted
requires: [sequences-and-series]
spends: []
anchor: [up.wtw310.5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A sequence of functions converges pointwise where, at every fixed input, the sequence of values converges to the limit function's value there; it converges uniformly where the rate of that convergence does not depend on which input is chosen, a strictly stronger condition.

## The expression

$$
\sup_{x \in D} \lvert f_n(x) - f(x) \rvert \to 0 \quad \text{as } n \to \infty
$$

Here $D$ is the common domain of every $f_n$ and of the limit function $f$, $f_n(x)$ and $f(x)$ are the values of the sequence and its limit at $x$, and the supremum over $D$ is what forces every point in the domain to converge at a rate no worse than the slowest one. Pointwise convergence asks only that $f_n(x) \to f(x)$ hold separately at each $x$, with no bound on how the required $n$ varies across $D$.

## Why this node exists

A property that holds for every $f_n$, continuity or a bounded integral among them, need not survive the limit under pointwise convergence alone, since the pointwise definition places no control on how badly the approximation fails near any particular point as $n$ grows. Series of functions needs it next, since a series is only the partial sums of a sequence, and whether it converges uniformly decides whether the same properties survive summing infinitely many functions.
