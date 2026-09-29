---
id: present-value
title: Present value
domains: [actuarial]
status: drafted
requires: [accumulated-value]
spends:
  - {object: obj.discount-factor, domain: actuarial}
anchor: [ifoa.cm1.1.2-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The present value of a future payment is the amount that, invested now, accumulates
to that payment by the date it falls due, so it discounts a single future cashflow
back to its value today by running the accumulation relationship in reverse.

## The expression

$$
PV = FV \cdot v^n
$$

Here $FV$ is the future payment, $n$ is the number of periods until it falls due,
$v = \frac{1}{1+i}$ is the discount factor for one period at interest rate $i$, and
$PV$ is the present value.

## Why this node exists

Comparing payments due at different times needs them expressed in a common unit,
and present value is that unit, the value each payment would have if it fell due
today. Cashflow valuation needs it next, applying this same discounting to a whole
schedule of payments rather than to one payment taken alone.
