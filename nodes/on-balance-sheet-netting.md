---
id: on-balance-sheet-netting
title: On-balance-sheet netting
domains: [credit]
status: drafted
requires: []
spends: []
anchor: [assa.f107.6.1-6-6]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

On-balance-sheet netting offsets a customer's deposit balance against their loan balance with
the same bank, reducing the exposure recognised for capital purposes, where a legal right of
set-off allows the two to be combined.

## The expression

$$
E_{\text{net}} = \max(L - D, 0)
$$

Here $L$ is the customer's outstanding loan balance, $D$ is the customer's deposit balance held
with the same bank, and $E_{\text{net}}$ is the net exposure recognised once the deposit is set
against the loan. The maximum keeps the recognised exposure from falling below zero where the
deposit exceeds the loan.

## Why this node exists

Without a right of set-off, a bank would hold capital against the full loan balance even where
the same customer's deposit with it would absorb most of a default, overstating the loss the
bank is actually exposed to. Netting corrects that overstatement wherever the legal right to
combine the two balances genuinely exists, and it does so only for that customer's own accounts
rather than across unrelated exposures.
