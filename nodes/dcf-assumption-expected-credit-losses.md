---
id: dcf-assumption-expected-credit-losses
title: Expected credit loss assumption in a discounted cashflow model
domains: [credit, fin-man]
status: drafted
requires: [discounted-cashflow-model-pricing]
spends:
  - {object: obj.exposure, domain: credit}
  - {object: obj.exposure, domain: fin-man}
anchor: [assa.f107.5.4-2-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The expected credit loss assumption in a discounted cashflow model is the projected loss a
product is expected to suffer over the horizon being priced, built from the same three
components that measure expected loss anywhere else in the corpus.

## The expression

$$
\mathrm{EL} = \mathrm{PD} \times \mathrm{LGD} \times \mathrm{EAD}
$$

Here $\mathrm{PD}$ is the probability the borrower defaults within the horizon, $\mathrm{LGD}$
is the loss given default, the proportion of the exposure not recovered once a default occurs,
$\mathrm{EAD}$ is the exposure at default, and $\mathrm{EL}$ is the expected credit loss the
model deducts from the product's projected income before discounting.

## Why this node exists

A discounted cashflow model that priced only income and cost would price a loan to a borrower
who never defaults exactly the same as an identical loan to a borrower who defaults with
certainty, since neither loan's contractual cash flows depend on default actually occurring. This
assumption is what makes the model's projected cash flow reflect the loss a defaulting borrower
is expected to cause, rather than only the cash flow a performing one would pay.
