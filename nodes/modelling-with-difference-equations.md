---
id: modelling-with-difference-equations
title: Modelling with difference equations
domains: [data-eng, maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw152.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A difference equation models a dynamical process by relating the value of a sequence at one
time step to its values at earlier steps. It is the discrete-time counterpart of a
differential equation, and it has no fixed value until an initial condition pins down the
constant the general solution otherwise leaves free.

## The expression

$$
y_{n+1} = a y_n + b
$$

Here $y_n$ is the value of the sequence at step $n$, $a$ is the constant multiplier carrying
one step's value into the next, and $b$ is a constant term added at every step regardless of
$y_n$. Setting $b = 0$ gives the pure geometric recursion $y_{n+1} = a y_n$, whose solution
$y_n = a^n y_0$ decays where $|a| \lt 1$ and grows where $|a| \gt 1$.

## Why this node exists

A process that only updates at discrete points, a cohort maturing month by month or a reserve
compounding annually, cannot be described by a rate of change with no gap between
observations. A difference equation supplies the update rule that a differential equation
cannot: given today's value, it states tomorrow's directly. Consequently, any numerical scheme
that steps a model forward one period at a time is solving a difference equation, whether or
not it is written as one.
