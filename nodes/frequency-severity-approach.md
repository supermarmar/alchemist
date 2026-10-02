---
id: frequency-severity-approach
title: Frequency/severity approach
domains: [gi, stats]
status: drafted
requires: [collective-risk-model]
spends: []
anchor: [ifoa.sp8.3.5-2]
vault_articles: [methods/aggregate-loss-models]
vault_sources: []
taught_in: null
---

## Definition

The frequency/severity approach rates a risk by modelling how often claims occur and how
large each one is as two separate components, then combining them into an expected cost.
This separation is what lets an actuary see whether a change in the rate is being driven
by more claims or by larger ones.

## The expression

$$
E[S] = E[N]\, E[X]
$$

Here $E[S]$ is the expected aggregate loss, $E[N]$ is the expected number of claims, and
$E[X]$ is the expected size of an individual claim.

## Why this node exists

A single aggregate loss figure erases the question of what moved it, and the
frequency/severity split answers that question directly: a rate can rise because claims
became more frequent, because they became more severe, or both, and each cause points a
pricing actuary towards a different underwriting response. Original loss curve needs it
next, since building that curve means starting from the separate frequency and severity
components this node keeps apart.
