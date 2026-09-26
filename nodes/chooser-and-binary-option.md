---
id: chooser-and-binary-option
title: Chooser and binary options
domains: [fin-eng]
status: drafted
requires: [option-payoff-profile]
spends: []
anchor: [ifoa.sp6.2.6-2, ifoa.sp6.2.6-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A chooser option lets its holder decide, at a fixed date before expiry, whether the contract
becomes a call or a put, while a binary option pays a fixed cash amount, or nothing, according
to whether the underlying finishes above or below the strike at expiry.

## The expression

$$
V_{\text{chooser}} = \max\bigl(C(S, t), P(S, t)\bigr), \qquad
V_{\text{binary call}} = Q \cdot \mathbb{1}\{S_T \gt K\}
$$

Here $C(S, t)$ and $P(S, t)$ are the values, at the choice date $t$, of a call and a put on
the same underlying $S$, struck and dated identically, and the chooser's value is whichever is
larger since the holder always chooses the more valuable side. $Q$ is the fixed cash amount a
cash-or-nothing binary call pays, $S_T$ is the underlying's price at expiry $T$, $K$ is the
strike, and $\mathbb{1}\{\cdot\}$ is one if the condition holds and zero otherwise.

## Why this node exists

A payoff that switches discontinuously at a strike, or defers a choice to a later date, cannot
be priced by the smooth payoff formulas a plain call or put already uses, so both instruments
need their own valuation treatment built on top of the payoff profile a plain option
establishes. Without that treatment, a desk could describe what either contract pays but not
what it is worth today.
