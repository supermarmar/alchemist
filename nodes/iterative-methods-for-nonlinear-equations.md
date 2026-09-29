---
id: iterative-methods-for-nonlinear-equations
title: Iterative methods for non-linear equations
domains: [data-eng, maths]
status: drafted
requires: [root-finding-for-nonlinear-equations]
spends: []
anchor: [up.wtw383.4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

This node extends root-finding to a system of several non-linear equations solved
simultaneously, iterating an approximation vector towards the point at which every equation in
the system holds at once. It is degenerate where the system is linear, at which point a single
matrix solve replaces the iteration entirely.

## The expression

$$
\mathbf{x}^{(k+1)} = \mathbf{x}^{(k)} - J\bigl(\mathbf{x}^{(k)}\bigr)^{-1} \mathbf{f}\bigl(\mathbf{x}^{(k)}\bigr)
$$

Here $\mathbf{f}$ is the vector of equations the system requires to vanish simultaneously,
$\mathbf{x}^{(k)}$ is the $k$-th approximation to the solution, and $J\bigl(\mathbf{x}^{(k)}\bigr)$
is the Jacobian matrix of $\mathbf{f}$ evaluated there, this being Newton's method extended from
a single equation to a system.

## Why this node exists

A model calibrated against several market prices or several moment conditions at once needs its
parameters solved for as a system, since fixing one equation at a time would leave the others
unsatisfied. Introduction to numerical optimisation needs it next, since minimising a function
by setting its gradient to zero is itself a system of non-linear equations solved the same
iterative way.
