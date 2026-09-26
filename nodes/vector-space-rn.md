---
id: vector-space-rn
title: Vector space of n-tuples
domains: [maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw124.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The vector space $\mathbb{R}^n$ is the set of all ordered $n$-tuples of real
numbers, made into a vector space by adding and scaling the entries one at a time.

## The expression

$$
(x_1,\dots,x_n) + (y_1,\dots,y_n) = (x_1+y_1,\dots,x_n+y_n), \qquad c(x_1,\dots,x_n) = (cx_1,\dots,cx_n)
$$

Here $x=(x_1,\dots,x_n)$ and $y=(y_1,\dots,y_n)$ are two vectors in $\mathbb{R}^n$
and $c$ is a real scalar. Addition and scalar multiplication are each carried out
entry by entry, so the sum or the scaled vector is again an $n$-tuple of real
numbers.

## Why this node exists

Every later construction in the linear algebra branch is stated as an operation on
these n-tuples, so the space itself needs fixing before any of them can be defined.
A linear transformation, a system of equations, and a line or a plane in space are
all examples. Abstract vector space needs it next, since it generalises exactly
this componentwise structure to sets, such as polynomials or matrices, that are
not tuples of numbers at all.
