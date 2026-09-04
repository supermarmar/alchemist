# Transcription brief, Phase 1

Read this in full before transcribing. It is binding, and where it disagrees with your own
judgement, follow it and record the disagreement in your report rather than departing quietly.
Inconsistent conventions are invisible in a node list read once and expensive in Phase 3.

## What you produce

Stub node records, one markdown file per node, written into **your own staging directory**:

```
.superpowers/phase-1/<body-id>/nodes/<node-id>.md
.superpowers/phase-1/<body-id>/manifest.yaml
```

You do **not** write into `nodes/`. Twenty agents share that namespace and several of
you will produce `survival-function`; writing direct means the second clobbers the first and
drops its anchor silently. Task 9 merges your staging into the corpus and unions the fields a
shared node accumulates.

## The node record

```yaml
---
id: hazard-rate
title: Hazard rate
domains: [stats, life, gi, credit]
status: stub
requires: [survival-function]
spends: []
anchor: [ifoa.cs2.2.1-3]
vault_articles: []
vault_sources: []
taught_in: null
---

One or two sentences saying what this node covers, in your own words, so a
reader of the review document can tell it apart from its neighbours.
```

Five fields are fixed for every stub you write. `status` is always `stub`. `spends` is always
empty, because a stub declares no symbols and Phase 3 fills it when it writes the page.
`vault_articles` and `vault_sources` are always empty, because attaching sources is Phase 2.
`taught_in` is always `null`, because check 8 fails on a lecture that does not exist yet.

The body is **one or two sentences and no mathematics**. Keep it under a paragraph, leave the
citable definition to Phase 3, and use no `$...$` at all: Phase 3 writes the page against a locked template, and prose
written now is prose Phase 3 has to read and discard. `scripts/katex_sweep.py` now sweeps `.md`
bodies alongside `.qmd`, so running it over your batch and seeing any span reported at all means
a body broke this rule, whether or not KaTeX itself can parse the maths. The body exists so that
gate 2 can tell `hazard-rate` from `force-of-mortality` in a list, and that is its whole job.

## Node ids

Lowercase, hyphen-separated, matching `^[a-z0-9]+(-[a-z0-9]+)*$`, and **never renamed** once
merged. Four rules that stop twenty agents diverging:

1. **Name the concept, never the syllabus.** `chain-ladder` rather than `cs2-topic-4-2`. Two
   bodies teaching one concept must collide on the id, because the collision is what makes the
   node shared rather than duplicated.
2. **Singular, and no article.** `loss-distribution` rather than `the-loss-distributions`.
3. **Spell out an abbreviation unless the abbreviation is the name practitioners use.**
   `probability-of-default` rather than `pd`, but `glm` and `arima` stay, because nobody says
   "generalised linear model" twice in a sentence.
4. **British English in the id as everywhere else.** `generalised-linear-model`,
   `discretisation`, `modelling`.

Where you suspect another body covers the same concept under a different name, still emit your
node and record the suspicion in your manifest's `duplicate_of` field. Guessing at another
agent's slug is worse than declaring the overlap.

## Granularity

A node is **one thing a reader can be examined on separately and that carries its own
prerequisites**, targeting one node per twenty to forty minutes of teaching.

Gate 1 tied this to the **syllabus item**, meaning CS2 1.1.5 rather than CS2 1.1. That is a
default rather than an identity, and two departures from it are expected:

- **Fold** an item that restates its neighbour. CS2 1.2.5 reads "loss distributions for both
  the insurer and the reinsurer after the operation of simple forms of proportional and excess
  of loss reinsurance where underlying losses take the forms given in 1.2.4". It applies 1.2.4
  and is not separately examinable, so it folds into the node 1.2.4 produced and adds its
  anchor to that node's list.
- **Split** an item naming several things examined separately. CS2 1.4.1 reads "recognise
  extreme value distributions, suitable for modelling the distribution of severity of loss and
  their relationships". The generalised extreme value and the generalised Pareto are separate
  nodes with separate prerequisites, and both take the anchor `ifoa.cs2.1.4-1`.

Your ratio of nodes to items should land between 0.5 and 1.5. Task 10 measures it across every
body and a ratio outside that band is reported to Mario, so explain yours in your report rather
than being surprised by it.

## The anchor mapping table

`anchor` is a **list**, because a node put in the corpus by three bodies carries three anchors.
Every anchor is lowercase, dot-separated, and three or four segments, or the literal `chosen`.
The grammar allows four segments at most, so a body numbering three levels deep hyphenates its
third level into the item segment.

