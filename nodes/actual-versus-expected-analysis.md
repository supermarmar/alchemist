---
id: actual-versus-expected-analysis
title: Actual versus expected analysis
domains: [actuarial, fin-man]
status: drafted
requires: [actuarial-control-cycle]
spends: []
anchor: [ifoa.cp1.5.2-1, ifoa.cp1.5.3-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Actual versus expected analysis compares the experience actually observed against
what the assumption set predicted, expressing the comparison as a ratio that flags
where the assumptions need revision.

## The expression

$$
\mathrm{A/E} = \frac{\text{Actual}}{\text{Expected}}
$$

Here Actual is the outcome observed over the period, and Expected is what the
assumption set predicted for the same period and population. An A/E ratio close to
one shows the assumption holding; a ratio persistently away from one is the signal
that it needs revising.

## Why this node exists

A model that is never checked against what happens will drift silently away from
reality, and A/E analysis is the check that catches the drift assumption by
assumption. Analysis of surplus needs it next, since it decomposes the same gap
between actual and expected experience into the individual assumptions responsible
for it.
