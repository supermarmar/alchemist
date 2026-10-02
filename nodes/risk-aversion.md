---
id: risk-aversion
title: Risk aversion
domains: [eco]
status: drafted
requires: [utility-function]
spends: []
anchor: [ifoa.cm2.1.2-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An investor is risk averse where their utility function is concave in wealth, risk neutral
where it is linear, and risk seeking where it is convex. The Arrow-Pratt coefficients measure
the strength of that curvature and how it changes as wealth itself changes.

## The expression

$$
A(W) = -\frac{U''(W)}{U'(W)}, \qquad R(W) = W \, A(W)
$$

Here $U(W)$ is the utility function, $U'(W)$ and $U''(W)$ are its first and second derivatives
with respect to wealth $W$, $A(W)$ is the coefficient of absolute risk aversion, and $R(W)$ is
the coefficient of relative risk aversion, absolute risk aversion scaled by wealth itself. A
positive $A(W)$ that falls as $W$ rises describes an investor who holds a growing pound amount
in risky assets as they become wealthier, decreasing absolute risk aversion.

## Why this node exists

A utility function alone says only that an investor prefers more wealth to less and is averse
to risk in general, without saying by how much or whether that aversion changes with wealth.
Common utility functions need this node next, since each one is chosen precisely for the shape
of absolute or relative risk aversion it produces.
