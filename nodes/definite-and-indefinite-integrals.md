---
id: definite-and-indefinite-integrals
title: Definite and indefinite integrals
domains: [maths]
status: drafted
requires: [functions-limits-and-continuity]
spends: []
anchor: [up.wtw114.10, up.wtw114.9]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An indefinite integral of a function is any function whose derivative recovers it, and a definite
integral over an interval is the limit of a sum of thin rectangles under the function's graph as
their width shrinks to zero, giving the signed area between the function and the horizontal axis.

## The expression

$$
\int f(x)\,dx = F(x) + C, \quad F'(x) = f(x)
$$

$$
\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^{*})\,\Delta x
$$

Here $f$ is the function being integrated, $F$ is an antiderivative of $f$, $C$ is an arbitrary
constant, since any two antiderivatives of the same function differ only by a constant, $a$ and
$b$ are the interval's endpoints, $\Delta x = (b-a)/n$ is the width of each of the $n$
rectangles, and $x_i^{*}$ is a point sampled from the $i$-th rectangle.

## Why this node exists

A definite integral defined only as a limit of sums is correct but unusable for anything beyond
the simplest functions, since the limit itself has to be evaluated directly. The fundamental
theorem of calculus needs both objects named here next, because it is the result that lets a
definite integral be evaluated from an indefinite one.
