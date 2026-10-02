---
id: select-and-ultimate-life-table
title: Select and ultimate life table
domains: [life]
status: drafted
requires: [survival-model]
spends: []
anchor: [up.ias221.2, up.ias353.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A select and ultimate life table records mortality separately during a select period following
selection, when a life's mortality is lighter than the population average, before that select
rate merges into the ultimate rate once the select period has elapsed.

## The expression

$$
q_{[x]+r} \le q_{x+r}, \qquad 0 \le r \lt s
$$

Here $q_{[x]+r}$ is the select mortality rate for a life selected at age $x$ and now $r$ years
past selection, $q_{x+r}$ is the corresponding ultimate rate for a life of the same attained
age with no selection history, and $s$ is the length of the select period, the duration after
which $q_{[x]+r}$ and $q_{x+r}$ become the same rate.

## Why this node exists

A life table built on ultimate rates alone overstates mortality for a recently underwritten
life, since underwriting itself screens out the lives most likely to die soon, and pricing
against the wrong rate for that period misprices exactly the business a fund has just written.
This node makes that screening effect explicit as a separate select rate, so that a valuation
applies the rate appropriate to how recently the life was selected.
