---
id: assumption-setting-for-reserving
title: Assumption setting for reserving
domains: [actuarial, life]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp1.5.1-2, ifoa.sp2.5.1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Assumption setting for reserving chooses the mortality, morbidity, persistency and expense
bases used to determine an insurer's liabilities, set with enough prudence that the
resulting reserve holds up under experience worse than expected.

## The expression

$$
{}_tV = \mathrm{EPV(future\ benefits + expenses)} - \mathrm{EPV(future\ premiums)}
$$

Here ${}_tV$ is the prospective reserve held at duration $t$, and each expected present
value term is computed under the reserving basis, a basis chosen more prudently than the
pricing basis that set the premium in the first place.

## Why this node exists

A reserve computed on the pricing basis carries no margin against experience turning out
worse than assumed, and a reserve is meant to hold precisely when that happens. This node's
prudent basis is what makes the reserve resilient, and pricing versus reserving assumption
differences needs it stated before it can be set against the pricing basis directly.
