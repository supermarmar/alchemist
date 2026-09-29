---
id: permutation-group
title: Permutation group
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

A permutation group is a group whose elements are the bijections of a finite set to itself,
called permutations, with the group operation given by composing two permutations in turn. The
symmetric group on $n$ elements collects every permutation of that set, and Cayley's theorem
states that every finite group is isomorphic to a subgroup of some symmetric group, so a
permutation group is not a special case but the structure every finite group reduces to.

## The expression

$$
|S_n| = n!
$$

Here $S_n$ is the symmetric group on a set of $n$ elements, and $|S_n|$ is its order, the number
of distinct permutations of $n$ objects, counted by choosing where each of the $n$ elements is
sent in turn.

## Why this node exists

A finite group given only abstractly, by a multiplication table or a presentation, becomes
something that can be visualised and computed with once it is realised as permutations acting on
a concrete set, which is the route Cayley's theorem opens and representation theory later builds
on.
