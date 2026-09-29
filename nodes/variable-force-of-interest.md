---
id: variable-force-of-interest
title: Variable force of interest
domains: [actuarial]
status: drafted
requires: [payment-frequency-conversion]
spends:
  - {object: obj.discount-factor, domain: actuarial}
anchor: [ifoa.cm1.1.1-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A variable force of interest is the instantaneous rate of interest at each moment when that
rate is itself a function of time, and the equivalent constant annual effective rate over a
period is recovered by integrating the force across that period.

## The expression

$$
v(t) = \exp\left(-\int_0^t \delta(s)\, ds\right)
$$

Here $\delta(s)$ is the force of interest prevailing at time $s$, and $v(t)$ is the discount
factor (spent here as the actuarial discount factor) for a payment due at time $t$, obtained by
accumulating the varying force across the whole interval from $0$ to $t$ before discounting.
The equivalent constant force $\bar\delta$ satisfying $\bar\delta\, t = \int_0^t \delta(s)\, ds$
gives the same discount factor as a single constant rate applied throughout.

## Why this node exists

A real interest rate environment rarely holds still, so a valuation that assumes one constant
rate throughout mis-prices any cash flow whose term stretches across a period where rates
genuinely moved. Integrating the force of interest is what lets a single equivalent rate stand
in for that whole varying path without distorting the cash flow's present value. Cashflow
valuation needs it next, since every present value from here on discounts at whichever force,
constant or varying, this node has already reduced to one equivalent rate.
