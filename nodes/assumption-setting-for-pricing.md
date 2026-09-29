---
id: assumption-setting-for-pricing
title: Assumption setting for pricing
domains: [actuarial, life]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp1.4.2-2, ifoa.sp1.5.1-1, ifoa.sp2.5.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Assumption setting for pricing chooses the mortality, morbidity, persistency and expense
bases fed into the premium equation, so that the premium charged is expected to cover the
benefits and expenses the contract will generate, alongside the required profit margin.

## The expression

$$
\mathrm{EPV(premiums)} = \mathrm{EPV(benefits)} + \mathrm{EPV(expenses)} + \mathrm{EPV(profit)}
$$

Here $\mathrm{EPV}$ denotes the expected present value of the cash flow named in
parentheses, each computed under the pricing assumptions chosen for the contract. Solving
this equation for the premium is what turns a set of assumptions into a price.

## Why this node exists

A premium set without stated assumptions cannot be checked, defended or repriced when
experience diverges from what was expected, since there is nothing recorded to compare
experience against. Pricing versus reserving assumption differences needs this node's
pricing basis fixed before it can contrast that basis with the more prudent one reserving
requires.
