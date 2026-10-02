---
id: unit-linked-contract
title: Unit-linked contract
domains: [actuarial, life]
status: drafted
requires: [assurance-contract]
spends: []
anchor: [ifoa.cm1.3.1-3, ifoa.sp2.1.1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A unit-linked contract pays, on the death of the life assured, an absolute sum assured
plus the value of the units held in a linked fund at that time; the death benefit
collapses to the sum assured alone where the policyholder has not yet allocated any
premium to units.

## The expression

$$
D_t = SA + N_t \, U_t
$$

Here $D_t$ is the death benefit payable if death occurs at time $t$, $SA$ is the fixed
sum assured, $N_t$ is the number of units the policyholder holds at $t$, and $U_t$ is the
price of one unit at $t$. The product $N_t U_t$ is the fund value, which grows or shrinks
with the performance of the assets the fund is invested in.

## Why this node exists

A conventional non-linked contract fixes its benefit at outset, so the insurer alone
bears investment risk, whereas a unit-linked contract passes that risk to the
policyholder through $U_t$ and keeps only the sum-assured layer on its own balance sheet.
An accumulating with-profits contract needs it next, since it borrows the unit-fund
mechanics here and replaces the linked fund's market-driven $U_t$ with a smoothed,
insurer-declared growth rate.
