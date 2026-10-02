---
id: prepayment-behaviour-modelling
title: Modelling pre-payment behaviour
domains: [credit, fin-man, stats]
status: drafted
requires: [prepayment-risk]
spends: []
anchor: [assa.f107.10.2-3]
vault_articles: [regulation/eba-gl-2022-14-irrbb-csrbb]
vault_sources: []
taught_in: null
---

## Definition

Modelling prepayment behaviour forecasts the conditional prepayment rate a loan pool will
actually experience under a given interest rate scenario. The forecast scales a calibrated base
rate by a multiplier that speeds prepayment when rates fall and slows it when rates rise, since a
borrower's incentive to refinance moves with the gap between their existing rate and the rate on
offer.

## The expression

$$
\mathrm{CPR}_s = \mathrm{CPR}_{\mathrm{base}} \cdot m(s)
$$

Here $\mathrm{CPR}_{\mathrm{base}}$ is the conditional prepayment rate calibrated to historical
experience, $s$ indexes the interest rate scenario being modelled, $m(s)$ is the scenario
multiplier applied to that base rate, and $\mathrm{CPR}_s$ is the resulting prepayment rate
assumed under scenario $s$.

## Why this node exists

A pool's cash flows cannot be projected under a stressed rate environment from its historical
prepayment experience alone, since that experience was earned under whatever rate path actually
occurred. Loan behavioural tenor needs this node next, since a pool's effective repricing or
repayment date under a liquidity or interest rate risk model is built from exactly the
scenario-scaled prepayment rate this node produces.
