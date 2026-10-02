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
point on the plane is perpendicular to a given normal vector.

## The expression

$$
\mathbf{n} \cdot (\mathbf{r} - \mathbf{a}) = 0
$$

Here $\mathbf{a}$ is the position vector of a known point on the plane, $\mathbf{n}$ is a
vector normal to the plane, and $\mathbf{r}$ is the position vector of a general point,
which satisfies the equation exactly when it lies on the plane. A line through the point $\mathbf{a}$ in a direction $\mathbf{d}$ is written instead in
parametric form, $\mathbf{r} = \mathbf{a} + t\mathbf{d}$ for scalar parameter $t$, and can
equally be recovered as the intersection of two planes, each satisfying an equation of this
form with its own normal.

## Why this node exists

A displacement, a velocity, or a factor loading is written as a vector from the moment it
is introduced, and the geometry of the space that vector sits in has to be fixed before a
curve traced out by a varying vector can be described. Vector functions and quadratic
curves need it next.
