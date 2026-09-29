---
id: vector-functions-and-quadratic-curves
title: Vector functions and quadratic curves
domains: [maths]
status: drafted
requires: [vector-algebra-lines-and-planes]
spends: []
anchor: [up.wtw124.10]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A vector function traces a curve in space by mapping a single scalar parameter to a position
vector, and a quadratic curve is the set of points in the plane satisfying a second-degree
equation in two variables, whose coefficients determine whether the curve is an ellipse, a
parabola, or a hyperbola.

## The expression

$$
\mathbf{r}(t) = \bigl(x(t),\, y(t),\, z(t)\bigr)
$$

$$
Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0
$$

Here $\mathbf r(t)$ is the position vector at parameter $t$, and $x(t)$, $y(t)$, and $z(t)$ are
its coordinate functions, each tracing the curve's motion along one axis as $t$ varies. In the
second display, $A$, $B$, $C$, $D$, $E$, and $F$ are the equation's fixed coefficients, and the
sign of the discriminant $B^2 - 4AC$ classifies the curve as an ellipse when negative, a
parabola when zero, and a hyperbola when positive.

## Why this node exists

A line or a plane, the two objects the prerequisite fixes, moves along a direction that never
changes, so neither can describe a path that bends or a boundary that curves back on itself.
Vector functions and quadratic curves extend that straight-line geometry to genuinely curved
objects, one by letting position vary continuously with a parameter and the other by letting
the defining equation carry a squared term. Later work on conics and on parametrised motion
draws on whichever of the two it needs.
