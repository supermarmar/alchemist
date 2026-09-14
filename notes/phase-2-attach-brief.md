# Phase 2 attach brief

Reconstructed on 14 September 2026 from the wave 1 artefacts (`report-01.md` to
`report-13.md`, `ledger-01.yaml` to `ledger-13.yaml`), because wave 1 ran from a brief that
lived only in a session's context. Wave 2 and wave 3 work from this file, so the three waves
stay comparable and the gate report reads batch-to-batch variation as subject matter rather
than as brief drift.

It lives in `notes/` rather than in `.staging/phase-2/`, which is gitignored, because losing
the brief is the failure this file exists to repair and an untracked copy loses it to any
`git clean` or fresh clone. Five of its rules were written during wave 2 from what thirteen
agents each discovered separately: the stray-writes scoping, the multi-anchor ledger rule, the
direct-read rule on a subagent's quotations, the same-wave collision sequence, and the heredoc
workaround for a refused report write.

## The job

Each agent owns one batch of forty node ids, named explicitly in
`.staging/phase-2/manifest.yaml` under `batches: <N>: nodes:`. For every node in the batch,
decide whether the vault holds a wiki article that genuinely covers the node's subject. Where
it does, attach it. Where it does not, record what document would close the gap.

Batches are disjoint, which is what licenses agents to write node files directly. Never touch
a node outside your own batch.

## The cover bar

Attach an article when it treats the node's subject, meaning a definition and a use, a named
section, or a derivation the node's body would be written from. A passing mention is not
coverage: one clause naming the term inside an argument about something else is rejected, and
the rejection is named in the report.

Partial coverage attaches. Where an article covers one half of a two-part node, attach it and
say in the report which half is uncovered, then ledger the remainder. A node whose vault
article covers less than it needs is better served by a real citation plus a stated gap than
by nothing.

Where two articles cover the same ground, attach the dedicated one and leave the broader
overview off, saying so. Where two articles cover different parts of the node, attach both.

Open every candidate before judging it, yourself. Where you delegate searching to a subagent,
its answer locates an article and nothing more: every quotation and every claim about what an
article says must trace to your own direct read of the file before it reaches a report or a
rejection. A wave 2 batch caught a subagent quoting a sentence its named article does not
contain, and a fabricated quotation beside a real slug is invisible at the gate.

The index (`data/vault-index.yaml`, 483 articles with
slug, title, type, topics and confidentiality) is a search surface, not evidence; the title
and topic list will mislead you about a third of the time. A full-text grep across
`~/Documents/Repos/vault/wiki` catches articles the topics miss, and a node reported as having
no vault content at all should have been checked both ways.

## Writing the attachment

Set the field through the tool, never by hand:

```
.venv/bin/python scripts/attach_articles.py --node <id> --articles <slug> [<slug> ...]
```

The tool re-renders the whole record, so every write is identical in shape, and it refuses a
slug that would fail check 11 (unresolvable, unclassified, or not public-free/public-paid). An
uncovered node keeps its empty `vault_articles`; do not run the tool with an empty
`--articles` on a node you did not change.

## The ledger fragment

Write `.staging/phase-2/ledger-<NN>.yaml`, a YAML list of entries, each carrying `id`,
`needed_by`, `claim`, `document`, `expected_tier`, `acquisition` and `status`, with `url`,
`note` and `primary_alternative` optional. `acquisition` is one of `public-download`,
`regulator`, `journal`, `purchased-personal`; `status` is one of `wanted`, `located`,
`in-raw`, `ingested`. The contract is in `scripts/alchemist/ledger.py`.

Propose the document by the node's own anchor body, which is the default rule: a node anchored
`ifoa.cs2.*` wants the IFoA CS2 Core Reading, one anchored `assa.f107.*` wants the ASSA F107
study material. Depart from it where direct inspection shows the anchor body does not in fact
carry the material, and say why in the entry's `note`.

