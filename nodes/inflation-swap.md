---
id: inflation-swap
title: Inflation swap
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.2.7-5, ifoa.sp6.2.7-6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An inflation swap exchanges a fixed-rate cash flow for a cash flow linked to the
cumulative change in a specified price index over the life of the contract, so
that the party paying the fixed rate and receiving the inflation-linked leg is
protected against inflation running ahead of the rate fixed at outset.

## The expression

$$
N\left[\frac{I_T}{I_0} - (1+K)^T\right]
$$

Here $N$ is the notional principal, $I_0$ is the value of the price index at the
start of the contract, $I_T$ is its value at maturity, $K$ is the fixed rate
agreed at outset, and $T$ is the term of the swap in years. The expression is the
net payoff at maturity to the party receiving the inflation leg, and $K$ is the
breakeven rate that makes the swap worth zero at inception, so that neither party
pays anything to enter the contract. The two sides are exchanged only at maturity
for a zero-coupon inflation swap, which is the form the expression above describes.

## Why this node exists

A pension scheme or an annuity book with liabilities that rise with inflation
cannot hedge that risk with an ordinary fixed-rate instrument, since a fixed
coupon leaves the real value of the liability exposed however interest rates
move. The floating leg above transfers exactly the inflation-index risk a
fixed-income hedge cannot reach, at the cost of the counterparty risk and market
liquidity that any over-the-counter contract carries.
