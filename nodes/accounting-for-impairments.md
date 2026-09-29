---
id: accounting-for-impairments
title: Accounting for impairments
domains: [fin-man, regulation]
status: drafted
requires: []
spends: []
anchor: [assa.f107.1.9-4]
vault_articles: [concepts/ifrs9-expected-credit-loss]
vault_sources: []
taught_in: null
---

## Definition

Impairment is the accounting recognition that a loan or other financial asset is worth
less than the amount at which it is carried, measured under IFRS 9 as an expected credit
loss allowance rather than as a loss triggered only once a default has occurred.

## The expression

$$
\mathrm{ECL} = \mathrm{PD} \times \mathrm{LGD} \times \mathrm{EAD}
$$

Here $\mathrm{ECL}$ is the expected credit loss allowance a bank must hold against an
exposure, $\mathrm{PD}$ is the probability that exposure defaults over the horizon the
stage calls for, $\mathrm{LGD}$ is the proportion of the exposure not expected to be
recovered given that default, and $\mathrm{EAD}$ is the exposure amount at the point of
default. IFRS 9 sets the horizon by stage: twelve months where credit risk has not
increased significantly since origination, and the instrument's remaining lifetime once it
has.

## Why this node exists

A bank cannot report a true financial position while it waits for a default to occur
before recognising the loss that default makes likely. Expected credit loss brings that
recognition forward, and the size of the allowance it produces is what shows up on the
balance sheet as an impaired asset, which needs this node next.
