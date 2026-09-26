---
id: cauchy-riemann-equations
title: Cauchy-Riemann equations
domains: [maths]
status: drafted
requires: [complex-functions]
spends: []
anchor: [up.wtw320.4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Cauchy-Riemann equations are the pair of partial differential equations a complex
function's real and imaginary parts must satisfy at a point for the function to be
differentiable there in the complex sense, a condition far stronger than differentiability of
either part as a real function of two variables.

## The expression

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad
\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$

Here $f(z) = u(x, y) + i \, v(x, y)$ is a complex function of $z = x + iy$, $u$ is its real
part and $v$ its imaginary part, both functions of the real variables $x$ and $y$. The two
equations must both hold at a point, and the partial derivatives involved must be continuous
there, for $f$ to be complex differentiable at that point.

## Why this node exists

A real function's derivative only has to agree along the real line, but a complex function's
derivative has to agree along every direction of approach in the plane, and these equations
are the algebraic test that a candidate derivative actually does. Cauchy's integral theorem
needs a function known to be differentiable everywhere inside a region before it can say
anything about integrating that function around a closed contour in the region.
