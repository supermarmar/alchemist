---
id: time-value-of-money
title: Time value of money
domains: [actuarial, fin-eng, fin-man]
status: drafted
requires: []
spends:
  - {object: obj.discount-factor, domain: actuarial}
  - {object: obj.discount-factor, domain: fin-eng}
anchor: [up.fbs122.4, up.ias121.1, up.ias211.3, up.ias211.4, up.ias211.5, up.ias282.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The time value of money is the principle that a unit of currency received today is worth more
than the same unit received later, since it can be invested in the meantime to earn interest.

## The expression

$$
PV = FV \times v^n, \qquad v = \frac{1}{1 + i}
$$

Here $FV$ is an amount payable $n$ periods from now, $i$ is the interest rate per period, $v$ is
the discount factor, the present value of one unit payable in one period, and $PV$ is the
present value of $FV$ today. Raising $i$ to obtain $FV$ from $PV$ is called accumulating, and
applying $v^n$ to obtain $PV$ from $FV$ is called discounting.

## Why this node exists

Two cash flows falling at different times cannot be compared, added or valued against one
another until they are expressed at a common point in time, and every actuarial and financial
valuation in the corpus rests on this single conversion. The equation of value needs it next,
since setting the present value of what is paid equal to the present value of what is received
is exactly this discounting relationship applied to a whole schedule of cash flows at once.
