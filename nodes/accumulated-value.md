---
id: accumulated-value
title: Accumulated value
domains: [actuarial]
status: drafted
requires: [interest-discount-relationship]
spends: []
anchor: [ifoa.cm1.1.2-1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The accumulated value of a sum invested for a term is the amount it grows to under
a stated rate of interest, compounding the principal over each period it remains
invested.

## The expression

$$
A = P(1+i)^n
$$

Here $P$ is the principal invested, $i$ is the effective annual rate of interest,
$n$ is the term in years, and $A$ is the accumulated value at the end of that term.

## Why this node exists

A model cannot compare a payment made now with a payment made later until it can
say what one becomes by the date of the other, and accumulation is that
conversion run forward in time. Present value needs it next, since present value is
the same relationship read in reverse, discounting the accumulated value back to
the principal that would produce it.
