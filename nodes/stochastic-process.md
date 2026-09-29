---
id: stochastic-process
title: Stochastic process
domains: [stats]
status: drafted
requires: [random-variable]
spends: []
anchor: [ifoa.cs2.3.1-1, ifoa.cs2.3.1-2, ifoa.cs2.3.1-3, up.wst312.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A stochastic process is a family of random variables, all defined on the same probability space, indexed by a set that typically represents time and read together as a description of how a quantity subject to randomness evolves.

## The expression

$$
X = \{X_t : t \in T\}
$$

Here $T$ is the index set, running over discrete values such as $\{0, 1, 2, \ldots\}$ or a continuous interval such as $[0, \infty)$, and $X_t$ is the random variable observed at index $t$, every one of them defined on the same underlying probability space. Fixing $t$ recovers a single random variable; fixing the underlying outcome instead traces out one realised path of the process across every $t$.

## Why this node exists

A single random variable can describe an outcome observed once, but a claims process, a default hazard evolving with the economic cycle, or a share price needs more than one draw to describe, since what matters is how the randomness at one time relates to the randomness at another. This indexed family gives that relationship a name before any specific process, a random walk, a Poisson process or a diffusion, adds the extra structure that turns the general definition into a model. The Markov property needs it next, since it is the first restriction placed on how one index's randomness may depend on another's.
