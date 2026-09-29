---
id: linear-transformation
title: Linear transformation
domains: [maths]
status: drafted
requires: [vector-space-rn]
spends: []
anchor: [up.wtw211.9]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A linear transformation maps one vector space to another in a way that preserves vector
addition and scalar multiplication, so that the image of a sum or a scaled vector equals the
sum or the scaling of the images taken separately.

## The expression

$$
T(u + v) = T(u) + T(v), \qquad T(cu) = cT(u)
$$

Here $T$ is the transformation, $u$ and $v$ are vectors in the domain space, and $c$ is a
scalar. The two conditions together are equivalent to a single one, that $T(cu + v) = cT(u) +
T(v)$ for every scalar $c$ and every pair of vectors $u, v$, and every linear transformation
between finite-dimensional spaces can be represented by a matrix $A$ acting by $T(x) = Ax$ once
a basis is fixed for each space.

## Why this node exists

Preserving structure, not merely mapping points, is what distinguishes a linear transformation
from an arbitrary function between vector spaces, and it is that preserved structure that lets
a transformation be represented and computed with a matrix at all. The matrix representation of
a linear transformation needs this node next, since choosing a basis is the step that turns the
abstract preservation property this node states into the concrete array of numbers a
calculation actually uses.
