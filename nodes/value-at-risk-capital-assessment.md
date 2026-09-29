---
id: value-at-risk-capital-assessment
title: Value at risk capital assessment
domains: [life, regulation, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp1.4.4-1, ifoa.sp2.4.4-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Value at risk capital assessment sets solvency capital at the smallest loss a firm's
own loss distribution exceeds with no more than a stated small probability over a
stated horizon. Solvency II's one-year, 99.5 per cent calibration is the best-known
instance of the approach.

## The expression

$$
\mathrm{VaR}_\alpha(L) = \inf\{x : P(L > x) \le \alpha\}
$$

Here $L$ is the loss over the assessment horizon, $\alpha$ is the small probability
the firm accepts of exceeding the capital held, and $\mathrm{VaR}_\alpha(L)$ is that
capital: the smallest loss level whose exceedance probability is no greater than
$\alpha$.

## Why this node exists

A solvency regime cannot enforce a capital number until a rule fixes how much loss
that capital must absorb, and reading the loss distribution off at a quantile
supplies exactly that rule on a basis a supervisor can compare across firms.
Reserve and capital interplay needs this quantile next, since a firm's provisions
and its capital are read against the same loss distribution and only differ in
where along it each is set.
