---
id: embedded-value-calculation
title: Embedded value calculation
domains: [actuarial, life]
status: drafted
requires: [assumption-setting-for-embedded-value, cost-of-capital]
spends:
  - {object: obj.discount-factor, domain: actuarial}
  - {object: obj.discount-factor, domain: life}
anchor: [ifoa.sp1.4.3-4]
vault_articles: [concepts/market-consistent-embedded-value]
vault_sources: []
taught_in: null
---

## Definition

Embedded value calculation turns a health and care book's projected future shareholder cash
flows into a single present value, by discounting each projected year's cash flow at a rate
that reflects the risk the book still carries once the assumptions behind the projection are
fixed.

## The expression

$$
\mathrm{VIF} = \sum_{t=1}^{n} \mathrm{CF}_t \, v^t
$$

Here $\mathrm{CF}_t$ is the shareholder cash flow the book is projected to release in year
$t$, $n$ is the projection term, and $v$ is the discount factor derived from the risk
discount rate the cost of capital sets. Summing the discounted cash flows gives the value of
in-force business, $\mathrm{VIF}$, which is added to the adjusted net asset value already
held to give the embedded value the previous node's formula names.

## Why this node exists

Assumption setting fixes what each future cash flow is projected to be, but a stream of
future cash flows is not itself a value until it is brought back to the present, and doing
that consistently across every year of the projection is this node's job. Without it, the
projection would remain a schedule of numbers rather than the single reported figure a
board, a regulator or a buyer needs to compare against another book's value.
