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
that the party paying the floating leg receives protection against inflation
running ahead of the rate fixed at outset.

## The expression

$$
N\Bigl[(1+K)^T - 1\Bigr] = N\left[\frac{I_T}{I_0} - 1\right]
$$

Here $N$ is the notional principal, $K$ is the fixed rate agreed at outset, $T$
is the term of the swap in years, $I_0$ is the value of the price index at the
start of the contract, and $I_T$ is its value at maturity. The two sides are
exchanged only at maturity for a zero-coupon inflation swap, which is the form
the expression above prices.

## Why this node exists

A pension scheme or an annuity book with liabilities that rise with inflation
cannot hedge that risk with an ordinary fixed-rate instrument, since a fixed
coupon leaves the real value of the liability exposed however interest rates
move. The floating leg above transfers exactly the inflation-index risk a
fixed-income hedge cannot reach, at the cost of the counterparty risk and market
liquidity that any over-the-counter contract carries.
