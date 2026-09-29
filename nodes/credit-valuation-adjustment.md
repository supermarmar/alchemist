---
id: credit-valuation-adjustment
title: Credit valuation adjustment
domains: [credit, fin-eng, regulation]
status: drafted
requires: [counterparty-credit-risk]
spends:
  - {object: obj.hazard, domain: credit}
  - {object: obj.survival, domain: credit}
anchor: [assa.f107.1.12-5, assa.f107.2.3-3, assa.f107.2.4-3, assa.f107.6.3-1, assa.f207.2.2-4, bcbs.d424.cva.para-1]
vault_articles: [concepts/credit-valuation-adjustment, regulation/bcbs-d507-cva-framework]
vault_sources: []
taught_in: null
---

## Definition

Credit valuation adjustment, CVA, is the reduction to a derivative's risk-free value that
reflects the counterparty's risk of defaulting before the derivative's cash flows are settled in
full, computed as the risk-neutral expected loss from that default across the derivative's life.

## The expression

$$
\mathrm{CVA} = (1-R)\int_0^{T} DF(t)\, EE(t)\, S(t)\, h(t)\, dt
$$

Here $R$ is the recovery rate assumed on the counterparty's debt, $DF(t)$ discounts a cash flow
at time $t$ back to today, $EE(t)$ is the expected positive exposure to the counterparty at $t$,
$S(t)$ is the counterparty's survival probability to $t$, and $h(t)$ is its hazard rate at $t$,
so $S(t)h(t)$ is the instantaneous rate at which default probability arrives at that instant.
Integrating this product over the derivative's life $T$ accumulates the expected loss from
default across every point at which it could occur.

## Why this node exists

Before the 2008 crisis, banks priced most derivatives as though the counterparty were certain
to perform, and industry-wide losses in the crisis came predominantly from mark-to-market
deterioration in this adjustment, which is why Basel III raised a specific capital charge
against CVA's own volatility. CVA
capital requirement scope needs this valuation next, since the capital charge is set against
exactly the quantity this integral defines.
