---
id: liquidity-coverage-ratio
title: Liquidity coverage ratio
domains: [fin-man, regulation]
status: drafted
requires: []
spends: []
anchor: [assa.f107.10.4-2, assa.f107.2.3-8, assa.f207.6.2-1]
vault_articles: [regulation/bcbs-liquidity-coverage-ratio-original]
vault_sources: []
taught_in: null
---

## Definition

The liquidity coverage ratio measures whether a bank holds enough high-quality
liquid assets to survive a 30-day stress without recourse to emergency funding,
and Basel III requires it to stay at or above 100 per cent.

## The expression

$$
LCR = \frac{HQLA}{NCO_{30}} \ge 100\%
$$

Here $HQLA$ is the stock of high-quality liquid assets, unencumbered assets that
can be converted to cash rapidly and reliably even under stress, and $NCO_{30}$ is
the total net cash outflow projected over the standardised 30-day stress scenario,
combining an idiosyncratic shock to the bank's own funding with a market-wide
shock to funding conditions generally.

## Why this node exists

A bank can be solvent and still fail if it cannot convert what it holds into cash
fast enough to meet a run, and the ratio exists to make that separate failure mode
measurable. High-quality liquid assets needs this ratio next, since it is what
defines the numerator the asset eligibility rules are built to populate.
