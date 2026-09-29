---
id: vector-algebra-lines-and-planes
title: 'Vector algebra: lines and planes'
domains: [maths]
status: drafted
requires: [vector-space-rn]
spends: []
anchor: [up.wtw124.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A plane in three-dimensional space is the set of points whose displacement from a fixed
point on the plane is perpendicular to a given normal vector; the definition degenerates
to a line where the normal vector is instead fixed to be perpendicular to two given
directions rather than one.

## The expression

$$
\mathbf{n} \cdot (\mathbf{r} - \mathbf{a}) = 0
$$

Here $\mathbf{a}$ is the position vector of a known point on the plane, $\mathbf{n}$ is a
vector normal to the plane, and $\mathbf{r}$ is the position vector of a general point,
which satisfies the equation exactly when it lies on the plane. The same dot product
underlies the line's own vector equation, $\mathbf{r} = \mathbf{a} + t\mathbf{d}$ for a
direction $\mathbf{d}$ and scalar parameter $t$, since a line is the intersection of two
such planes.

## Why this node exists

A displacement, a velocity or a factor loading is written as a vector from the moment it
is introduced, and the geometry of the space that vector sits in has to be fixed before a
curve traced out by a varying vector can be described. Vector functions and quadratic
curves need it next.
