---
id: numerical-integration
title: Numerical integration
domains: [data-eng, maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw123.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Numerical integration approximates a definite integral by evaluating the integrand at a finite
set of points, for use where no closed-form antiderivative exists or where one is too costly to
find.

## The expression

$$
\int_a^b f(x)\,dx \approx \frac{h}{2}\left(f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n)\right)
$$

Here $f$ is the integrand, $a$ and $b$ are the limits of integration, $n$ is the number of
subintervals the range $[a,b]$ is divided into, $h = (b-a)/n$ is the width of each subinterval,
and $x_0, \dots, x_n$ are the equally spaced grid points at which $f$ is evaluated. This
trapezoidal rule approximates the area under $f$ on each subinterval by a trapezium rather than
a rectangle, which halves the error for the same number of evaluations.

## Why this node exists

Many integrals that arise from a model, a discounted cash flow with a rate that varies
continuously, or a likelihood with no closed form, cannot be evaluated symbolically at all.
Numerical integration replaces the exact area with a sum a computer can evaluate to any
required accuracy by refining the grid, and every later scheme for solving a differential
equation numerically depends on being able to approximate an integral in exactly this way.
