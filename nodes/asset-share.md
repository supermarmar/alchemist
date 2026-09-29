---
id: asset-share
title: Asset share
domains: [life]
status: drafted
requires: [with-profits-contract]
spends: []
anchor: [ifoa.sp2.2.2-2, up.lew700.3]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The asset share of a with-profits policy is the accumulated value of the premiums it has
paid, invested at the insurer's actual experience and reduced by its actual charges and
claims cost, built up one period at a time; it starts at zero at the policy's outset.

## The expression

$$
AS_t = \bigl(AS_{t-1} + P_t - E_t\bigr)(1 + i_t) - Q_t \, C_t
$$

Here $AS_t$ is the asset share at the end of period $t$, $P_t$ is the premium received
during the period, $E_t$ is the expense charged, $i_t$ is the insurer's actual investment
return earned over the period, $Q_t$ is the probability of a claim arising in the
period, and $C_t$ is the cost of that claim. Each term is drawn from the insurer's own realised
experience over the period, in contrast with the assumptions loaded into the premium.

## Why this node exists

A with-profits contract promises to distribute a surplus the insurer actually earns, and
the asset share is what measures that surplus policy by policy, so bonuses can be
declared against something realised rather than a figure fixed in advance. With-profits
surplus distribution needs it next, since a bonus scale is set by comparing the asset
share against the policy's guaranteed benefits.
