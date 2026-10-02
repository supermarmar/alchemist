---
id: internal-models-approach-market-risk
title: Internal models approach for market risk
domains: [fin-eng, regulation, stats]
status: drafted
requires: [value-at-risk]
spends: []
anchor: [assa.f107.7.6-2]
vault_articles: [regulation/frtb-minimum-capital-market-risk]
vault_sources: []
taught_in: null
---

## Definition

Under the internal models approach, a bank's market risk capital charge is set from its own
Value at Risk model, taken as the greater of the previous day's VaR and a multiplier applied
to the recent average VaR, with the multiplier itself set by how well the model has performed
in backtesting.

## The expression

$$
MRC_t = \max\left( VaR_{t-1}, \ k_t \cdot \frac{1}{60} \sum_{i=1}^{60} VaR_{t-i} \right) + SRC_t
$$

Here $VaR_{t-1}$ is the bank's own Value at Risk figure from the previous trading day, the
average term is the mean of the last sixty daily VaR figures, $SRC_t$ is the specific risk
charge covering issuer-specific risk the general VaR measure does not capture, and $MRC_t$ is
the resulting market risk capital charge. $k_t$ is the backtesting multiplier: it starts at a
supervisory floor and rises as the bank's count of backtesting exceptions, the days on which
realised losses exceeded the model's VaR estimate, climbs through the supervisor's green,
amber and red zones, so a model that keeps failing its own predictions is charged more capital
for the privilege of using them.

## Why this node exists

Requiring every bank to hold capital against a supervisor's own standardised charge takes no
account of how a specific trading book is actually diversified, and a bank whose internal
model genuinely captures that diversification would be forced to hold capital well above what
its own risk actually warrants. Tying the capital charge to the bank's own VaR model, subject
to supervisory approval and a backtesting penalty that punishes an unreliable model, lets
capital track a book's real risk while keeping the incentive to misstate that risk in check.
The fundamental review of the trading book needs this measure next, since it replaces the VaR
figure at its centre with an expected shortfall calculated at a higher confidence level.