| Body | Prefix | Source numbering | Anchor spelling |
|---|---|---|---|
| IFoA CS1, CS2, CM1, CM2, CB2, CP1 | `ifoa.<subject>` | topic, section, item: `1`, `1.1`, `1.1.5` | `ifoa.cs2.1.1-5` |
| IFoA SP1, SP2, SP5, SP6, SP7, SP8, SP9 | `ifoa.<subject>` | same three levels where present; some subjects stop at two | `ifoa.sp7.2.3-1`, or `ifoa.sp7.2.3` where the syllabus has no third level |
| ASSA F107, F207 | `assa.<subject>` | outer section, then an objective list that **restarts at 1 inside each section**, then sub-items | section 1, objective 12, item 12.4 becomes `assa.f107.1.12-4` |
| BCBS d424 | `bcbs.d424` | numbered paragraphs | `bcbs.d424.para-31` |
| IASB IFRS 9 | `iasb.ifrs9` | clauses: `5.5.1` | `iasb.ifrs9.5.5-1` |
| ETH summer school | `eth.dl-actuarial-2026` | twelve lectures | `eth.dl-actuarial-2026.l02`, where `l04` covers the combined lecture 04-05 and `l10` the combined 10-11 |
| UP undergraduate | `up.<module-code>` | module, then section within the module description | `up.wst311.4` |
| UP honours | `up.iashons<number>` | same | `up.iashons712.2` |

**Read the F107 row twice.** Its objective numbering restarts inside each outer section, so
"objective 12" is ambiguous without the section and `assa.f107.12.4` would name two different
things. The section segment is what disambiguates it.

An anchor must point at something that exists. Before you finish, pick three of your anchors,
find the heading each one names in your source text, and quote it in your report. That
demonstrates the mapping rather than asserting it, and it is the only check anyone will make
on this.

## Domains

The closed vocabulary is twelve: `maths`, `stats`, `ml`, `data-eng`, `fin-eng`, `actuarial`,
`life`, `gi`, `credit`, `regulation`, `eco`, `fin-man`. Nothing outside it parses.

Assign the domains a node **belongs to** rather than the domains that might one day cite it. A node
in four domains is making a claim that four fields teach this object, and that claim generates
the bridge table. Two guides:

- `maths` and `stats` are for the roots, meaning material with no insurance or banking content
  at all. A survival function is `stats`; an exposed-to-risk calculation is `life`.
- `regulation` is for material whose content is what a rule requires rather than for material a rule
  happens to use. The IRB risk-weight formula is `credit` and `regulation`; the Vasicek
  single-factor model underneath it is `credit` and `stats`.

## Prerequisites

`requires` names nodes, and you can only name nodes you know about, which is your own body's.
**Emit within-body prerequisites only.** Task 11 resolves the cross-body edges once every
staging directory exists, and a guess at a node another agent may or may not have produced is
a broken reference that check 3 will reject.

Two rules. `requires` is what a reader must already hold to follow this node rather than everything
related to it, so a list beyond five entries is usually a grain problem rather than a rich
node. And the graph must stay acyclic, so where two nodes seem mutually prerequisite, one of
them is really two nodes and you should split it.

## Your manifest

```yaml
body: ifoa-cs2-2026
source: data/syllabi/ifoa-cs2-2026.txt
items_in_document: 87
nodes_emitted: 94
nodes:
  - id: hazard-rate
    title: Hazard rate
    anchor: [ifoa.cs2.2.1-3]
    domains: [stats, life, gi, credit]
    requires: [survival-function]
    duplicate_of: null
  - id: loss-distribution
    title: Loss distribution
    anchor: [ifoa.cs2.1.1-1]
    domains: [gi, stats]
    requires: []
    duplicate_of: "likely the same concept SP8 will call severity-distribution"
```

## Before you report

Run `.venv/bin/python scripts/check.py` and expect it to pass. It confirms the corpus you have
not touched is still whole, which is what "write nothing into `nodes/`" is standing on. It reads
`nodes/` and `paths/` at the repository root, so it cannot see your staging directory, and
checking your own batch takes a second command:

```bash
cd ~/Documents/Repos/alchemist
.venv/bin/python - <<'EOF'
from pathlib import Path
from scripts.alchemist.model import parse_node, Corpus
from scripts.alchemist.checks import check_requires_resolve_and_acyclic

records = sorted(Path(".superpowers/phase-1/<body-id>/nodes").glob("*.md"))
nodes, failures = {}, []
for record in records:
    try:
        node = parse_node(record)
        nodes[node.id] = node
    except Exception as exc:
        failures.append(f"{record}: {type(exc).__name__}: {exc}")

result = check_requires_resolve_and_acyclic(Corpus(nodes=nodes, paths={}))
failures.extend(result.failures)

print(f"{len(records)} staged records, {len(failures)} problems")
for failure in failures:
    print(f"  {failure}")
EOF
```

Replace `<body-id>` with your own and expect `0 problems`. This is `parse_node` plus the
acyclicity half of check 3, run against only the nodes you wrote: it rejects a malformed
anchor, an unknown domain, an id that fails the slug pattern, a filename that disagrees with
its id, and a `requires` edge that does not resolve within your own batch or that closes a
cycle. Then report what neither command verified about your batch. Neither checks that an
anchor points at a section that exists, that your grain matches the corpus, or that `requires`
is pedagogically ordered rather than merely acyclic, and neither can check symbol resolution,
path teachability or a cross-body edge, because those need every body's nodes sharing one
namespace, which is what Task 9 and Task 11 build once every staging directory exists. Report:

1. Three anchors, each with the heading it names quoted from your source.
2. Your node count against your document's item count, with any ratio outside 0.5 to 1.5
   explained.
3. Every `requires` edge you were unsure about.
4. Every cross-body overlap you suspect, which is what your `duplicate_of` fields carry.

**Measure rather than read, and report rather than silently patch.**
