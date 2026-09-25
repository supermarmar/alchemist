---
id: radon-nikodym-derivative
title: Radon-Nikodym derivative
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.3.3-5]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The Radon-Nikodym derivative is the random variable that converts an
expectation taken under one probability measure into the equivalent expectation
under another, equal to the ratio of the two measures' densities; it exists
only where the second measure assigns positive probability to every event the
first measure does.

## The expression

$$
E_Q[X] = E_P\left[X \frac{dQ}{dP}\right]
$$

Here $P$ and $Q$ are two probability measures on the same event space,
$\frac{dQ}{dP}$ is the Radon-Nikodym derivative of $Q$ with respect to $P$, and
$X$ is any random variable whose expectation is being restated under the new
measure $Q$.

## Why this node exists

Without a single object converting an expectation from one measure to another,
switching from the real-world measure to a risk-neutral one would require
re-deriving every expectation from first principles. Change of measure needs
this node next to formalise exactly that switch.
