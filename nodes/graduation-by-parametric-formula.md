---
id: graduation-by-parametric-formula
title: Graduation by parametric formula
domains: [life]
status: drafted
requires: [graduation-rationale]
spends:
  - {object: obj.hazard, domain: life}
anchor: [ifoa.cs2.4.5-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Graduation by parametric formula fits a mathematical law directly to the crude mortality data,
choosing the law's parameters to minimise the deviation between the fitted and the crude rates.
The fitted rates are smooth by construction, since the formula itself has no room for the
sampling noise a crude rate carries.

## The expression

$$
\mu_x = A + B c^{x}
$$

Here $\mu_x$ is the force of mortality at age $x$, $A$ is an age-independent component covering
causes such as accidental death, and $B$ and $c$ govern the exponential rise in mortality with
age that this Gompertz-Makeham law assumes. The three parameters are usually fitted by maximum
likelihood or by minimising a weighted sum of squared deviations from the crude rates across
the ages graduated.

## Why this node exists

A formula compresses an entire graduated mortality curve into a handful of fitted parameters, so
a rate at any age is recovered by evaluating the formula, with no full table to store. That
compactness is bought at a cost: the fitted curve can only take the shape the chosen law allows,
however the crude data itself behaves, which is the smoothness-against-fidelity trade every
graduation method makes differently.
