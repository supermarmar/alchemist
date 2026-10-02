---
id: stop-loss-pricing
title: Stop loss pricing
domains: [gi]
status: drafted
requires: [reinsurance-product]
spends: []
anchor: [ifoa.sp8.4.5-4]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

Stop loss pricing sets a reinsurance premium for cover that responds once a cedant's aggregate
losses across a whole account exceed a stated retention, so the price depends on the combined
shape of the account's loss experience above that point.

## The expression

$$
P = (1+\theta)\, E\bigl[(S - M)_{+}\bigr]
$$

Here $S$ is the cedant's aggregate loss for the account over the period, $M$ is the retention
above which the cover responds, $(S-M)_+$ denotes $\max(S-M,0)$, $\theta$ is the loading the
reinsurer adds to the expected recovery, and $P$ is the resulting stop loss premium.

## Why this node exists

A stop loss layer responds to the account's combined experience over the period, so pricing it
depends on the shape of the whole aggregate loss distribution above the retention. That
distribution is rarely observed directly, so it is usually built up by fitting a compound
distribution, or a suitable parametric proxy, to the account's historical loss ratios before
the expected excess above the retention is evaluated. The loading $\theta$ is where the
reinsurer prices the residual uncertainty in that fitted distribution, since a stop loss
layer's payout is far more volatile, relative to its expected value, than a proportional share
of the same account would be.
