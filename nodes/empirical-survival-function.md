---
id: empirical-survival-function
title: Empirical survival function
domains: [life, stats]
status: drafted
requires: [censoring, survival-function]
spends:
  - {object: obj.survival, domain: life}
  - {object: obj.survival, domain: stats}
anchor: [ifoa.cs2.4.2-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The empirical survival function estimates the survival function directly from a
sample, as the proportion of subjects still event-free at a given time, with no
parametric form assumed. It is unbiased only where every subject's event time is fully
observed, since a censored subject's true status at $t$ is unknown, and cannot simply
be counted either way.

## The expression

$$
\hat{S}(t) = \frac{\#\{i : T_i \gt t\}}{n}
$$

Here $\hat{S}(t)$ is the empirical estimate of the survival function, $n$ is the sample
size, and the numerator counts the subjects whose event time exceeds $t$. The object
estimated is the same $S(t)$ statistics already names and the same ${}_tp_x$ the life
table already names, read here from a sample rather than assumed.

## Why this node exists

A direct count of survivors is correct only when nobody has left the sample before
their event time is known, and censoring guarantees that some subjects will. The
Kaplan-Meier estimator needs this node next, since it is built to correct exactly this
failure when censoring is present.
