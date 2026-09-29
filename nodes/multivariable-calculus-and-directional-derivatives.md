---
id: multivariable-calculus-and-directional-derivatives
title: Multivariable calculus and directional derivatives
domains: [maths]
status: drafted
requires: [differential-calculus-of-single-variable-functions]
spends: []
anchor: [up.wtw218.1, up.wtw218.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The directional derivative of a function of several variables measures its
instantaneous rate of change along a chosen direction, generalising the ordinary
derivative beyond movement along a single coordinate axis.

## The expression

$$
D_{\mathbf{u}} f(\mathbf{x}) = \nabla f(\mathbf{x}) \cdot \mathbf{u}
$$

Here $f$ is the function, $\mathbf{x}$ is the point at which the rate of change is
measured, $\mathbf{u}$ is a unit vector fixing the direction, and $\nabla f$ is the
gradient of $f$, the vector of its partial derivatives.

## Why this node exists

A function of one variable has a single rate of change at each point, but a function
of several variables has a different rate of change in every direction, and the
gradient's dot product with a direction is what recovers a single number from that
whole family. Lagrange multipliers needs it next, since the condition that a
constrained optimum satisfies is stated in exactly this gradient language.
