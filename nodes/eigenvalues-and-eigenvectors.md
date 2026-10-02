---
id: eigenvalues-and-eigenvectors
title: Eigenvalues and eigenvectors
domains: [maths]
status: drafted
requires: [matrix-algebra-and-linear-systems]
spends: []
anchor: [up.wtw211.6, up.wtw211.7]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An eigenvector of a square matrix is a nonzero vector whose direction the matrix leaves
unchanged, only scaling its length by a factor called the corresponding eigenvalue. A matrix
with a repeated eigenvalue can have more than one linearly independent eigenvector sharing
it.

## The expression

$$
A v = \lambda v
$$

Here $A$ is an $n \times n$ matrix, $v$ is an eigenvector of $A$, and $\lambda$ is the scalar
eigenvalue $v$ carries. Rearranging gives $(A - \lambda I)v = 0$, which has a nonzero
solution $v$ only where $A - \lambda I$ is singular, so the eigenvalues of $A$ are exactly
the roots of $\det(A - \lambda I) = 0$.

## Why this node exists

A matrix applied repeatedly to an arbitrary vector mixes every direction together, and that
mixing is opaque until the directions the matrix treats independently, its eigenvectors, are
found. Matrix diagonalisation needs it next, since expressing a matrix in terms of its
eigenvalues and eigenvectors is what makes repeated application, and much else that a general
matrix makes difficult, tractable.
