---
id: numerical-error-and-convergence
title: Numerical error and convergence
domains: [data-eng, maths]
status: drafted
requires: [root-finding-for-nonlinear-equations]
spends: []
anchor: [up.wtw123.5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Numerical error and convergence analysis bounds the gap between a numerical method's
approximation and the true solution, and characterises how quickly that gap shrinks as the
method's iterations or its discretisation are refined.

## The expression

$$
|x_{n+1} - x^*| \le C |x_n - x^*|^p
$$

Here $x_n$ is the method's approximation at iteration $n$, $x^*$ is the true solution the
method is converging towards, $C$ is a constant bounding how the error contracts from one
iteration to the next, and $p$ is the order of convergence: $p=1$ is linear convergence, where
the error shrinks by roughly a fixed factor each step, and $p=2$ is quadratic convergence,
where the number of correct digits roughly doubles each step.

## Why this node exists

Root-finding, and every iterative method built on it, produces only an approximation, so a
result is unusable until something says how far that approximation can be trusted to lie from
the true answer and how many iterations are needed to bring it within a stated tolerance. The
order $p$ is what distinguishes a method worth the extra computation per step, such as
Newton's method, from a slower method that is simpler to implement, and it is what lets a
stopping rule be set with a known error bound.
