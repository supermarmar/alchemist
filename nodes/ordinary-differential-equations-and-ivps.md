---
id: ordinary-differential-equations-and-ivps
title: Ordinary differential equations and initial value problems
domains: [maths]
status: drafted
requires: [definite-and-indefinite-integrals]
spends: []
anchor: [up.wtw264.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An ordinary differential equation relates a function to its own derivatives, and an
initial value problem pairs that equation with the function's value at a starting
point, fixing the one solution out of the equation's whole family that passes through
it.

## The expression

$$
\frac{dy}{dx} + p(x) y = q(x), \qquad y(x_0) = y_0
$$

Here $y$ is the unknown function, $p(x)$ and $q(x)$ are known functions of $x$, and
$y(x_0) = y_0$ is the initial condition; multiplying through by the integrating
factor $e^{\int p(x)\,dx}$ reduces the left-hand side to the derivative of a single
product and makes the equation directly integrable.

## Why this node exists

A quantity whose rate of change is known is described by a differential equation long
before it is described by a closed-form function of time. An interest-bearing balance and a
decaying reserve are two examples, and solving the equation is what recovers that closed
form. Laplace transform needs it next, turning the same differential equation
into an algebraic one before transforming the solution back.
