---
id: credit-concentration-risk
title: Credit concentration risk
domains: [credit, regulation]
status: drafted
requires: [credit-risk]
spends: []
anchor: [assa.f107.1.12-6, assa.f207.1.8-1]
vault_articles: [methods/credit-risk-concentration-bcbs]
vault_sources: []
taught_in: null
---

## Definition

Credit concentration risk is the risk that a portfolio insufficiently diversified across
borrowers, sectors or geographies suffers a loss the portfolio's average default rate alone
would not predict, because a common factor drives defaults together across the concentrated
cluster.

## The expression

$$
\mathrm{HHI} = \sum_i s_i^2
$$

Here $s_i$ is obligor or sector $i$'s share of total portfolio exposure, and $\mathrm{HHI}$ is
the Herfindahl-Hirschman Index, which rises towards one as exposure concentrates in fewer
names and falls towards zero as it spreads evenly across many. The Basel Committee's
granularity adjustment approximates the extra capital a concentrated portfolio needs above the
asymptotic single-risk-factor formula as proportional to this index.

## Why this node exists

The internal ratings-based capital formula assumes a portfolio granular enough that no single
exposure carries material weight, and a real book with a few large exposures or a sector tilt
breaks that assumption in a way the formula itself does not capture. Risk concentration needs
this measure settled before it can decide, at the level of the whole risk-taking
organisation, how much capital or limit headroom to hold against it.
