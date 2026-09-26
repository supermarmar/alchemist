---
id: pension-fund-interest-rate-and-inflation-hedging
title: Pension fund interest rate and inflation hedging
domains: [fin-eng, fin-man]
status: drafted
requires: []
spends: []
anchor: [assa.f207.2.7-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Hedging a pension fund's interest rate and inflation exposure means holding
instruments whose value moves with long-term nominal and real yields in the
same direction as the liabilities do, so that a fall in yields that inflates
the liability value is offset by a rise in the value of the hedge.

## The expression

$$
N = \frac{\mathrm{PV01}_L}{\mathrm{PV01}_H}
$$

Here $\mathrm{PV01}_L$ is the change in the present value of the pension
liabilities for a one basis point fall in yields, $\mathrm{PV01}_H$ is the
corresponding change in the value of one unit of the hedging instrument, and
$N$ is the notional of that instrument needed to match the liabilities'
sensitivity exactly.

## Why this node exists

Without matching the hedge notional to the liabilities' own rate and inflation
sensitivity, a scheme that looks fully funded against today's yields can find
itself underfunded the moment rates fall, since the liabilities then grow
faster than an unmatched or partially matched asset book.
