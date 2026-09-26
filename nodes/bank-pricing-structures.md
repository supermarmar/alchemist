---
id: bank-pricing-structures
title: Pricing structures of loans and deposits
domains: [fin-man]
status: drafted
requires: []
spends: []
anchor: [assa.f107.5.1-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A loan or deposit is priced as a fixed rate agreed for the term, or as a floating rate set
periodically at a margin over a published reference rate.

## The expression

$$
r = r_{\text{ref}} + m
$$

Here $r$ is the rate charged or paid, $r_{\text{ref}}$ is the reference rate the product is
set against, such as a central bank base rate or an interbank benchmark, and $m$ is the
margin the bank adds on a loan or deducts on a deposit. A fixed-rate product simply holds
$r$ constant over the term instead of resetting it against $r_{\text{ref}}$ each period.

## Why this node exists

A margin set too thin against the reference rate leaves a loan unable to cover the funding,
expected loss and capital cost behind it, while a deposit margin set too wide loses the
funding a bank needs to write those loans in the first place. Risk-based pricing needs this
structure fixed before it can vary the margin $m$ by the borrower's own credit risk rather
than holding it uniform across a book.
