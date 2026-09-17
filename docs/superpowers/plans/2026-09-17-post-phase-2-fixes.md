# Post Phase 2 fixes: four branches

Written 17 September 2026, after PR #8 merged, from four decisions Mario took that day and two
he retook once measurement contradicted the framing. The branches are independent in content and
sequenced only where one gates the next. One concern per pull request, per
`~/.claude/rules/git-conventions.md`.

## Global constraints

- Python is `.venv/bin/python`, never a system `python3`.
- The pre-commit hook runs `scripts/check.py` and validates the **working tree** rather than the
  index, so a branch never commits with a rule red.
- Explicit paths on `git add`. Never `git add -A` or `git add .`.
- Conventional Commits, imperative and lowercase, no trailing period, ending with
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- Never self-merge, never force-push `main`, never `--no-verify`.
- British English throughout, no em or en dashes as punctuation, currency written with the unit
  word.
- This repo is public. Nothing from a Gini engagement enters it.
- Baseline at `03eb6dc`: 1,560 nodes, 13 paths, 0 failures on eleven rules; 307 tests passing.

---

## Branch 1: `ci/gate-pull-requests` (G26 and G27)

Sequenced first, because it gates every pull request the three branches below raise.

**G26, Pages.** Every deploy since 4 September has failed at `actions/deploy-pages@v4` with
`HttpError: Not Found`, while the build step passed each time. Run 35237105901 names the cause:
"Ensure GitHub Pages has been enabled". The repository setting is Mario's to change, either in
Settings, Pages, source GitHub Actions, or by authorising
`gh api -X POST repos/supermarmar/alchemist/pages -f build_type=workflow`. Publishing exposes
nothing new, since `build_site.py` renders node bodies already committed to a public repository,
and checks 5 and 11 gate publishability on top of that. No commit belongs to this half.

**G27, checks on pull requests.** Add `.github/workflows/checks.yml`, triggered on
`pull_request`, running `scripts/check.py` and `pytest`. Leave `pages.yml` on push to `main`:
adding `pull_request` there would attempt a deploy from a branch. Today the pre-commit hook is
the only gate, which is why PR #8 merged with an empty status rollup.

**Done when:** a pull request shows both jobs, and one deploy run succeeds with
`https://supermarmar.github.io/alchemist/` resolving.

---

## Branch 2: `fix/anchor-defects-and-audit`

Four defects are known, all found by Phase 2 agents and verified against primary text:
`corporate-exposure-risk-weights` cites `bcbs.d424.sa.para-37`, which is securities firms rather
than corporates (38 to 43); `downturn-lgd-estimation` cites para 229, which is PD estimation;
`ead-quantification-standards` cites para 241, the bare EAD definition rather than the
quantification standards; and `dropout`'s anchor lecture cites Srivastava only in a bibliography.
The pilot's l01 node is **not** a fifth, since `notes/l01-anchor-finding-2026-09-14.md` rules that
anchor sound.

**No twelfth check.** An existence rule would have caught none of the four. d424's paragraph
numbers restart at every section, so "37." appears at four places in
`vault/markdown/bcbs/bcbs_d424.md` (lines 487, 2557, 5199 and 6370), and 229 and 241 are present
too. Every bad anchor cites a number that exists. The eleven checks stay eleven, and no document
needs renumbering.

**Build `scripts/anchor_audit.py` instead.** A topic-overlap probe, reporting rather than gating,
scoring each verifiable anchor by how much of its node's subject vocabulary appears in the cited
section and printing the weakest first. It is the technique that surfaced all four, and it has no
false-positive cost because a human reads the ranking. Scope it to what the vault can verify
today: bcbs (143 references, against `markdown/bcbs/bcbs_d424.md`) and ucsc (96, against
`markdown/courses/`). ifoa (1,065), assa (483), up (408) and iasb (55) point at material nobody
holds, so the script reports them as unverifiable rather than passing them silently. Re-run it
once that material is acquired.

**Order within the branch:** corrections first, so the eleven rules stay green at every commit,
then the script, then `notes/anchor-audit-2026-09.md` carrying the ranking and the corrections.

**Done when:** the four are corrected against primary text read directly rather than through a
subagent summary, per `~/.claude/rules/subagent-verification.md`; the audit runs over all 239
verifiable references; `check.py` is clean and the suite has not shrunk.

