---
id: risky-investment-evaluation
title: Risky investment evaluation
domains: [fin-man]
status: drafted
requires: [capital-project-appraisal]
spends: []
anchor: [up.fbs122.9]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Risky investment evaluation discounts a project's expected cash flows at a required rate raised above the risk-free rate by a premium reflecting the project's own risk. A project whose cash flows are certain needs no such premium, and its appraisal reduces to the ordinary net present value calculation.

## The expression

$$
\mathrm{NPV} = \sum_{t=1}^{n} \frac{C_t}{(1 + r_f + \pi)^{t}} - C_0
$$

Here $C_0$ is the initial outlay, $C_t$ is the expected net cash flow in year $t$, $n$ is the project's life, $r_f$ is the risk-free rate, and $\pi$ is the risk premium added to compensate for the uncertainty in $C_t$. Raising the discount rate by $\pi$ lowers the present value assigned to any cash flow whose size or timing is less certain, weighing it against a cash flow of the same expected size treated as guaranteed.

## Why this node exists

A single required rate cannot serve every project a firm considers, since two projects promising the same expected cash flow do not carry the same chance of actually delivering it, and discounting them identically would rank the riskier one too generously. Raising the discount rate by a risk premium is the simplest way to build that difference into the appraisal, though the premium itself needs justifying project by project, unlike a single discount rate set once for the whole firm.
