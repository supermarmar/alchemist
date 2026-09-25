---
id: capital-project-appraisal
title: Capital project appraisal
domains: [actuarial, fin-eng, fin-man]
status: drafted
requires: [time-value-of-money]
spends:
  - {object: obj.discount-factor, domain: actuarial}
anchor: [up.fbs122.8, up.fni700.7, up.ias282.2, up.ias712.13, up.ias712.14]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Capital project appraisal discounts a project's expected future cash flows to a present value
at the organisation's required rate of return, and a project is worth undertaking only where
that present value exceeds the cost of the investment it requires.

## The expression

$$
\mathrm{NPV} = \sum_{t=1}^{n} v^{t} \, C_t - C_0
$$

Here $\mathrm{NPV}$ is the project's net present value, $C_0$ is the initial outlay, $C_t$ is
the net cash flow expected in year $t$, $n$ is the project's life, and $v$ is the discount
factor for one year at the required rate of return. A positive net present value means the
project's discounted returns exceed its cost; a negative one means they do not.

## Why this node exists

Comparing a cash flow received today against one promised in ten years' time needs a common
basis before the comparison means anything, and discounting is what supplies that basis. Risky
investment evaluation needs a base-case present value settled before it can adjust that figure
for the uncertainty a real project's cash flows actually carry.
