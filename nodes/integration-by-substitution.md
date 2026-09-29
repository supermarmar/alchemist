---
id: integration-by-substitution
title: Integration by substitution
domains: [maths]
status: drafted
requires: [definite-and-indefinite-integrals]
spends: []
anchor: [up.wtw114.11]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Integration by substitution rewrites an integral whose integrand is a composite function in
terms of a new variable set equal to the inner function, turning the integral into one that
the basic rules can evaluate directly.

## The expression

$$
\int f\bigl(g(x)\bigr)\, g'(x)\, \mathrm{d}x = \int f(u)\, \mathrm{d}u, \qquad u = g(x)
$$

Here $g(x)$ is the inner function chosen as the substitution, $f$ is the outer function the
integrand applies to $g(x)$, $g'(x)$ is $g$'s derivative, and $u$ is the new variable that
replaces $g(x)$ once $\mathrm{d}u = g'(x)\,\mathrm{d}x$ is substituted in. The right-hand side
is evaluated in $u$, and the substitution $u = g(x)$ is then reversed to express the result
back in terms of $x$.

## Why this node exists

A composite integrand rarely matches any of the standard antiderivative forms directly, and
without a way to change variables an integral of that shape resists the basic rules
altogether. Substitution supplies that change of variable, turning an integral built around an
unfamiliar composite function into one built around $u$ alone, which the standard rules can
then evaluate.
