---
id: bayes-theorem
title: Bayes' theorem
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.5.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Bayes' theorem gives the conditional probability of a hypothesis given evidence in terms of the reverse conditional probability of the evidence given the hypothesis, together with the marginal probabilities of each. It is a rearrangement of the multiplication rule rather than a separate assumption, so it holds wherever the conditioning event has positive probability.

## The expression

$$
P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B)}, \qquad P(B) > 0
$$

Here $P(A \mid B)$ is the probability of $A$ once $B$ is known, $P(B \mid A)$ is the reverse conditional probability, $P(A)$ is the marginal probability of $A$ before $B$ is observed, and $P(B)$ is the marginal probability of $B$ across every way it can occur.

## Why this node exists

Evidence almost always arrives the wrong way round: a test result is easy to condition on the disease, but a diagnosis needs the disease conditioned on the test result. Without a rule for reversing that conditioning, an observed outcome could never be turned back into a statement about the hypothesis that produced it. Prior and posterior distributions needs it next, since updating a prior into a posterior applies this same reversal to a whole distribution instead of a single event.
