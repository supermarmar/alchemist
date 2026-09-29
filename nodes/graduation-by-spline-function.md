---
id: graduation-by-spline-function
title: Graduation by spline function
domains: [life]
status: drafted
requires: [graduation-rationale]
spends: []
anchor: [ifoa.cs2.4.5-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Graduation by spline function fits a piecewise polynomial through the crude mortality data,
with the degree of smoothing controlled by a separate penalty rather than by the choice of a
particular mortality law. It is degenerate wherever the penalty is driven to zero, at which
point the graduated curve simply interpolates the crude rates and no smoothing has occurred.

## The expression

$$
\sum_i w_i \bigl(q_i - g(x_i)\bigr)^2 + \lambda \int g''(x)^2 \, dx
$$

Here $q_i$ is the crude rate observed at age $x_i$, $w_i$ is the weight given to that
observation, $g$ is the fitted spline evaluated at $x_i$, and $\lambda$ is the smoothing
parameter that trades fidelity to the crude data against the curvature penalty $\int
g''(x)^2\,dx$. The graduated rates are the values of $g$ that minimise this sum, chosen once
$\lambda$ has been set.

## Why this node exists

Separating the smoothing decision from the choice of a mortality law lets the fitted curve
follow a shape no single formula would produce, at the cost of an explicit smoothing choice that
a parametric fit never has to make. That explicit choice is what a graduator must justify
directly, since nothing in the spline itself picks $\lambda$ the way a law's functional form
constrains a parametric fit.
