---
id: illiquid-asset-index-construction
title: Constructing indices of illiquid assets
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp5.8.2-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An index built from illiquid assets relies on appraisal-based valuations that
update infrequently and smooth out true price movements, so the reported returns
understate volatility and true correlation with other markets. Desmoothing
recovers an estimate of the unobserved true return series from this smoothed
appraisal series.

## The expression

$$
r_t = \frac{R_t - (1-\alpha)\, r_{t-1}}{\alpha}
$$

Here $R_t$ is the observed, smoothed, appraisal-based return in period $t$, $r_t$
is the desmoothed estimate of the true return in period $t$, $r_{t-1}$ is the
previous period's desmoothed return, and $\alpha$ is the smoothing parameter
estimated from the autocorrelation of the observed series, with a value of
$\alpha$ close to zero indicating heavy appraisal smoothing.

## Why this node exists

An index that is not corrected this way looks less risky and less correlated
with listed markets than the underlying assets actually are, because appraisal
smoothing removes exactly the volatility a genuine market price would show. An
allocation decision built on the uncorrected index therefore overstates the
diversification benefit an illiquid asset class appears to offer, understating
the true risk the investor is taking on.
