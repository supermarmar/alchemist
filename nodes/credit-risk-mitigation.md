---
id: credit-risk-mitigation
title: Credit risk mitigation
domains: [credit, fin-man, regulation]
status: drafted
requires: [pillar-3-market-discipline, standardised-approach-credit-risk]
spends: []
anchor: [assa.f207.1.9-3, bcbs.d424.sa.para-117, ifoa.sp9.6.4]
vault_articles: [regulation/crr-credit-risk-provisions]
vault_sources: []
taught_in: null
---

## Definition

Credit risk mitigation reduces the credit risk of an exposure through methods other than
securitisation or a credit default swap, chiefly financial collateral, guarantees, netting and
credit insurance, each substituting or offsetting the risk the exposure would otherwise carry in
full.

## The expression

$$
E^{*} = \max\bigl(0,\ E(1+H_e) - C(1-H_c-H_{fx})\bigr)
$$

Here $E^{*}$ is the exposure value after mitigation is recognised, $E$ is the exposure before
mitigation and $H_e$ its own volatility haircut, $C$ is the collateral's value, and $H_c$ and
$H_{fx}$ are haircuts applied to the collateral for its own price volatility and for any
currency mismatch between the exposure and the collateral. The adjusted exposure $E^{*}$ then
enters the capital calculation at the risk weight of the counterparty, and not of the
collateral.

## Why this node exists

An exposure secured by collateral or backed by a guarantee genuinely carries less risk than an
unsecured one, and a capital framework that ignored that difference would charge capital against
risk the bank has already reduced. Guarantees needs this comprehensive approach next, since a
guarantee is priced by the alternative route of substituting the guarantor's own risk weight for
the obligor's, and a bank choosing between collateral and a guarantee for the same exposure is
choosing between the two mitigation routes this node sets out.
