---
id: orthogonality
title: Orthogonality
domains: [maths]
status: drafted
requires: [abstract-vector-space]
spends: []
anchor: [up.wtw221.4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Two vectors in an inner product space are orthogonal where their inner product is
zero, extending the geometric notion of perpendicularity beyond ordinary
two-dimensional or three-dimensional space, and a basis built entirely from such
vectors is an orthogonal basis.

## The expression

$$
\langle \mathbf{u}, \mathbf{v} \rangle = 0
$$

Here $\mathbf{u}$ and $\mathbf{v}$ are vectors in the space, and $\langle \cdot,
\cdot \rangle$ is the inner product the space is equipped with.

## Why this node exists

Expressing a vector in terms of a general basis needs a system of equations to be
solved for the coefficients, and an orthogonal basis collapses that system to a
single inner product per coefficient, because every cross term in the general
expansion vanishes by definition. Diagonalisability of symmetric matrices needs it
next, since the eigenvectors that diagonalise a symmetric matrix are exactly such an
orthogonal basis.
