---
id: ring-theory-fundamentals
title: Ring theory fundamentals
domains: [maths]
status: drafted
requires: [group-theory-fundamentals]
spends: []
anchor: [up.wtw381.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A ring is a set with two binary operations, addition and multiplication, such that the set is
an abelian group under addition, multiplication is associative, and multiplication distributes
over addition on both sides. An ideal is a subset closed under addition that absorbs
multiplication by any ring element, and it is the object a ring homomorphism's kernel always is.

## The expression

$$
a \cdot (b + c) = a \cdot b + a \cdot c, \qquad (a + b) \cdot c = a \cdot c + b \cdot c
$$

Here $a$, $b$ and $c$ are elements of the ring, $+$ is the addition under which the ring is an
abelian group, and $\cdot$ is the multiplication that need not commute and need not admit an
inverse. The two distributive laws are what tie the two operations together, making the ring's
addition and multiplication one coherent structure built on a shared set.

## Why this node exists

A group carries a single operation, so it cannot describe a structure in which two elements are
both added and multiplied consistently, the pattern every number system and every matrix algebra
in this corpus actually has. Ring theory fundamentals generalises group theory to exactly that
case, and field extension needs it next, since a field extension is built by asking which
elements a ring's multiplication lets an element be inverted against.
