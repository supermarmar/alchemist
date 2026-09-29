---
id: swaption
title: Swaption
domains: [fin-eng]
status: drafted
requires: [interest-rate-swap]
spends: []
anchor: [ifoa.sp6.2.5-11, ifoa.sp6.2.7-3, ifoa.sp6.3.6-3-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A swaption is an option to enter an interest rate swap as the fixed-rate payer or receiver from
a set date, with a European swaption exercisable only on that date and priced against the
forward swap rate the underlying swap would carry at expiry.

## The expression

$$
V = A \bigl[F\, \Phi(d_1) - K\, \Phi(d_2)\bigr], \qquad d_{1,2} = \frac{\ln(F/K) \pm \tfrac{1}{2}\sigma^2 T}{\sigma\sqrt{T}}
$$

Here $F$ is the forward swap rate observed today, $K$ is the swaption's strike, the fixed rate
it grants the right to pay or receive, $T$ is the time to the swaption's expiry, $\sigma$ is the
volatility of the forward swap rate, $A$ is the annuity factor built from the discounted period
lengths of the underlying swap, and $\Phi$ is the standard normal distribution function. $V$ is
the value of a payer swaption granting the right to pay the fixed rate $K$; a receiver swaption
swaps the roles of $F$ and $K$ inside the brackets.

## Why this node exists

An interest rate swap's value is defined only once the swap already exists, and a swaption
needs a way to price the right to enter that swap before it does, at a rate fixed today against
a swap rate that will not be known until expiry. Bermudan swaption needs this node next,
extending a European swaption's single exercise date into a set of dates the holder may choose
between.
