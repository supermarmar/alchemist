---
id: conditional-probability
title: Conditional probability
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.1.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The conditional probability of an event given a second event is the probability that
both occur, divided by the probability of the second. It is undefined where the
second event has probability zero, which is why a continuous conditioning variable
needs a density rather than this definition.

## The expression

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0
$$

Here $A$ is the event whose probability is wanted, $B$ is the event taken as given,
and $A \cap B$ is their joint occurrence. Rearranging gives the multiplication rule,
$P(A \cap B) = P(A \mid B)\,P(B)$, which is the form every likelihood in the corpus
is assembled from.

## Why this node exists

Every model downstream is a conditional statement. A probability of default is the
probability of an event given what was known at origination, a hazard is a
probability given survival so far, and a generalised linear model's response is a
distribution given a covariate vector. Without conditioning, none of those three
sentences can be written down, so this node is the root the survival branch grows
from and the survival function needs it next.
