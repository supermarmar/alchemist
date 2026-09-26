---
id: stock-market-indices
title: Stock market indices
domains: [fin-eng]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp5.8.2-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A stock market index tracks the aggregate price movement of a defined basket of constituent
shares, relative to a base date, according to a stated weighting and constituent-selection
methodology.

## The expression

$$
I_t = I_0 \times \frac{\sum_i p_{i,t}\, q_i}{\sum_i p_{i,0}\, q_i}
$$

Here $I_t$ is the index level at time $t$, $I_0$ is its level at the base date, $p_{i,t}$ is the
price of constituent $i$ at time $t$, and $q_i$ is the weight given to constituent $i$, fixed at
the base date. Setting $q_i$ to the number of shares in issue gives a market-capitalisation
weighted index, and setting it to a constant gives a price-weighted index instead.

## Why this node exists

An investor comparing a portfolio's return with the market as a whole needs a single summary
figure to compare it against, and the weighting choice embedded in that figure changes what the
comparison means: a market-capitalisation weighted index lets its largest constituents dominate
its movement, while a price-weighted index gives that influence to whichever shares happen to
trade at the highest price. Uses of investment indices needs this construction next, since
which use an index is put to, as a benchmark, as an investable product or as an economic
indicator, depends on which methodology built it.
