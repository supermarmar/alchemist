---
id: numerical-optimisation-introduction
title: Introduction to numerical optimisation
domains: [data-eng, maths]
status: drafted
requires: [iterative-methods-for-nonlinear-equations]
spends: []
anchor: [up.wtw383.5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Numerical optimisation finds the input that minimises, or maximises, a function by
iterating from a starting point toward a stationary point, reusing the same iterative
machinery built for solving non-linear equations, applied now to the equation that
sets the function's gradient to zero.

## The expression

$$
x_{n+1} = x_n - \alpha \nabla f(x_n)
$$

Here $x_n$ is the current iterate, $\nabla f(x_n)$ is the gradient of the objective
function at that iterate, $\alpha$ is a step size, and $x_{n+1}$ is the next iterate,
moved against the gradient toward a lower function value.

## Why this node exists

Most models in the corpus have no closed-form solution, and every one of them,
from a generalised linear model's likelihood to a network's loss, is fitted by
driving a gradient to zero by iteration, so this node is the shared machinery every
one of those fits calls on beneath its own name.
