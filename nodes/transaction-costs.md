---
id: transaction-costs
title: Transaction costs
domains: [fin-man, regulation]
status: drafted
requires: []
spends: []
anchor: [iasb.ifrs9.b5.4-8]
vault_articles: [concepts/effective-interest-rate]
vault_sources: []
taught_in: null
---

## Definition

Transaction costs are the incremental costs of acquiring, issuing or disposing of a financial
instrument that would not have arisen otherwise, such as fees paid to agents, advisers and
regulators, and they adjust the instrument's initial carrying amount instead of being expensed
at inception.

## The expression

$$
C_0 = \sum_{t=1}^n \frac{CF_t}{(1+r)^t}
$$

Here $CF_t$ is the contractual cash flow expected at time $t$, $r$ is the effective interest
rate, the single rate that discounts those cash flows to equal the instrument's initial carrying
amount, and $C_0$ is that carrying amount, net of any transaction costs paid or received at
origination. Adding transaction costs into $C_0$ raises $r$ above the instrument's stated
contractual rate, since the same future cash flows must now be discounted from a smaller
starting amount.

## Why this node exists

A cost that is integral to a lending or investing decision cannot be recognised in profit or
loss the moment it is paid, or the instrument's reported yield would jump in the period of
origination and understate it in every period after. Spreading transaction costs through the
effective interest rate keeps income recognition consistent with the instrument's actual
economics, and initial measurement at fair value needs this adjusted carrying amount as its
starting point.
