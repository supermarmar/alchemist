---
id: multi-asset-and-quanto-option
title: Multi-asset and quanto options
domains: [fin-eng]
status: drafted
requires: [option-payoff-profile]
spends: []
anchor: [ifoa.sp6.2.6-1, ifoa.sp6.2.6-7, ifoa.sp6.2.6-8]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An exchange option pays the excess of one underlying over another at expiry, a basket option
pays the excess of a weighted combination of several underlyings over a strike, and a quanto
option converts a foreign-currency payoff at a rate fixed in advance, removing the exchange-rate
risk that a plain foreign payoff would otherwise carry.

## The expression

$$
\begin{aligned}
\text{Payoff}_{\text{exchange}} &= \max(S_1(T) - S_2(T),\, 0) \\
\text{Payoff}_{\text{basket}} &= \max\!\left(\sum_i w_i S_i(T) - K,\, 0\right)
\end{aligned}
$$

Here $S_1(T)$ and $S_2(T)$ are the two underlyings' prices at expiry in the exchange option,
$w_i$ and $S_i(T)$ are the weight and expiry price of the $i$th asset in the basket, and $K$ is
the basket's strike.

$$
\text{Payoff}_{\text{quanto}} = X_0 \cdot \max(S(T) - K,\, 0)
$$

Here $S(T)$ is the foreign-currency price of the underlying at expiry, $K$ is the strike in the
same foreign currency, and $X_0$ is the exchange rate fixed at inception, applied to the payoff
regardless of where the exchange rate actually moves to by expiry.

## Why this node exists

A single-underlying, single-currency payoff cannot price a position that depends on the
relationship between two assets or on an asset traded in a currency other than the one the
payoff is wanted in, and each of these three payoffs supplies one of those missing pieces.
Pricing any of them still reduces to an expectation of the payoff under some measure, exactly
as the plain call and put already do, so the extension is in what is inside the maximum rather
than in how the price is eventually computed from it.
