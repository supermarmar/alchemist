---
id: filtration
title: Filtration
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.sp6.3.2-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A filtration is the increasing sequence of information sets available to an observer as time
passes. A process is adapted to a filtration when its value at each time is known given the
information available at that time, which is the condition a process must meet to represent
something an observer can see at that time.

## The expression

$$
\mathcal{F}_s \subseteq \mathcal{F}_t \subseteq \mathcal{F}, \qquad 0 \le s \le t \le T
$$

Here $\mathcal{F}_t$ is the sigma-algebra of events known by time $t$, $\mathcal{F}$ is the full
sigma-algebra of events knowable by the terminal time $T$, and the nesting $\mathcal{F}_s
\subseteq \mathcal{F}_t$ for $s \le t$ states that no information already known is ever forgotten
as time moves forward.

## Why this node exists

A stochastic model that let a process depend on information not yet available would be using
the future as an input, and the filtration makes that distinction precise enough to enforce.
The previsible process needs this node next, since a previsible process is one whose value is
known one step earlier than the filtration that adaptedness alone would allow.
