---
id: counterparty-credit-risk
title: Counterparty credit risk
domains: [credit, fin-eng, fin-man, life]
status: drafted
requires: [credit-risk]
spends:
  - {object: obj.exposure, domain: credit}
anchor: [assa.f107.1.12-5, assa.f107.2.3-3, assa.f107.6.3-1, assa.f207.2.2-4, ifoa.sp1.3.1-13, ifoa.sp2.3.1, ifoa.sp6.4.4-1, ifoa.sp9.3.2-1]
vault_articles: [regulation/counterparty-credit-risk-saccr]
vault_sources: []
taught_in: null
---

## Definition

Counterparty credit risk is the risk that the counterparty to a derivative or securities
financing transaction defaults before the final settlement of its cash flows, and it differs
from ordinary lending risk because both the exposure and the counterparty's credit quality can
move sharply and together.

## The expression

$$
\mathrm{EAD}_i = \alpha \, \bigl(RC_i + PFE_i\bigr)
$$

Here $\mathrm{EAD}_i$ is the exposure at default for netting set $i$ under the standardised
approach for counterparty credit risk, $RC_i$ is the replacement cost, what it would cost to
replace the netting set's transactions today, $PFE_i$ is the potential future exposure, an
add-on for how far exposure could still grow before default, and $\alpha$ is a supervisory
multiplier fixed at 1.4. Collateral reduces $PFE_i$ but can never bring $\mathrm{EAD}_i$ to
zero, since some gap risk between the last margin exchange and post-default replacement always
remains.

## Why this node exists

Ordinary lending exposure is fixed at the loan's outstanding balance, but a derivative's
exposure moves with the market and can be negative one day and large the next, so exposure
measurement has to capture that potential future movement rather than only today's mark. Once
that measured exposure is known, potential future exposure is the specific component this
formula needs estimated before the standardised approach can be applied.
