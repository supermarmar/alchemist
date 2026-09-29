---
id: numerical-methods-for-initial-value-problems
title: Numerical methods for initial value problems
domains: [data-eng, maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw123.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Numerical methods for initial value problems step a differential equation forward from a known
starting value, approximating a solution where none can be written down in closed form.

## The expression

$$
y_{n+1} = y_n + h\, f(t_n, y_n)
$$

Here $y_n$ is the approximate solution at time $t_n$, $h$ is the step size carrying the
approximation from $t_n$ to $t_{n+1} = t_n + h$, and $f(t_n, y_n)$ is the right-hand side of the
differential equation $y' = f(t, y)$ evaluated at the current point. This is Euler's method, the
simplest such scheme, and it advances the solution by assuming the rate of change stays constant
over each step of width $h$.

## Why this node exists

A differential equation with no closed-form solution still needs a number to evaluate a model
against, and stepping forward from the known initial value is the only way to produce one
without an exact formula. Consequently, every model whose dynamics are stated as a rate of
change rather than as an explicit function of time depends on a scheme of this kind to turn that
rate into a usable trajectory.
