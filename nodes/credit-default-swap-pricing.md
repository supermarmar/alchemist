---
id: credit-default-swap-pricing
title: Pricing a credit default swap
domains: [credit, fin-eng]
status: drafted
requires: [credit-default-swap, credit-event-and-recovery-rate]
spends:
  - {object: obj.discount-factor, domain: fin-eng}
  - {object: obj.hazard, domain: credit}
anchor: [ifoa.sp6.3.9-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Pricing a credit default swap values the contract by setting the present value of the premium
leg the protection buyer pays equal to the present value of the protection leg the protection
seller stands ready to pay, given a hazard rate curve and an assumed recovery rate. The fair, or
par, spread is the rate that clears that equality.

## The expression

$$
s \sum_{k=1}^{n} v^{t_k}\, e^{-h t_k} = (1-R) \sum_{k=1}^{n} v^{t_k} \left(e^{-h t_{k-1}} - e^{-h t_k}\right)
$$

Here $s$ is the fair spread, $t_k$ is the $k$-th premium date up to maturity, $n$ is the number
of premium dates, $v$ is the discount factor applied per period, $h$ is the reference entity's
hazard rate, treated here as constant, so that survival to $t$ is $e^{-ht}$, and $R$ is the
assumed recovery rate. The left side is the premium leg's present value, the right side the
protection leg's.

## Why this node exists

The par spread the previous node approximated as $(1-R)h$ assumed a flat term structure and
ignored the timing of payments, and this equality replaces that approximation with the actual
present value each leg carries once discounting and the payment schedule are put back in. A
trading desk marks a swap to market by revaluing this same equality at the day's hazard rate
curve, since a change in that curve moves the two legs by different amounts and leaves a gain
or loss on the position held.
