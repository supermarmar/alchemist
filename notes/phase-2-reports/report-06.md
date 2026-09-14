# Phase 2 batch 6 report

40 nodes worked. 5 attached, 35 uncovered.

## Attached

**capital-measurement-tlac-regulation** -> `regulation/fsb-tlac-gone-concern-loss-absorption`. The article treats the FSB TLAC standard directly, including its calibration in RWA and leverage-ratio terms and its explicit distinction from going-concern regulatory capital, which is the node's own subject (how capital measurement connects to TLAC and the wider regulatory capital framework).

**capital-requirement-by-risk-type** -> `regulation/solvency-ii-scr-standard-formula`. The article's own content is the SCR standard formula's modular decomposition (underwriting, market, counterparty default, operational) aggregated into the BSCR before the overall SCR, which mirrors the node's description of a capital model assessing distinct risk types separately before combining them. Regulatory rather than a generic actuarial-practice framing, but the mechanism itself is a direct match.

**capital-target-setting** -> `regulation/pra-icaap-and-pillar-2`. The PRA Buffer (Pillar 2B) section states exactly the node's subject: capital planning under stress establishes the buffer needed above the regulatory minimum to avoid a breach.

**categorical-encoding** -> `methods/ols-risk-factor-encoding`. Covers ordinal, one-hot and nested-dummy encoding with the same sparsity/instability concern the node raises, at the depth a Phase 3 writer needs.

**chain-ladder** -> `methods/chain-ladder-reserving`. Opens by stating the mechanism itself (extrapolating a triangle along age-to-age development factors) before its statistical foundations; direct treatment.

## Uncovered, with the strongest candidate rejected

**capital-management-strategy**: considered `regulation/pra-icaap-and-pillar-2` (use test, capital planning, allocation) but rejected; the general "tying together targets/allocation/strategic plan" framing versus the article's specific UK regulatory-compliance angle felt too diffuse a match, unlike the tighter mechanism-level fit for capital-target-setting.

**capital-structure-and-cost-of-capital**: `regulation/solvency-ii-technical-provisions` and Solvency UK risk-margin articles use "cost of capital" as the Solvency II 6% risk-margin rate, an unrelated Solvency II mechanism, not corporate capital-structure theory (WACC/debt-equity choice).

**challenger-bank**: `concepts/bbb-small-business-finance-markets` cites challenger-bank market-share statistics but never treats the business model itself.

**central-clearing**: `regulation/margin-transparency-im-centrally-cleared` is CCP margin-transparency policy, assuming central clearing as background rather than explaining it.

**censoring**: `methods/lgd-survival-analysis` gives right-censoring a precise paragraph, but scoped to LGD recovery-data construction, not the general definition plus the life/credit/GI comparison the node needs.

**causal-masking**: the same lecture as the seeded attention-mechanism gap (`ucsc.dl-actuarial-2026.l10`) states the mechanism verbatim (masking future-position attention weights to zero) at p.30-31, but no wiki article treats it; `concepts/in-context-learning-tabular-actuarial-models` uses a structurally different masking (blocking target-to-target, not future-position) in one clause.

**catastrophe-reinsurance-pricing**: `methods/reinsurance-pricing` treats general XL exposure/experience rating in depth, but the node specifically wants catastrophe-model-driven pricing, which the article does not address.

**capital-versus-liquidity-distinction**: PRA ICAAP/ILAAP articles describe the two processes in parallel but never state why they are separate.

**chapman-kolmogorov-equations** and **central-limit-theorem**: only passing "Markov chain" mentions and no CLT hits at all in the vault.

Remaining 26 nodes (capital-modelling-approach/implementation, capital-performance-metrics, capital-project-appraisal, capital-risk, capital-structure-and-dividend-policy, cash-flow-hedge, cash-flow-modelling-budgeting, cash-shortfall, cashflow-model, cashflow-valuation, catastrophe-model-structure, catastrophe-risk, categorical-data-analysis, cauchy-riemann-equations, cauchys-integral-theorem, census-approximation, central-bank, central-bank-funding, central-exposed-to-risk, change-of-basis, change-of-measure, chaotic-systems-introduction, chi-square-goodness-of-fit-test, chi-square-independence-test) returned no plausible index or grep candidate at all: pure maths (complex analysis, chaos), actuarial exposure/mortality-investigation technique, or bank/GI management topics the vault's credit-risk focus does not reach.

## Notable ledger items

**cash-flow-hedge and cash-shortfall**: both anchor into the IFRS 9 standard text, already ingested at `vault/markdown/ifrs/ifrs9_standard.md`. Direct inspection confirms paragraphs B5.5.28-30 define "cash shortfall" almost verbatim against the node's own wording, and the Chapter 6 hedge-types list names "cash flow hedge" verbatim. Neither vault wiki article on IFRS 9 (`concepts/ifrs9-expected-credit-loss`, `regulation/ifrs9-financial-instruments`) covers either at this definitional level; both stay at the PD/LGD/EAD and general-effectiveness-testing altitude. One new ledger id, `iasb-ifrs9-standard-cash-shortfall-and-hedge-types`, status `ingested` (the gap is wiki-article scope, not acquisition).

**causal-masking**: extended the seeded `dl-actuarial-2026-l10-11-transformers` id (same lecture as attention-mechanism) rather than minting a new one; did not touch its existing note, to avoid discarding batch 1's reasoning via a field disagreement, so the causal-masking-specific reasoning lives only in this report.

**Two id collisions found and fixed during `--dry-run`**: `up-wst312-course-notes` and `up-wtw320-course-notes` were independently minted by batch 4 and batch 7 respectively for different chapters of the same course notes. Reused both ids, copied their fields verbatim, and added notes (neither carried one yet) rather than fragmenting the ledger.

**capital-project-appraisal**: anchors to five paragraphs across four UP courses (fbs122, fni700, ias282, ias712 twice). Took only the first-listed anchor (up.fbs122.8) as the ledger document per the brief's default rule rather than an entry per co-anchor; noted the simplification in the ledger entry itself.

## check.py

Last line: `1560 nodes, 13 paths, 0 failures` (all 11 checks report `ok`, run after the five attachments and 35 clears above).

## Ambiguities in the brief

None blocking. One judgement call worth flagging: for capital-requirement-by-risk-type and capital-target-setting, EU/UK regulatory articles (Solvency II SCR, PRA ICAAP) were attached to nodes anchored in generic actuarial/banking course material, on the basis that the article's own mechanism matches the node's description precisely even though the framing is jurisdiction-specific. This reads as consistent with the cover bar's "judge the article's own treatment" instruction, but a stricter reading (jurisdiction-specific compliance process versus a general concept) could reasonably reject both; flagging for the spot-read.
