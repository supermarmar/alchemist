---
id: forward-foreign-exchange-hedging
title: Forward foreign exchange hedging
domains: [fin-eng]
status: drafted
requires: [currency-as-asset-class]
spends: []
anchor: [ifoa.sp5.7.2-3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A forward foreign exchange contract fixes today the exchange rate at which a currency amount
will be bought or sold at a future date, letting a holder of an overseas asset or liability
lock in the domestic-currency value it will convert to, regardless of how the spot rate moves
before then.

## The expression

$$
F_0 = S_0 \, \frac{1 + r_d T}{1 + r_f T}
$$

Here $S_0$ is today's spot exchange rate, expressed as domestic currency per unit of foreign
currency, $F_0$ is the forward rate for delivery in $T$ years, and $r_d$ and $r_f$ are the
domestic and foreign risk-free rates respectively. The relationship holds under covered
interest rate parity: borrowing in one currency, converting at spot, investing at the foreign
rate and converting the proceeds back at the forward rate must earn no more than investing
directly in the domestic currency, or an arbitrage would be available.

## Why this node exists

Currency as an asset class establishes that a currency position carries its own return and
risk, but a business exposed to that risk through an overseas holding still needs an
instrument that removes the uncertainty, and the forward
contract is that instrument. Without covered interest rate parity fixing the forward rate to
the two currencies' interest rate differential, the price at which that uncertainty could be
removed would be set by nothing more than the market's own supply and demand for forward
contracts.
