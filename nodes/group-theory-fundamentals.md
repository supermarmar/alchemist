---
id: group-theory-fundamentals
title: Group theory fundamentals
domains: [maths]
status: drafted
requires: []
spends: []
anchor: [up.wtw381.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A group is a set together with a binary operation that combines any two elements
to form a third, satisfying closure, associativity, an identity element, and an
inverse for every element. The definition places no restriction on commutativity,
which is why a group whose operation does commute is given the separate name
abelian.

## The expression

$$
\forall\, a, b, c \in G:\ (a \cdot b) \cdot c = a \cdot (b \cdot c), \qquad
\exists\, e \in G,\ \forall\, a \in G: e \cdot a = a \cdot e = a, \qquad
\forall\, a \in G,\ \exists\, a^{-1} \in G: a \cdot a^{-1} = a^{-1} \cdot a = e
$$

Here $G$ is the underlying set, $\cdot$ is the group operation, $e$ is the
identity element, and $a^{-1}$ is the inverse of $a$. Closure, that $a \cdot b$
itself lies in $G$ for every $a$ and $b$, is built in by writing the operation as
a map from $G \times G$ back into $G$.

## Why this node exists

Every richer algebraic structure in this corpus, from a ring's second operation
to a vector space's scalars, is built by adding axioms on top of this one, and the
notions of subgroup and the order of an element let a large group be studied
through smaller pieces it contains. Group homomorphism and quotient structure
needs it next, since a homomorphism is a map required to respect exactly the
operation this node defines.
