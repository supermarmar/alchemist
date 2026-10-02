---
id: matrix-algebra-and-linear-systems
title: Matrix algebra and linear systems
domains: [maths]
status: drafted
requires: [vector-space-rn]
spends: []
anchor: [up.wtw124.3, up.wtw124.4, up.wtw211.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Matrix algebra defines addition, scalar multiplication and multiplication on rectangular
arrays of numbers, and a system of linear equations is written compactly as one matrix
equation once those operations are fixed.

## The expression

$$
A\mathbf{x} = \mathbf{b}
$$

Here $A$ is an $m \times n$ matrix of coefficients, $\mathbf{x}$ is the $n$-vector of unknowns,
and $\mathbf{b}$ is the $m$-vector of right-hand-side values, so that each row of the matrix
equation reproduces one equation of the original system. The system has a unique solution
$\mathbf{x} = A^{-1}\mathbf{b}$ exactly where $A$ is square and invertible, and no solution or
infinitely many otherwise.

## Why this node exists

A system of several linear equations solved one at a time by substitution becomes
unmanageable as the number of equations grows, and matrix notation is what lets the whole
system be manipulated as a single object instead. Every later linear-algebra construction,
from a determinant to an eigenvalue, is defined on the matrix this node introduces. Linear
combinations and span needs this node next, reading the columns of $A$ as the vectors whose
combinations decide whether the system has a solution at all.
