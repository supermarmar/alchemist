---
id: loan-behavioural-tenor
title: Loan behavioural tenor
domains: [credit, fin-man]
status: drafted
requires: [prepayment-behaviour-modelling]
spends: []
anchor: [assa.f107.10.3-2]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

A loan's behavioural tenor is the weighted average time to repayment implied by its expected
principal cash flows once observed prepayment behaviour is built into the schedule, used in
place of the loan's contractual maturity for liquidity risk purposes.

## The expression

$$
WAL = \frac{\sum_{t=1}^{T} t \cdot CF_t}{\sum_{t=1}^{T} CF_t}
$$

Here $T$ is the loan's contractual final maturity, $CF_t$ is the principal cash flow expected
in period $t$ once the assumed prepayment rate is applied to the contractual amortisation
schedule, and $WAL$ is the behavioural tenor: each period's principal repayment weighted by how
far away it falls, divided by the total principal repaid. A loan with faster assumed
prepayment concentrates more of $CF_t$ into earlier periods, which pulls $WAL$ below the
contractual maturity $T$.

## Why this node exists

A liquidity projection built on contractual maturities assumes every borrower repays exactly
on schedule, which understates how quickly a loan book that prepays ahead of schedule actually
returns cash to the bank. Weighting each period's principal by how far away it falls turns the
prepayment assumption into a single effective maturity a liquidity model can use directly. The
behaviouralisation exercise needs it next, since re-estimating a bank's prepayment assumptions
against fresh data is only worth doing because a behavioural tenor built on stale assumptions
would already be feeding the wrong figure into every liquidity model that depends on it.
