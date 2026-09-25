---
id: numerical-linear-system-solution
title: Numerical linear system solution
domains: [data-eng, maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw123.4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Numerical linear system solution finds the vector satisfying a system of linear equations by an
algorithm suited to running on a computer, in place of algebraic elimination carried out by
hand.

## The expression

$$
x^{(k+1)} = D^{-1}\bigl(b - (L + U) x^{(k)}\bigr)
$$

Here $A = D + L + U$ splits the coefficient matrix into its diagonal $D$, strictly lower
triangular part $L$ and strictly upper triangular part $U$, $b$ is the right-hand side of the
system $Ax = b$, and $x^{(k)}$ is the approximate solution at iteration $k$. This Jacobi
iteration updates every component of $x$ from the previous iterate alone, and it converges to
the true solution wherever $A$ is diagonally dominant.

## Why this node exists

A system with thousands of unknowns, the kind a discretised partial differential equation or a
large regression problem produces, is too large for elimination by hand and too costly for
exact elimination to remain the fastest computational route. An iterative scheme trades an
exact answer for one refined to any required tolerance at a fraction of the cost. Direct methods
for linear systems needs this node next, since it sets the elimination-based alternative against
the iterative approach introduced here.