Where a node carries several anchor bodies, ledger it against the first-listed one and name the
others in that entry's note, rather than opening an entry per body. One node wanting five
documents inflates the ledger against which acquisition is decided, and the first anchor is the
body the node was transcribed from. Batches 15, 24 and 26 each reached this rule independently
in wave 2, and `arbitrage-and-market-completeness` in `ledger-04.yaml` is wave 1's precedent.

**Reusing an existing id.** `.staging/phase-2/proposed-ids.yaml` lists every id proposed so far,
seeded and earlier waves alike. Where your node wants one of them, copy `document`, `expected_tier`,
`acquisition`, `status` and `claim` verbatim from that file and write `needed_by` with your own
batch's node ids only, so `union_entries` records no disagreement. Where your batch needs a
different part of that document than the claim describes, say which part in a `note`. Notes on a
shared id accumulate rather than overwrite, so yours survives the merge alongside every other
batch's.

Check the fragment before reporting:

```
.venv/bin/python scripts/merge_ledger.py --dry-run
```

Run it **last**, after your fragment is complete. `proposed-ids.yaml` holds the ids settled in
earlier waves, so it cannot show you an id a sibling in your own wave has just claimed for a
different section of the same document. That collision appears only as a field disagreement in
the dry run against the live staging directory. Where you see one on an id you proposed, copy
the sibling's `document`, `expected_tier`, `acquisition`, `status` and `claim` verbatim, keep
your own `needed_by` and your own note, and re-run. Wave 2's batches 15 and 17 collided this
way on `up-wtw381-course-notes`, group theory against field extensions.

## The report

Write `.staging/phase-2/report-<NN>.md`. Where the harness refuses the `Write` tool on it,
reading a pipeline artefact named `report-NN.md` as a caller-facing summary, write it with a
Bash heredoc instead; the file is a required output of this batch and the wave cannot be
verified without it. Open with the counts: nodes worked, nodes attached,
nodes uncovered, total (article, node) attachments. Then two sections.

**Attached.** One entry per node. Name every candidate considered with a one-word verdict,
then the attachment and the sentence or section that earns it, quoted where a quotation settles
it. Name each rejected candidate and why it lost. State any partial-scope limit.

**Uncovered.** Grouped by reason, not listed flat. The groups wave 1 used, and they held:
no vault content at all (confirmed by index and full-text grep); passing mentions only, with
the strongest rejected candidate named; and considered but deliberately not attached despite
surface similarity, with the reasoning. Close with a paragraph on the ledger fragment: how many
entries, which reuse existing ids, which depart from the anchor-body default and why.

## Verification before you report done

1. `.venv/bin/python scripts/check.py` passes, all eleven rules.
2. `.venv/bin/python scripts/merge_ledger.py --dry-run` reports no complaint.
3. Every node file you wrote belongs to your batch. Thirteen agents share one working tree
   during a wave and nobody commits mid-wave, so `git diff --name-only` shows every sibling's
   writes as well as yours and a tree-wide `stray_writes` call will report roughly 500 strays
   that are not yours. Pass it the files **you** touched, which is the list of ids you ran
   `attach_articles.py` against. The tree-wide check is the orchestrator's after the wave, where
   the union of every batch's ids is the right thing to test against:

```
.venv/bin/python - <<'EOF'
import sys, yaml
sys.path.insert(0, '.')
from scripts.alchemist.batches import stray_writes
BATCH = <NN>
manifest = yaml.safe_load(open('.staging/phase-2/manifest.yaml'))
MINE = ['<every node id you ran attach_articles.py against>']
print(stray_writes(manifest, BATCH, MINE) or 'no strays')
EOF
```

## House rules that bind the prose you write

British English throughout. No em dashes or en dashes as punctuation. Currency takes the unit
word, never a bare dollar sign, because every `$` on a page is a maths delimiter. Node titles
are sentence case, and you are not retitling anything in this phase anyway.

Do not commit. Do not merge the ledger into `sources/wanted.yaml`; that happens once, after
wave 3, at the Phase 2 gate.
