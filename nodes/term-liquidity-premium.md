---
id: term-liquidity-premium
title: Term liquidity premium
domains: [fin-eng, fin-man]
status: drafted
requires: [deposit-pricing-considerations, funds-transfer-pricing]
spends: []
anchor: [assa.f107.5.2-3, assa.f207.4.4-1, assa.f207.4.4-2, assa.f207.4.4-6, assa.f207.4.4-7, assa.f207.4.5-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The term liquidity premium is the extra rate a bank must pay, over the rate on an instantly
accessible deposit of the same credit quality, to secure funding committed for a fixed term.

## The expression

$$
\pi_{\text{term}} = r_{\text{ftp}}(\tau) - r_{\text{ftp}}(0)
$$

Here $r_{\text{ftp}}(\tau)$ is the internal transfer rate assigned to funding committed for
term $\tau$, $r_{\text{ftp}}(0)$ is the transfer rate assigned to funding available on demand,
and $\pi_{\text{term}}$ is the term liquidity premium between them, rising with $\tau$ because
longer-dated funding lets the bank rely on it through a longer stress window before it must be
refinanced.

## Why this node exists

Funds transfer pricing charges a lending or deposit-gathering unit against an internal curve,
so that curve has to reflect the term commitment behind the funding as well as its rate. The
term liquidity premium is the increment the curve adds for tenor alone, holding credit quality
fixed. A bank that ignored it would price a five-year fixed deposit no differently from an
overnight one, leaving it with no reward for gathering the longer, stickier funding its own
liquidity buffer depends on.
