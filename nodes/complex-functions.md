---
id: complex-functions
title: Complex functions
domains: [maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw320.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A complex function maps a subset of the complex plane to the complex plane, and it is differentiable at a point when the difference quotient defining its derivative tends to the same limit regardless of the direction from which the increment approaches zero, a far stronger requirement than differentiability of a function of one real variable.

## The expression

$$
f'(z_0) = \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h}
$$

Here $f'(z_0)$ is the complex derivative at $z_0$, $f(z_0)$ is the function's value there, and $h$ is the complex increment, which may approach zero from any direction in the plane rather than along a single real axis.

## Why this node exists

Testing the limit directly along every possible direction of approach is impractical, and the Cauchy-Riemann equations node needs it next, turning that directional requirement into two ordinary partial derivative conditions that can be checked directly.
