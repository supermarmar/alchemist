---
id: dcf-use-risk-based-pricing
title: Risk-based pricing use of a discounted cashflow model
domains: [credit, fin-man]
status: drafted
requires: [discounted-cashflow-model-pricing]
spends: []
anchor: [assa.f107.5.4-3-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Risk-based pricing sets a loan's customer rate as the sum of the bank's internal funding cost,
the expected loss the loan is assumed to generate, its share of operating costs and a charge for
the capital it consumes, so that a riskier loan is priced to earn back what it is expected to
cost, and a safer loan is priced lower to reflect the cost it avoids.

## The expression

$$
r_{\text{price}} = r_{\text{ftp}} + \frac{\mathrm{EL}}{\mathrm{EAD}} + \frac{\mathrm{Opex}}{\mathrm{EAD}} + h \times \frac{K}{\mathrm{EAD}}
$$

Here $r_{\text{ftp}}$ is the internal funds transfer price charged for the loan's funding,
$\mathrm{EL}$ is its expected credit loss, $\mathrm{Opex}$ is its share of operating costs, $K$
is the capital required to support it, $\mathrm{EAD}$ is its exposure at default, and $h$ is the
hurdle rate the bank targets on capital, so that $r_{\text{price}}$ is the customer rate that
recovers every one of those four components in turn.

## Why this node exists

A rate set only to cover funding cost and expected loss still leaves operating costs and the
return shareholders require on capital unrecovered, and a bank that prices that way is
systematically under-earning on every loan it writes. Building the price up from each of these
components separately is what lets a bank see which component is driving a given loan's price,
so it can adjust that one component directly and leave the others untouched.
