---
id: integration-techniques
title: Integration techniques
domains: [maths]
status: drafted
requires: [definite-and-indefinite-integrals]
spends: []
anchor: [up.wtw124.7]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Beyond substitution, an integral whose integrand is a product of two functions, or a rational
function whose denominator factorises, is evaluated by two further standard techniques:
integration by parts, and decomposition into partial fractions.

## The expression

$$
\int u\, \mathrm{d}v = uv - \int v\, \mathrm{d}u
$$

$$
\frac{p(x)}{(x - a)(x - b)} = \frac{A}{x - a} + \frac{B}{x - b}
$$

In the first identity, $u$ and $v$ are the two functions chosen from the product forming the
integrand, with $\mathrm{d}v$ integrated to $v$ and $u$ differentiated to $\mathrm{d}u$; the
identity trades the original integral for one built from $v\,\mathrm{d}u$, chosen to be
simpler than $u\,\mathrm{d}v$. In the second, $p(x)$ is a polynomial of lower degree than the
denominator, $a$ and $b$ are the denominator's distinct roots, and $A$ and $B$ are constants
found by matching coefficients, after which each term on the right integrates to a logarithm
directly.

## Why this node exists

A product of two unrelated functions, or a rational function with a factorable denominator,
matches none of the basic antiderivative forms and resists substitution as well, since neither
factor is the derivative of the other. Integration by parts and partial fractions supply the
two remaining standard routes to a closed-form antiderivative, and together with substitution
they cover the integrals the corpus needs evaluated in closed form.
