---
id: exposure-at-default
title: Exposure at default
domains: [credit, regulation, stats]
status: drafted
requires: []
spends:
  - {object: obj.exposure, domain: credit}
anchor: [assa.f107.6.1-3-1-3, assa.f107.6.1-9-3, bcbs.d424.irb.para-98]
vault_articles: [methods/ifrs9-ead-ccf-modelling]
vault_sources: []
taught_in: null
---

## Definition

Exposure at default is the amount a bank expects to be owed at the point a borrower defaults. For
a term loan it is largely contractual, but for a revolving or partly undrawn facility it exceeds
the balance outstanding today, since a borrower who is about to default tends to draw further
before doing so.

## The expression

$$
\mathrm{EAD}_i = D_i + \mathrm{CCF}_i \times (L_i - D_i)
$$

Here $D_i$ is facility $i$'s drawn balance today, $L_i$ is its committed limit, $L_i - D_i$ is the
undrawn commitment, and $\mathrm{CCF}_i$ is the credit conversion factor, the estimated proportion
of that undrawn amount the borrower draws down before default. $\mathrm{EAD}_i$ is the resulting
exposure the loss given default is applied to.

## Why this node exists

A model that priced only the drawn balance would understate exposure for exactly the accounts
whose credit position is deteriorating fastest, since utilisation typically rises before default
on a revolving facility. EAD quantification standards need this node next, since they fix how the
credit conversion factor itself is estimated and calibrated.
