---
id: prepayment-risk
title: Prepayment risk
domains: [credit, fin-eng]
status: drafted
requires: []
spends: []
anchor: [assa.f107.1.12-12]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Prepayment risk is the risk that borrowers in a loan pool repay principal
earlier than the scheduled amortisation implies, shortening the pool's actual
cash flow profile relative to the one used to price and hedge it.

## The expression

$$
\mathrm{CPR} = 1 - (1 - \mathrm{SMM})^{12}
$$

Here $\mathrm{SMM}$ is the single monthly mortality rate, the proportion of the
remaining pool balance prepaid in one month, and $\mathrm{CPR}$ is the
annualised conditional prepayment rate obtained by compounding that monthly
rate over twelve months.

## Why this node exists

A pool's cash flows cannot be scheduled from its contractual amortisation alone
once prepayment is material. Modelling pre-payment behaviour needs this node
next, turning the conditional prepayment rate defined here into a rate that
responds to the drivers, such as the interest rate gap, that actually move it.
