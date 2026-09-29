---
id: actuarial-investigation
title: Actuarial investigation
domains: [actuarial, gi]
status: drafted
requires: [general-insurance-data-quality]
spends: []
anchor: [ifoa.sp7.5.2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

An actuarial investigation measures how far actual experience over a period departed
from what the assumptions used to price or reserve for that period predicted, summarised
as the ratio of actual to expected.

## The expression

$$
AE = \frac{\sum_i \text{Actual}_i}{\sum_i \text{Expected}_i}
$$

Here $AE$ is the actual-to-expected ratio for the investigation, $\text{Actual}_i$ is the
observed outcome, such as claims or deaths, for exposure cell $i$, and $\text{Expected}_i$
is the outcome that cell's assumptions predicted. A ratio above one means the assumptions
understated the experience being investigated, and a ratio below one means they
overstated it.

## Why this node exists

A pricing or reserving assumption that is never checked against what actually happens
drifts silently out of line with the business it is meant to describe, and the
actual-to-expected ratio is what turns that drift into a single monitored number. The
consequence of skipping the investigation is that a stale assumption keeps feeding
capital and reserving calculations long after the experience behind it has moved.
