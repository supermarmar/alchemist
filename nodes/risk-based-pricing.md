---
id: risk-based-pricing
title: Risk-based pricing of loans
domains: [credit, fin-man]
status: drafted
requires: [bank-pricing-structures, credit-risk]
spends: []
anchor: [assa.f107.5.1-2, assa.f207.1.12-1]
vault_articles: [concepts/economic-value-of-rating-systems]
vault_sources: []
taught_in: null
---

## Definition

Risk-based pricing sets a loan's margin above the reference rate so that it also compensates the
lender for the borrower's own assessed credit risk, replacing a margin held uniform across the
book with one that varies borrower by borrower.

## The expression

$$
r_i = r_{\text{ref}} + m + \mathrm{PD}_i \times \mathrm{LGD}_i
$$

Here $r_i$ is the rate charged to borrower $i$, $r_{\text{ref}} + m$ is the base pricing
structure of reference rate plus margin, and $\mathrm{PD}_i \times \mathrm{LGD}_i$ is that
borrower's expected loss rate, the probability of default multiplied by the loss given default,
added to the margin so that a riskier borrower is charged a compensating premium over a safer
one.

## Why this node exists

A margin held uniform across every borrower leaves a bank charging a safe borrower more than
their risk requires and a risky borrower less, which drives the safest borrowers to a
competitor pricing them correctly and leaves the bank's book adversely selected. Retail loan
pricing needs this node next, applying the same principle to the specific margin conventions a
retail lending book uses.
