---
id: direct-methods-for-linear-systems
title: Direct methods for linear systems
domains: [data-eng, maths]
status: drafted
requires: [numerical-linear-system-solution]
spends: []
anchor: [up.wtw383.1, up.wtw383.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A direct method solves a system of linear equations exactly, in a fixed number of arithmetic
steps determined in advance by the size of the system, by factorising the coefficient matrix
into triangular pieces and then solving each piece by substitution.

## The expression

$$
A = LU, \qquad Ly = b, \qquad Ux = y
$$

Here $A$ is the coefficient matrix of the system $Ax = b$, $L$ is a lower triangular matrix and
$U$ an upper triangular matrix whose product recovers $A$, $b$ is the right-hand side, $y$ is an
intermediate vector solved for by forward substitution through $L$, and $x$ is the system's
solution, recovered by back substitution through $U$.

## Why this node exists

Gaussian elimination and this factorisation are the same arithmetic, and stating the
factorisation once means it never has to be redone for a second right-hand side sharing the same
$A$, since only the two substitutions need repeating. Iterative methods for linear systems and
eigenvalue problems needs it next, since it is measured against this exact, finite-step solve as
the alternative that trades exactness for speed on a system too large to factorise.
