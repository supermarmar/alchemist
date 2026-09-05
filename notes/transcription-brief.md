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

1. **Name the concept rather than the syllabus.** `chain-ladder` rather than `cs2-topic-4-2`. Two
   bodies teaching one concept must collide on the id, because the collision is what makes the
   node shared rather than duplicated.
2. **Singular, and no article.** `loss-distribution` rather than `the-loss-distributions`. A
   fixed named term keeps its conventional form even where that reads as plural, so
   `efficient-markets-hypothesis`, `option-greeks` and `term-structure-of-interest-rates` stand,
   because forcing the singular misnames the term practitioners use.
3. **Spell out an abbreviation unless it is on this list: `glm`, `gam`, `arima`, `garch`,
   `gev`, `gpd`, `mcmc`, `pca`, `svd`.** Those nine are what practitioners actually say, and
   nobody says "generalised linear model" twice in a sentence. Everything else is spelled out,
   so `probability-of-default` rather than `pd`. The list is closed. Report a case you believe
   belongs on it rather than adding it yourself, because a list twenty agents can each extend
   independently is the same failure as no list.
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

- **Hunt for restatements before you write.** A broad principles paper states one concept
  under several headings: a risk taxonomy and then a "main risks" list, PD, LGD and EAD defined
  once and again under model development, the Basel pillars introduced generically and re-named
  under a specific risk. Each restatement is a fold onto the node the first statement produced,
  and a transcriber who does not look for them first writes the same node three times.

