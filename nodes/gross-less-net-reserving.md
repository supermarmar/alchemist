---
id: gross-less-net-reserving
title: Gross less net reserving
domains: [gi]
status: drafted
requires: [chain-ladder, reinsurance-product]
spends: []
anchor: [ifoa.sp7.5.6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The gross less net method reserves the direct business and the expected reinsurance
recoveries on it as two separate projections, then takes the net reserve as the difference
between them.

## The expression

$$
R_{\mathrm{net}} = R_{\mathrm{gross}} - R_{\mathrm{RI}}
$$

Here $R_{\mathrm{gross}}$ is the reserve projected from the gross claims triangle,
$R_{\mathrm{RI}}$ is the reserve projected from the reinsurance recoveries triangle, each
found by chaining development factors as the chain ladder method sets out, and
$R_{\mathrm{net}}$ is the reserve the insurer carries after allowing for the recoveries it
expects to collect. Projecting the two triangles separately lets each be developed against
its own pattern, since gross claims and reinsurance recoveries do not generally develop at
the same speed.

## Why this node exists

A reinsurance programme changes how quickly and how completely a claim reaches its ultimate
value on the insurer's own books, and a single net triangle would blend that reinsurance
effect into the development pattern in a way that is hard to isolate later. Reserving the
gross and reinsurance triangles apart, and only subtracting at the end, keeps each
development pattern legible and lets the reinsurance recovery assumption be revisited on its
own without disturbing the gross reserve underneath it.
