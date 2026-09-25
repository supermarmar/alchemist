---
id: complex-numbers-and-polynomial-factorisation
title: Complex numbers and polynomial factorisation
domains: [maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw124.6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A complex number extends the real numbers by adjoining $i$, a root of $i^2 = -1$, so
that every polynomial with real or complex coefficients acquires as many roots as its
degree once complex values are allowed.

## The expression

$$
p(z) = a_n \prod_{k=1}^{n} (z - z_k)
$$

Here $p$ is a polynomial of degree $n$ with leading coefficient $a_n$, $z$ is the
complex variable, and $z_1,\ldots,z_n$ are its roots, counted with multiplicity,
whose existence as complex numbers is what the fundamental theorem of algebra
guarantees.

## Why this node exists

A real polynomial can fail to factorise into real linear factors, since a quadratic
with negative discriminant has no real root, and calculus built only on the reals then
has to treat that failure as a standing exception. Adjoining $i$ removes the
exception, so every polynomial factorises completely, and the polynomial ring and
factorisation needs that guarantee next.
