---
id: persistency-risk
title: Persistency risk
domains: [life]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp1.3.1-6, ifoa.sp2.3.1, ifoa.sp2.3.5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Persistency risk is the risk that a portfolio's actual persistency rate, the
proportion of policies remaining in force from one duration to the next,
diverges from the rate assumed at pricing, disrupting the profit a product was
designed to earn over its full term.

## The expression

$$
p_t = 1 - q_t^{\mathrm{lapse}}
$$

Here $p_t$ is the persistency rate in policy year $t$, the proportion of
in-force policies that remain in force to the start of year $t + 1$, and
$q_t^{\mathrm{lapse}}$ is the assumed or observed lapse rate over that year.

## Why this node exists

A pricing basis that assumes too optimistic a persistency rate overstates the
premium income a book will actually collect over its term. Health and care
underwriting risk needs this node next, since a health and care product's
persistency assumption feeds directly into the underwriting margin that risk
measures.