Where your source numbers its items, an item is the finest numbered entry, and that holds where a
numbered item continues in unnumbered bullets: the bullets decide anchoring and splitting and add
nothing to the item count. Batch B split on exactly this, SP1 and SP9 counting bullets while SP5
and SP8 did not, and the ratios stopped comparing. Where a numbered source carries an unnumbered
glossary or defined-terms appendix (IFRS 9's Appendix A), leave it out of the count, fold its content
onto clause-anchored nodes, and state the exclusion in your report, because it can move the ratio
across the band on its own. Where the source does not number at all (a yearbook module description, a
regulation's running paragraphs), count with one rule so ratios compare across bodies: a full-stop-terminated sentence is one item, and a colon-introduced
list counts each listed member as an item. The two Pretoria agents each invented a rule and the two
disagreed, so their ratios were never comparable; state the rule you used in your report.

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
| IFoA SP1, SP2, SP5, SP6, SP7, SP8, SP9 | `ifoa.<subject>` | same three levels where present, decided per section rather than per subject, since one paper can carry both | `ifoa.sp7.3.5-1` for item 3.5.1 under 3.5 Reserving result analyses, or `ifoa.sp7.2.1` where section 2.1 has no third level |
| ASSA F107, F207 | `assa.<subject>` | outer section, then an objective list that **restarts at 1 inside each section**, then sub-items | section 1, objective 12, item 12.4 becomes `assa.f107.1.12-4` |
| BCBS d424 | `bcbs.d424` | numbered paragraphs, restarting from 1 inside each chapter, so the chapter is the section segment: `intro`, `sa`, `irb`, `cva`, `oprisk`, `floor`, `lr` | `bcbs.d424.irb.para-220` |
| IASB IFRS 9 | `iasb.ifrs9` | clauses: `5.5.1`; Appendix B paragraphs `B5.5.37` restart with a letter prefix and no chapter digit | `iasb.ifrs9.5.5-1`, and `iasb.ifrs9.b5.5-37` for the appendix, the prefix lowercased into the section segment |
| ETH summer school | `eth.dl-actuarial-2026` | twelve lectures | `eth.dl-actuarial-2026.l02`, where `l04` covers the combined lecture 04-05 and `l10` the combined 10-11 |
| UP undergraduate and honours | `up.<module-code>` | module code lowercased with no insertion, then section within the module description | `up.wst311.4`, `up.ias712.2`, `up.fni700.1` |

**Read the F107 row twice.** Its objective numbering restarts inside each outer section, so
"objective 12" is ambiguous without the section and `assa.f107.12.4` would name two different
things. The section segment is what disambiguates it.

**Where the source stops numbering and continues in bullets**, a bullet under a numbered item
takes its position in document order as the hyphenated final segment, so the second bullet under
SP8's item 3.5 is `ifoa.sp8.3.5-2`, and your report says you did this, because a reader verifying
that anchor has to count bullets rather than read a number. Bullets become separate nodes where
each names a separately teachable technique or object (SP8's burning cost, frequency-severity and
original loss curve approaches under 3.5), and fold into the parent item's single node where they
list considerations, factors or examples of one topic (SP8's 1.3, 2.2 and 3.4).

Where one numbered item carries both unnumbered bullets and numbered sub-items (SP6's 2.9 has a
bullet list and then 2.9.1 and 2.9.2), the bullets share the bare item anchor and only the numbered
sub-items take a hyphenated suffix, so a bullet position can never collide with a sub-item number.
Where PDF extraction has joined two bullets on one line ("Convertibles property derivatives"), read
them as two and say so in your report.

**`chosen` is the anchor for a prerequisite your paper assumes and never states.** A specialist
paper takes core technique for granted: SP7 discusses stochastic reserving throughout and never
names the deterministic chain ladder it builds on. Write the node, anchor it `chosen`, and say so
in your report, rather than stretching a real heading to cover something it does not say.

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

## Before you invent an id

Rule 1 says two bodies teaching one concept must collide on the id, and a merged id is never
renamed afterwards, so a collision missed here is a collision missed permanently. Make it a
procedure rather than a hope:

```bash
cd ~/Documents/Repos/alchemist
{ find .superpowers/phase-1 -path '*/nodes/*.md' 2>/dev/null; find nodes -maxdepth 1 -name '*.md'; } | sed 's#.*/##; s/\.md$//' | sort -u
```

That prints every id staged so far, by any body, together with every id already in the corpus at
`nodes/`, which holds drafted records from Phase 0 that the merge protects and that you must reuse
rather than reinvent. Before you write a node, look for one naming
your concept and reuse it exactly, character for character. Where a staged id means what you
mean but spells it differently, take the staged spelling over your own and say so in that
node's `duplicate_of`.

Agents run in parallel, so this list holds whatever landed before you started and it will be
incomplete. Run it again immediately before you write your files, because bodies land while you
read: SP2's first scan found nothing to reuse and its second, minutes later, found fourteen. It is still what separates a merge that unions two records from one that carries
`hazard-rate` and `hazard-function` as two nodes forever. For a concept you expect another body
to teach and cannot find staged, write your own id and name the expectation in `duplicate_of`,
which is what Task 9 and Task 11 read to catch the near misses this check could not.

Reusing a staged id also donates your node's `requires` and `domains` into the shared record when
Task 9 unions the fields. Where your reading of the concept differs materially from the body that
staged it, say so in `duplicate_of`: CS2's `age-period-cohort` is a mortality projection model and
the trunk's is a vintage-curve decomposition of loss rates, and the merged node needs a human to
look at that union rather than assume it resolves.

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
    needs: [claim-frequency-model]
```

`duplicate_of` names a concept you believe another body teaches under a different id. `needs`
lists prerequisites this node has that live in another body rather than yours, which your batch
check would reject in `requires` because it resolves ids within your own batch only. Keep the two
apart: Task 11 reads `needs` as edges to draw once every body is merged, and `duplicate_of` as
records to consider merging, and prose in one slot made it do both by hand. Omit `needs` where
there is nothing to list.

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

Then round-trip your own manifest, because neither command above reads it and hand-rolled YAML
goes invalid the moment a long `duplicate_of` string wraps mid-sentence:

```bash
.venv/bin/python -c "
import yaml, sys
m = yaml.safe_load(open('.superpowers/phase-1/<body-id>/manifest.yaml'))
assert len(m['nodes']) == m['nodes_emitted'], (len(m['nodes']), m['nodes_emitted'])
print(f\"manifest parses, {m['nodes_emitted']} entries\")"
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
