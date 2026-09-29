---
id: probability-theory-foundations
title: Probability theory foundations
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [up.wst111.7]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Probability theory rests on a small set of axioms fixing what any assignment of
probabilities to events must satisfy: every event has a non-negative
probability, the certain event has probability one, and the probability of a
union of mutually exclusive events is the sum of their separate probabilities.

## The expression

$$
P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i), \qquad A_i \cap A_j = \varnothing \text{ for } i \ne j
$$

Here $A_1, A_2, \dots$ is a countable sequence of mutually exclusive events, and
the axiom of countable additivity states that the probability of their union
equals the sum of their individual probabilities; together with non-negativity
and $P(\Omega) = 1$, it is one of Kolmogorov's three axioms.

## Why this node exists

Every rule the corpus uses for combining probabilities, from the addition rule
for overlapping events to conditioning itself, is a consequence of these three
axioms rather than a separate assumption. The probability measure needs this
node next, giving the axioms a single formal object to attach to.
