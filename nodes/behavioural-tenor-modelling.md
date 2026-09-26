---
id: behavioural-tenor-modelling
title: Behavioural tenor modelling
domains: [fin-eng, fin-man]
status: drafted
requires: [funds-transfer-pricing]
spends: []
anchor: [assa.f207.4.3-2]
vault_articles: [concepts/eve-and-nii]
vault_sources: []
taught_in: null
---

## Definition

Behavioural tenor modelling replaces the contractual maturity of a deposit or lending
facility with the tenor customers actually behave to, which matters most for a balance with
embedded optionality such as a non-maturity deposit or a prepayable loan that carries no
fixed repricing date of its own.

## The expression

$$
\bar{t} = \sum_i w_i \, t_i
$$

Here $\bar{t}$ is the weighted average behavioural tenor assigned to the balance, $t_i$ is
the repricing or run-off tenor of bucket $i$ in the behavioural profile, and $w_i$ is the
share of the balance allocated to that bucket, with the shares summing to one. A supervisor
reviewing this assumption typically caps $\bar{t}$ for the aggregate non-maturity deposit
book, since an unbounded average tenor would let a bank understate its own repricing risk.

## Why this node exists

Funds transfer pricing charges each business unit for the funding it uses, and a facility
with no contractual repricing date cannot be charged correctly until something stands in for
that date. Getting the behavioural tenor wrong misprices every facility built on it, since
too long a tenor understates the true cost of funding a balance that could reprice sooner
than assumed.
