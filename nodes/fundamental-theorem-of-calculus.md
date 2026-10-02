---
id: fundamental-theorem-of-calculus
title: Fundamental theorem of calculus
domains: [maths]
status: drafted
requires: [definite-and-indefinite-integrals]
spends: []
anchor: [up.wtw124.9]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The fundamental theorem of calculus links differentiation and integration, showing that
integrating a function's derivative over an interval recovers the change in the function
across that interval.

## The expression

$$
\int_a^b f'(x) \, dx = f(b) - f(a)
$$

Here $f$ is a function differentiable on an interval containing $[a, b]$, $f'$ is its
derivative, and the left-hand side is the definite integral of that derivative from $a$ to
$b$. Equivalently, defining $F(x) = \int_a^x f(t)\,dt$ makes $F$ an antiderivative of $f$, so
integration and differentiation are inverse operations of each other.

## Why this node exists

Definite and indefinite integrals are introduced as two separate objects, an area under a
curve and a family of antiderivatives differing by a constant, and nothing so far connects
them. The fundamental theorem is what identifies the two, since it shows that computing an
area reduces to finding any one antiderivative and evaluating it at the interval's endpoints,
which is what makes most of the integrals used elsewhere in the corpus computable at all.
