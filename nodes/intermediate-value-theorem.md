---
id: intermediate-value-theorem
title: Intermediate value theorem
domains: [maths]
status: drafted
requires: [functions-limits-and-continuity]
spends: []
anchor: [up.wtw220.5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The intermediate value theorem states that a continuous function on a closed interval takes
every value between its two endpoint values somewhere within that interval. It is degenerate
where the endpoint values are equal, in which case the theorem guarantees only that shared value
is attained.

## The expression

$$
f \text{ continuous on } [a, b], \quad f(a) \le y \le f(b) \implies \exists\, c \in [a, b]: f(c) = y
$$

Here $f$ is the function, $a$ and $b$ are the interval's endpoints, $y$ is any value between
$f(a)$ and $f(b)$, and $c$ is the point the theorem guarantees exists somewhere in $[a, b]$ at
which $f$ takes that value.

## Why this node exists

The theorem guarantees that a root or a target value exists somewhere in the interval, without
saying where, and it is exactly that gap between existence and location that an iterative
root-finding method such as bisection closes by narrowing the interval the theorem already
promises a root lies within.
