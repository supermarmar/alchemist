---
id: liquidity-risk-factor
title: Liquidity risk factor
domains: [fin-man]
status: drafted
requires: [sources-of-liquidity]
spends: []
anchor: [assa.f107.10.1-3-4]
vault_articles: [regulation/bcbs-liquidity-coverage-ratio-original]
vault_sources: []
taught_in: null
---

## Definition

A liquidity risk factor scales an asset's market value, or a funding line's committed amount,
down to the value it could actually realise in stress, reflecting how far a forced or rapid
conversion to cash falls short of the asset's quoted or nominal value.

## The expression

$$
V^{\mathrm{adj}} = V \cdot (1 - h)
$$

Here $V$ is the asset's market value or the funding line's committed amount, $h$ is the
liquidity risk factor, a haircut between zero and one set by how readily that item converts to
cash under stress, and $V^{\mathrm{adj}}$ is the value the bank can count on in its liquidity
position. An asset with a low, well-established market depth carries a small $h$, and one that
is harder to sell quickly without moving its price carries a larger one.

## Why this node exists

Treating every asset and funding line at its full quoted value would overstate a bank's
capacity to meet outflows in a stress scenario, since a stressed market rarely absorbs a large
sale at the price quoted the day before. The liquidity risk factor corrects for that gap
directly, and it is what turns a bank's raw balance sheet into the stressed liquidity position
a liquidity ratio or a stress test actually needs to measure.