**Say plainly in the note:** every defect found so far sits inside the verifiable tenth of the
corpus, which is selection bias rather than evidence the other nine tenths are clean. At the two
per cent the verifiable tenth shows, 2,250 references would carry about 47 bad anchors.

---

## Branch 3: `fix/l01-attachments-and-ledger`

Eight of the twelve nodes anchored at `ucsc.dl-actuarial-2026.l01` already carry a public vault
article. Only `age-period-cohort`, `censoring`, `multiple-decrement` and `outcome-window` have an
empty `vault_articles`, so the prize here is four nodes rather than twelve.

**Step 1, re-check the vault before ingesting anything.** Read the four nodes against the public
candidates already present: `methods/lgd-survival-analysis` and
`methods/survival-analysis-macroeconomic-pd` for censoring, `methods/mortality-modelling` and
`methods/breeden-2016-lifecycle-environment-loan-level-forecasts` for age-period-cohort,
`methods/collections-treatment-optimisation` for the outcome window. The bar is the one the waves
used: a reader could draft the node from it, rather than a passing mention. A T1 or T2 public
article beats a self-authored T5 recast wherever both cover the node. Check the owning batch
report under `notes/phase-2-reports/` first, since a candidate may already have been considered
and rejected with a reason.

**Step 2, ingest the recast for whatever remains.** `01_credit-use-case.qmd` covers censoring (10
mentions), the outcome window (19 and 28) and age-period-cohort (8 and 10) across 9,512 words,
while multiple decrement appears twice and may not clear the bar. Register it as a **new** source
record with its own URL at
`https://github.com/supermarmar/actuarial_deep_learning/blob/main/credit_lectures/01_credit-use-case.qmd`,
never by amending `dl-actuarial-2026-l01-use-case`, which describes a different document. The
repository is public, so `public-free` is accurate and check 11 will accept it. T5 by analogy
with the ETH lectures is an assumption rather than a schema rule, so state it in the record.

**Step 3, the two fixes that caused the misdiagnosis.** `sources/syllabi.yaml`'s `local` field
points at `actuarial_deep_learning/lectures/` while the trunk derives from `credit_lectures/`
beside it, and the two series share a numbering scheme, which is what sent three batches to the
wrong document. Correct the field and say in a comment that the two series exist at every lecture
number. Then retire the acquisition entry at `sources/wanted.yaml:1159`, which proposes acquiring
material that is not missing.

**Trap:** `.staging/phase-2/` still holds all 39 ledger fragments and `ledger-01.yaml` names that
entry, so `merge_ledger.py` resurrects it on the next run unless the fragment is edited in the
same commit.

**Out of scope, worth raising separately:** `actuarial_deep_learning` carries no LICENSE file
while its upstream summer-school material is CC BY-NC.

**Done when:** every one of the four either carries an article or has a recorded reason for
staying uncovered; `check.py` clean, check 11 included; the ledger merges idempotently.

---

## Branch 4: `refactor/ledger-claims`

Forty-five entries carry a `claim` naming one seeded section while `needed_by` has grown to span a
dozen, and the batch that added each node appended a paragraph to `note` saying so. The count
splits 29 university, 16 other in `wanted.yaml`, and 8 in `to-ingest.yaml`. The ten named at the
14 September gate do not survive measurement, and the worst entries are professional-body rather
than university: `assa-f107-study-material-2026` runs to 31 note paragraphs over 177 nodes, and
`ifoa-cs1-core-reading-2026` to 26.

Rewrite each `claim` so it describes what the document is actually needed for across every node in
its `needed_by`, and collapse the accumulated `note` into what a reader at the acquisition gate
needs, keeping any rejected-candidate reasoning that would otherwise be lost.

**Verification criterion, stated up front because no check validates claim text:** the diff shows
changes to `claim` and `note` only. Every `needed_by` list and every other field is byte-identical,
confirmed by loading both files before and after and comparing as data rather than by reading the
diff, and by a `merge_ledger.py` round trip that is byte for byte idempotent. Prose rewriting
across 45 entries is exactly where a `needed_by` id goes missing silently.

**Batch it** at roughly ten entries per agent on Sonnet, ordered largest first, so the entries the
acquisition gate reads first are the ones a fresh agent handles.
