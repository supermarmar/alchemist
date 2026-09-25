---
id: development-factor
title: Development factor
domains: [gi, stats]
status: drafted
requires: []
spends:
  - {object: obj.development-factor, domain: gi}
anchor: [ifoa.cm2.4.2-1]
vault_articles: [methods/chain-ladder-reserving]
vault_sources: []
taught_in: null
---

## Definition

A development factor is the ratio that carries a cohort's cumulative loss from one development
index to the next, estimated across every cohort in a triangle that has reached both indices.

## The expression

$$
f_j = \frac{\sum_i C_{i,j+1}}{\sum_i C_{i,j}}
$$

Here $f_j$ is the development factor carrying cumulative losses from development index $j$ to
$j+1$, $C_{i,j}$ is cohort $i$'s cumulative loss at development index $j$, and each sum runs
over every cohort in the triangle observed at both indices.

## Why this node exists

The chain ladder method chains a development factor at every index together to project each
cohort's latest observed loss through to its ultimate, so a single unestimated factor leaves a
gap the whole projection cannot cross. Chain ladder method needs this factor at every step it
takes.
