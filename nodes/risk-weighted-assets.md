---
id: risk-weighted-assets
title: Risk-weighted assets
domains: [credit, fin-man, regulation]
status: drafted
requires: []
spends:
  - {object: obj.exposure, domain: credit}
anchor: [assa.f107.1.10-4]
vault_articles: [regulation/eu-crr-2013-credit-risk]
vault_sources: []
taught_in: null
---

## Definition

Risk-weighted assets rescale a bank's exposures by a risk weight reflecting how
risky each one is, so that a large but safe exposure and a small but risky one can
be compared on the same footing. The rescaled total is the denominator against
which every regulatory capital ratio is measured.

## The expression

$$
\mathrm{RWA} = \sum_{i=1}^n \mathrm{RW}_i \times \mathrm{EAD}_i
$$

Here $\mathrm{EAD}_i$ is the exposure at default on exposure $i$, $\mathrm{RW}_i$
is the risk weight assigned to it, whether prescribed by the standardised approach
or produced by an internal ratings-based model, and $\mathrm{RWA}$ is the sum of
the two multiplied across every exposure in the book.

## Why this node exists

A regulatory capital ratio has no meaning until its denominator exists, since
capital held against a portfolio of unweighted exposures says nothing about
whether that capital matches the risk actually run. Determining capital
requirements from risk parameters needs this node next, because converting a
bank's own PD, LGD and EAD estimates into a capital figure is exactly the risk
weight this node applies, made explicit.
