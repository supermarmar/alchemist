---
id: fixed-income-valuation
title: Fixed income valuation
domains: [fin-eng]
status: drafted
requires: [bond-markets, investment-valuation]
spends:
  - {object: obj.discount-factor, domain: fin-eng}
anchor: [ifoa.sp5.3.2-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Fixed income valuation prices a bond, or a related instrument such as an interest rate swap
or a bond future, from its scheduled cash flows, discounted at rates drawn from the term
structure prevailing in the market.

## The expression

$$
P = \sum_{t=1}^{n} \mathrm{CF}_t \, v^t
$$

Here $P$ is the instrument's price, $\mathrm{CF}_t$ is the cash flow due at time $t$, whether
a coupon, a principal repayment or both, $n$ is the number of remaining cash flow dates, and
$v$ is the discount factor for one period at the yield the term structure implies for that
maturity. A swap is priced as the difference between two such valuations, a fixed leg and a
floating leg, and a bond future is priced off the same discounted cash flows adjusted for the
carry to delivery.

## Why this node exists

Bond markets set out what a bond promises to pay, but a promise of future cash is not a
price until it is discounted, and fixed income valuation supplies the discounting that turns
one into the other. Fixed income option pricing needs it next, since an option on a bond or a
swap is priced against the same discounted cash flow value this node establishes as the
underlying's fair price.
