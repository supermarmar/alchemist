---
id: probability-measure
title: Probability measure
domains: [maths, stats]
status: drafted
requires: [probability-theory-foundations]
spends: []
anchor: [up.wst211.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A probability measure is the function that assigns a number to every event in a sample space,
consistent with the axioms the previous node fixes. Together with the sample space and the
collection of events it is defined on, it forms a probability space, the single formal object
every later probability statement in this corpus is made against.

## The expression

$$
P : \mathcal{F} \to [0,1], \qquad P(\Omega) = 1
$$

Here $\Omega$ is the sample space of possible outcomes, $\mathcal{F}$ is the collection of
events the measure is defined on, and $P$ is the probability measure itself, a function taking
each event in $\mathcal{F}$ to a number between zero and one, with the certain event $\Omega$
assigned probability one.

## Why this node exists

Every quantity built downstream, from a random variable's distribution to a conditional
probability, is defined by referring back to this one function, so a statement that omits which
measure it is taken under is not yet a fully specified probability statement.
