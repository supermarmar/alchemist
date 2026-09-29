---
id: topological-properties-of-euclidean-space
title: Topological properties of Euclidean space
domains: [maths]
status: drafted
requires: [real-number-properties]
spends: []
anchor: [up.wtw310.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A subset of Euclidean space is open when it contains, around each of its own points, an
entire ball of some positive radius; it is closed when its complement is open, compact
when every open cover of it admits a finite subcover, and connected when it cannot be
split into two disjoint nonempty subsets that are both open in it.

## The expression

$$
B(x, r) = \{\, y \in \mathbb{R}^n : \lVert y - x \rVert \lt r \,\}
$$

Here $B(x, r)$ is the open ball of radius $r$ centred at $x$, $y$ ranges over the points
of $\mathbb{R}^n$ being tested for membership, and $\lVert y - x \rVert$ is the Euclidean
distance between $y$ and $x$. Every other notion this node covers, closed, compact,
connected and complete, is phrased in terms of this one ball.

## Why this node exists

A function's continuity is stated entirely in terms of which sets are open, so continuity
cannot be defined until openness has a precise meaning, and compactness is what lets an
optimisation problem over an infinite set guarantee that a minimum is actually attained
rather than only approached. Continuous function properties needs it next.
