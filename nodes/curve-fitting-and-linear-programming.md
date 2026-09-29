---
id: curve-fitting-and-linear-programming
title: Curve fitting and linear programming
domains: [data-eng, maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw152.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Curve fitting chooses the parameters of a function so that its predicted values are as
close as possible to a set of observed data points, most often by minimising the sum
of squared errors between the two; linear programming instead chooses a set of
decision variables to optimise a linear objective subject to linear constraints.

## The expression

$$
\min_{\beta} \sum_{i=1}^{n} \bigl(y_i - f(x_i; \beta)\bigr)^2
$$

$$
\max_{x} \; c^{\mathsf T}x \quad \text{subject to } Ax \le b,\; x \ge 0
$$

Here, in the fitting problem, $y_i$ is the $i$th observed value, $f(x_i;\beta)$ is the
fitted function evaluated at $x_i$ with parameters $\beta$, and the sum runs over the
$n$ observed points; in the linear programme, $x$ is the vector of decision variables,
$c$ is the vector of objective coefficients, and $A$ and $b$ define the constraints
$x$ must satisfy.

## Why this node exists

A model with unfitted parameters makes no prediction, and a resource allocation with
no stated objective and no stated constraints has no basis for preferring one
allocation over another. Curve fitting and linear programming are the two most basic
tools this corpus has for turning a functional form and a set of resource limits into
a single chosen answer, and both recur throughout the branches that follow wherever a
parameter needs fitting to data or a limited resource needs allocating optimally.
