---
id: credit-facility-drawdown-profile
title: Facility drawdown profile
domains: [credit]
status: drafted
requires: []
spends:
  - {object: obj.exposure, domain: credit}
anchor: [assa.f107.6.1-6-3]
vault_articles: [methods/ifrs9-ead-ccf-modelling]
vault_sources: []
taught_in: null
---

## Definition

A committed credit facility's drawdown profile describes how much of the undrawn
commitment converts to drawn exposure as a borrower's circumstances change, which
matters most in the run-up to default, when a borrower under stress tends to draw down
whatever headroom remains.

## The expression

$$
\mathrm{EAD} = D + \mathrm{CCF} \times (L - D)
$$

Here $\mathrm{EAD}$ is the exposure at default, $D$ is the amount already drawn, $L$
is the total committed limit, so that $L-D$ is the undrawn commitment, and
$\mathrm{CCF}$ is the credit conversion factor, the proportion of that undrawn
commitment expected to be drawn before default.

## Why this node exists

An exposure measured only from what is drawn today understates what a lender is owed
once a borrower draws down its remaining headroom on the way to default, so
provisioning against today's balance alone understates the loss the facility can
produce. The credit conversion factor is what closes that gap, estimated behaviourally
from exactly the kind of drawdown histories this node's own object records.
