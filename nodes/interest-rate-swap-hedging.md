---
id: interest-rate-swap-hedging
title: Interest rate swap hedging
domains: [fin-eng]
status: drafted
requires: [swaps-hedging]
spends: []
anchor: [assa.f207.2.4-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A bank hedges the rate basis of an asset or liability by entering an interest rate swap whose
floating leg is referenced to the same rate, so that the floating cash flows on the hedged
position and on the swap cancel, leaving the bank paying or receiving only the swap's fixed
rate.

## The expression

$$
N_t = -r^{L}_t \cdot F - r^{\mathrm{fix}} \cdot F + r^{\mathrm{float}}_t \cdot F = -r^{\mathrm{fix}} \cdot F, \qquad r^{L}_t = r^{\mathrm{float}}_t
$$

Here $F$ is the notional common to the hedged position and the swap, $r^{L}_t$ is the floating
rate paid on the hedged liability in period $t$, $r^{\mathrm{fix}}$ is the fixed rate the bank
pays on the swap, $r^{\mathrm{float}}_t$ is the floating rate the bank receives on the swap,
and $N_t$ is the bank's net cash outflow in period $t$. Where the swap's floating leg is
referenced to the same rate as the liability, $r^{L}_t$ and $r^{\mathrm{float}}_t$ are equal
every period, so they cancel and $N_t$ reduces to the fixed rate alone: the swap has converted
a floating-rate liability into one whose cost no longer moves with the reference rate.

## Why this node exists

A bank whose assets and liabilities reset on different rate bases carries a net interest
income that moves whenever the two bases diverge, and closing out the underlying loan or
deposit book to fix that mismatch is rarely practical at the scale or speed a treasury desk
needs. An interest rate swap changes the rate basis without touching the underlying position,
which is what makes it the standard instrument a bank's treasury holds for moving net interest
rate exposure towards its target.
