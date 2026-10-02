---
id: linear-combinations-and-span
title: Linear combinations and span
domains: [maths]
status: drafted
requires: [matrix-algebra-and-linear-systems]
spends: []
anchor: [up.wtw211.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A linear combination of a set of vectors is a new vector formed by scaling each one and adding
the results, and the span of that set is the collection of every vector reachable that way.

## The expression

$$
v = c_1 v_1 + c_2 v_2 + \cdots + c_n v_n, \qquad \mathrm{span}\{v_1, \dots, v_n\} = \{\, c_1 v_1 + \cdots + c_n v_n : c_1, \dots, c_n \in \mathbb{R} \,\}
$$

Here $v_1, \dots, v_n$ are the given vectors, $c_1, \dots, c_n$ are the scalar coefficients
chosen for each one, $v$ is the resulting linear combination, and $\mathrm{span}\{v_1, \dots,
v_n\}$ is the set of every vector obtainable by choosing some coefficients $c_1, \dots, c_n$.

## Why this node exists

A system of linear equations either has a solution or does not, and whether it does depends on
whether the equations' right-hand side sits inside the set of vectors the coefficient
columns can jointly reach. Span names that reachable set directly, which is what turns the
question of solvability into a question about set membership. Linear independence needs it
next, since it asks whether every vector in that set is reached by only one combination of
coefficients or by many.
