---
id: payment-frequency-conversion
title: Payment frequency conversion
domains: [actuarial]
status: drafted
requires: [interest-discount-relationship]
spends: []
anchor: [ifoa.cm1.1.1-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Payment frequency conversion restates an annual effective interest rate as the equivalent
nominal rate payable a stated number of times a year, and as the force of interest obtained by
taking that number of payments to the continuous limit. Every restatement values the same
accumulation of one unit over one year; only the frequency at which interest is credited
changes.

## The expression

$$
1 + i = \left(1 + \frac{i^{(p)}}{p}\right)^{p} = e^{\delta}
$$

Here $i$ is the annual effective rate of interest, $i^{(p)}$ is the nominal rate of interest
convertible $p$ times a year, and $\delta$ is the force of interest, the continuously
compounding rate obtained as $p \to \infty$. Each of the three describes the same annual
accumulation of one unit, so any one of them can be recovered from either of the others.

## Why this node exists

A cash flow schedule payable monthly or quarterly cannot be valued against an annual effective
rate without first converting one to match the other, and this conversion is what every annuity
or loan repayment calculated at a frequency other than annual depends on. Variable force of
interest needs this node next, since a force of interest that itself changes over time is built
by letting the constant $\delta$ this node defines vary with $t$.
