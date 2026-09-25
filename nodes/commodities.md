---
id: commodities
title: Commodities
domains: [fin-eng]
status: drafted
requires: [investment-asset-characteristics-and-markets]
spends: []
anchor: [ifoa.sp5.2.1-11]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Commodities are an investable asset class typically accessed through futures or derivative
exposure rather than physical holding, and their forward price is set by the cost of carrying
the physical commodity forward net of the benefit of holding it in hand.

## The expression

$$
F_0 = S_0 \, e^{(r + u - y) T}
$$

Here $F_0$ is the forward price agreed today for delivery at time $T$, $S_0$ is the spot
price, $r$ is the risk-free rate, $u$ is the storage cost expressed as a continuous yield, and
$y$ is the convenience yield, the benefit a holder of the physical commodity gets from having
it in hand that a holder of the forward contract does not. A financial asset paying no income
carries no such convenience yield, which is what distinguishes a commodity forward from an
equity or bond forward.

## Why this node exists

An equity or bond forward is priced from carry alone, but a commodity holder's willingness to
give up a forward contract's flexibility for the physical good itself, to keep production
running or meet a delivery obligation, adds a benefit no purely financial asset carries. Any
comparison between commodities and other investable asset classes has to account for that
benefit before their returns can be judged on the same footing.
