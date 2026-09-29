---
id: basel-iii-revised-minimum-capital-requirements
title: Basel III revised minimum capital requirements
domains: [fin-man, regulation]
status: drafted
requires: [basel-iii-tier-1-and-tier-2-redefinition]
spends: []
anchor: [assa.f107.2.3-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Basel III's revised minimum capital requirements set the lowest ratios of Common Equity Tier
1, Tier 1, and total capital a bank must hold against its risk-weighted assets, each ratio
computed on the redefined, higher-quality capital measures Basel III introduced after the
financial crisis.

## The expression

$$
\frac{\mathrm{CET1}}{\mathrm{RWA}} \ge 4.5\%, \qquad \frac{\mathrm{T1}}{\mathrm{RWA}} \ge 6\%,
\qquad \frac{\mathrm{Total\ capital}}{\mathrm{RWA}} \ge 8\%
$$

Here $\mathrm{CET1}$, $\mathrm{T1}$, and total capital are the three tiers of regulatory
capital, each nested inside the next so that CET1 sits within T1 and T1 sits within total
capital, and $\mathrm{RWA}$ is the bank's total risk-weighted assets. All three ratios must be
met at once, so the binding constraint is whichever tier's capital is scarcest relative to its
own minimum.

## Why this node exists

These three ratios are minima only, and a bank holding capital at exactly the minimum has no
room to absorb a downturn without breaching it. The capital conservation buffer needs this
node next, since it is defined as an additional layer of Common Equity Tier 1 sitting on top
of the 4.5% minimum this node fixes.
