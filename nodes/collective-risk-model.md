---
id: collective-risk-model
title: Collective risk model
domains: [gi, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs2.1.2-1, ifoa.cs2.1.2-2, ifoa.sp8.2.4]
vault_articles: [methods/aggregate-loss-models]
vault_sources: []
taught_in: null
---

## Definition

The collective risk model represents a portfolio's aggregate claims as a random sum of a random number of independent, identically distributed claim amounts, treating how many claims occur and how large each one is as separate components rather than modelling the total directly.

## The expression

$$
S = \sum_{i=1}^{N} X_i
$$

Here $S$ is the aggregate claims, $N$ is the random claim count, independent of the claim amounts, and each $X_i$ is the size of the $i$-th claim, drawn independently from the same severity distribution.

## Why this node exists

Modelling frequency and severity separately only pays off once their separate moments can be recombined into the moments of the total, and Moments of compound claim distributions needs it next to carry out that recombination.
