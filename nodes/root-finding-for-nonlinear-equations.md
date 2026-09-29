---
id: root-finding-for-nonlinear-equations
title: Root-finding for non-linear equations
domains: [data-eng, maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw123.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Root-finding locates a value at which a non-linear equation is satisfied by
iterating a sequence of approximations that converges towards it, since a
non-linear equation generally admits no closed-form solution. The method stops
once successive approximations differ by less than a chosen tolerance.

## The expression

$$
f(x^*) = 0
$$

Here $f$ is the function whose root is wanted and $x^*$ is the value at which it
vanishes. An iterative method produces a sequence $x_0, x_1, x_2, \ldots$ intended
to converge to $x^*$, each term built from the one before it by a rule specific to
the method chosen.

## Why this node exists

An actuarial or credit model regularly needs the input that makes an equation
balance, such as the yield that equates a bond's price to its discounted cashflows,
and no closed-form formula supplies that input in general. Iterative methods for
non-linear equations needs this node next, since a system of several such
equations is solved by extending exactly this single-equation idea.
