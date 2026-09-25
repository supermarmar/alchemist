---
id: censoring
title: Censoring
domains: [credit, life, stats]
status: drafted
requires: []
spends: []
anchor: [ucsc.dl-actuarial-2026.l01, ifoa.cs2.4.2-1]
vault_articles: [methods/credit-default-outcome-construction]
vault_sources: []
taught_in: null
---

## Definition

Right-censoring occurs when a subject's true event time lies beyond the edge of the
observation window, so only a lower bound on that time is known: the subject has not
been shown to survive past the window, only to have not yet failed within it. Every
estimator built on censored data assumes the censoring is non-informative, so that
leaving the risk set early carries no information about how much longer that subject
would otherwise have survived.

## The expression

$$
y_i = \min(T_i, C_i), \qquad \delta_i = \mathbb{1}(T_i \le C_i)
$$

Here $T_i$ is subject $i$'s true, possibly unobserved event time, $C_i$ is the time at
which observation of that subject ends, $y_i$ is the time actually recorded, and
$\delta_i$ indicates whether $y_i$ is the event itself or a censoring point.

## Why this node exists

Discarding every subject still open at the snapshot biases a sample towards those who
failed early, and treating an open subject as a survivor to the end of the window
biases it the other way. Recognising censoring as its own outcome, distinct from
either, is what lets a lender's still-performing loans and an insurer's still-living
policyholders enter the same calculation honestly. The empirical survival function
needs it next, since it is the first estimator this corpus builds that has to account
for it.
