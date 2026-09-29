---
id: cash-shortfall
title: Cash shortfall
domains: [credit, regulation]
status: drafted
requires: []
spends: []
anchor: [iasb.ifrs9.b5.5-28, iasb.ifrs9.b5.5-29, iasb.ifrs9.b5.5-30]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A cash shortfall is the present value of the gap between the cash flows contractually due to an entity and the cash flows it actually expects to receive. It is positive even where the entity expects eventual repayment in full, since a delay in payment is itself treated as a shortfall.

## The expression

$$
\mathrm{CS}_t = \mathrm{PV}\bigl(\mathrm{CF}^{\text{contractual}}_t - \mathrm{CF}^{\text{expected}}_t\bigr)
$$

Here $\mathrm{CS}_t$ is the cash shortfall assessed at time $t$, $\mathrm{PV}$ discounts the bracketed difference at the instrument's effective interest rate, $\mathrm{CF}^{\text{contractual}}_t$ is the cash flow contractually due, and $\mathrm{CF}^{\text{expected}}_t$ is the cash flow the entity actually expects to receive.

## Why this node exists

An expected credit loss is a probability-weighted average of shortfalls across future dates and scenarios, and there is nothing for that average to weight until each date has a shortfall of its own. Expected credit loss needs it next, since it is built directly from the object this node defines.
