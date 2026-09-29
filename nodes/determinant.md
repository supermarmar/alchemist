---
id: determinant
title: Determinant
domains: [maths]
status: drafted
requires: [matrix-algebra-and-linear-systems]
spends: []
anchor: [up.wtw124.5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The determinant of a square matrix is a single scalar computed from its entries, equal to
zero exactly where the matrix is singular. A matrix has an inverse if and only if its
determinant is nonzero.

## The expression

$$
\det(A) = \sum_{j=1}^{n} (-1)^{1+j} a_{1j} M_{1j}
$$

Here $A$ is an $n \times n$ matrix with entries $a_{ij}$, $\det(A)$ is its determinant, and
$M_{1j}$ is the minor formed by deleting row 1 and column $j$ from $A$, itself a determinant
of an $(n-1) \times (n-1)$ matrix. Expanding along the first row this way reduces an
$n \times n$ determinant to a sum of smaller ones, and for a $2 \times 2$ matrix the
recursion terminates immediately at $\det(A) = a_{11}a_{22} - a_{12}a_{21}$.

## Why this node exists

A linear system has a unique solution only where its coefficient matrix is invertible, and
the determinant is what tests for that invertibility without having to attempt the inversion
itself. Without it, a singular coefficient matrix could only be detected by trying to invert
it and watching the attempt fail, rather than by evaluating a single number in advance.
