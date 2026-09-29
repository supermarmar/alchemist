---
id: surrender-value-calculation-methods
title: Surrender value calculation methods
domains: [life]
status: drafted
requires: [assurance-contract, discontinuance-terms-principles]
spends: []
anchor: [ifoa.sp2.2.4-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A surrender value is the amount an insurer pays a policyholder who discontinues a conventional
without-profits contract before maturity, calculated either from the reserve held against the
policy or by equating the contract's value immediately before and after the change.

## The expression

$$
SV_t = f_t \, {}_tV
$$

Here ${}_tV$ is the reserve held against the policy at duration $t$ under its valuation basis,
$f_t$ is the surrender factor, a proportion no greater than one, and $SV_t$ is the surrender
value paid at that duration. The factor $f_t$ typically rises toward one as the contract
approaches maturity, once most of the acquisition costs it is recouping have already been
recovered from earlier premiums.

## Why this node exists

A policyholder who discontinues early has already caused the insurer to incur acquisition
costs that the premium stream was meant to recover over the contract's full term, so paying
the full reserve on early exit would leave that shortfall uncovered. The surrender factor is
how the insurer shares the shortfall between the policyholder who leaves and the
policyholders who remain, and setting it too low invites the regulatory and reputational
scrutiny that fair discontinuance terms are designed to avoid.
