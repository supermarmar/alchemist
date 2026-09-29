---
id: group-homomorphism-and-quotient-structure
title: Group homomorphism and quotient structure
domains: [maths]
status: drafted
requires: [group-theory-fundamentals]
spends: []
anchor: [up.wtw381.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A group homomorphism is a map between two groups that preserves the group operation, so the
image of a product equals the product of the images. It is degenerate where every element maps
to the identity of the target group, the trivial homomorphism, which preserves the operation
vacuously.

## The expression

$$
\varphi(a \cdot b) = \varphi(a) *_H \varphi(b), \qquad G / \ker\varphi \cong \operatorname{im}\varphi
$$

Here $\varphi$ is the homomorphism, $G$ is its source group with operation $\cdot$, $H$ is its
target group with operation $*_H$, and $a$ and $b$ are arbitrary elements of $G$. The second
equation is the first isomorphism theorem: $\ker\varphi$, the elements $\varphi$ sends to the
identity, is a normal subgroup of $G$, and the quotient group $G/\ker\varphi$ it defines is
isomorphic to $\varphi$'s image inside $H$.

## Why this node exists

A quotient structure lets a large group be studied through a smaller one built by collapsing a
normal subgroup to a point, and the first isomorphism theorem is what guarantees that collapse
always recovers a group a homomorphism was already mapping to. Consequently every classification
of a group up to isomorphism proceeds by naming its homomorphisms and reading off the quotients
they induce.
