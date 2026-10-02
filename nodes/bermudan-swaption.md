---
id: bermudan-swaption
title: Bermudan swaption
domains: [fin-eng]
status: drafted
requires: [swaption]
spends: []
anchor: [ifoa.sp6.2.5-14]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A Bermudan swaption grants the holder the right to enter the underlying swap on any one of a
specified set of exercise dates, so its price depends on the whole term structure of interest
rates behind every one of those dates.

## The expression

$$
V(t_k) = \max\Bigl(\mathrm{Exercise}(t_k),\ \mathbb{E}^{Q}\bigl[DF(t_k, t_{k+1})\, V(t_{k+1}) \mid \mathcal{F}_{t_k}\bigr]\Bigr)
$$

Here $V(t_k)$ is the swaption's value at exercise date $t_k$, $\mathrm{Exercise}(t_k)$ is the
value received if the holder exercises at $t_k$, $DF(t_k, t_{k+1})$ discounts from the next
exercise date back to $t_k$, and $\mathbb{E}^{Q}[\,\cdot \mid \mathcal{F}_{t_k}]$ is the
risk-neutral expectation conditional on what is known at $t_k$. Working backwards from the
final exercise date fixes $V$ at every earlier date in turn, which is why pricing a Bermudan
swaption needs a full term structure model to run that recursion across.

## Why this node exists

A European swaption's price answers what one exercise opportunity is worth, but a bank that
holds the right to cancel a swap on any of several future dates is holding something richer,
and undervaluing that right by pricing it as European leaves the true cost of the embedded
optionality unrecognised. The comparison exposes what a single-date model cannot express: the
value of the timing choice itself, since the holder chooses which of several available dates
to exercise on.
