---
id: field-extension
title: Field extension
domains: [maths]
status: drafted
requires: [ring-theory-fundamentals]
spends: []
anchor: [up.wtw381.3, up.wtw381.4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A field extension $L/K$ enlarges a field $K$ to a larger field $L$ containing it, most often
built by adjoining a root of a polynomial that has no root in $K$ itself.

## The expression

$$
[L : K] = \dim_K L
$$

Here $L/K$ is the extension, and $[L:K]$, its degree, is the dimension of $L$ as a vector
space over $K$. Where a single element $\alpha$ is adjoined to give $L = K(\alpha)$ and
$\alpha$ satisfies an irreducible polynomial of degree $n$ over $K$, the degree of the
extension is exactly $n$, since $1, \alpha, \dots, \alpha^{n-1}$ form a basis for $L$ over
$K$.

## Why this node exists

Ring theory supplies the algebraic structure a field needs, but it says nothing about how one
field can sit inside another or how large that containment is, and the degree of an extension
is what makes that size precise and computable. A length is constructible by straight edge
and compass only where the degree of the field extension it generates is a power of two,
which is the classical application that field extension theory was developed to settle.
