---
id: expectation-of-life
title: Expectation of life
domains: [life]
status: drafted
requires: [curtate-future-lifetime, survival-function]
spends:
  - {object: obj.survival, domain: life}
anchor: [ifoa.cs2.4.1-7]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The curtate expectation of life is the expected number of complete future years a life aged
exactly $x$ will survive, and the complete expectation of life is the expected value of the
same life's future lifetime measured continuously rather than in whole years.

## The expression

$$
e_x = \sum_{k=1}^{\infty} {}_k p_x
$$

Here $e_x$ is the curtate expectation of life at age $x$ and ${}_k p_x$ is the probability
that a life aged $x$ survives at least $k$ further years, the survival probability named
elsewhere in the corpus. Summing that survival probability over every future year, rather
than integrating it continuously, is what makes the expectation curtate. The complete
expectation, written $\overset{\circ}{e}_x$, exceeds $e_x$ by approximately one half under
the usual assumption that deaths are spread uniformly across each year of age.

## Why this node exists

A mortality table gives the probability of surviving to any given age, but a single summary
figure is often wanted for pricing and reserving purposes, and expectation of life is that
summary. Without a stated relationship between the curtate and complete forms, the half-year
adjustment between $e_x$ and $\overset{\circ}{e}_x$ is easy to apply in the wrong direction,
which is why the two notations, and the approximation linking them, are fixed here together.
