---
id: power-series-and-convergence
title: Power series and convergence
domains: [maths]
status: drafted
requires: [sequences-and-series]
spends: []
anchor: [up.wtw220.3, up.wtw320.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A power series represents a function as an infinite sum of terms in increasing
integer powers of a variable, centred on a fixed point, and it converges absolutely
inside a radius of convergence around that point and diverges beyond it, with its
behaviour exactly on the boundary requiring separate checking.

## The expression

$$
\sum_{n=0}^{\infty} a_n (x - c)^n, \qquad R = \lim_{n \to \infty}
\left| \frac{a_n}{a_{n+1}} \right|
$$

Here $a_n$ is the coefficient of the $n$th term, $c$ is the centre of the series,
$x$ is the point at which it is evaluated, and $R$ is the radius of convergence,
found here from the ratio of consecutive coefficients.

## Why this node exists

A function that is infinitely differentiable at a point can be rebuilt from nothing
but the derivatives at that one point, and a power series, specifically a Taylor
series, is the vehicle that reconstruction takes. Fourier analysis and series needs
it next, representing a function instead as a sum of trigonometric terms once the
function is periodic rather than merely smooth.
