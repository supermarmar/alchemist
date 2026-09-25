# Phase 3 pages brief

The brief every Phase 3 writing agent reads first, and the one the model measurement's two arms
read. It lives in `notes/` rather than in `.staging/phase-3/`, which is gitignored, because
Phase 2's wave 1 brief lived only in a session and had to be reconstructed from its artefacts.
The design it implements is `docs/superpowers/specs/2026-09-19-alchemist-phase-3-pages-design.md`.

## The job

You own one batch of node ids, named in `.staging/phase-3/manifest.yaml` under
`batches: <N>: nodes:`. The measurement arms are given their ten ids directly. For each node,
replace the stub body with a tier-1 page written to the template below and land it through the
write tool. Batches are disjoint, which is what licenses you to write node files directly.
Never touch a node outside your own list.

## Read once, before the first node

- `nodes/conditional-probability.md`, `nodes/survival-function.md` and `nodes/hazard-rate.md`:
  the three exemplars. Copy their shape. They are things to copy rather than things to
  interpret.
- `notation/objects.yaml`: the objects the corpus names and their spelling in each domain. A
  page spends an object in the spelling of the domain it declares, and the rendered page's
  alias table is generated from what you declare.
- This file.

## Per node, in manifest order

1. Read `nodes/<id>.md`. The stub body is the transcriber's one-paragraph statement of what the
   syllabus item covers. It fixes the scope of your page and is discarded when the page replaces
   it. The `anchor` field names the syllabus item, and that item's depth is the depth the page
   is examined at.
2. Read every article in `vault_articles` in full, at `<vault>/wiki/<slug>.md`, where the vault
   is at `$ALCHEMIST_VAULT` or `~/Documents/Repos/vault`. Write from them. Never quote them:
   paraphrase, since some are purchased material and this repo is public. Where the field is
   empty, write from the stub, the anchor, the node's neighbourhood and the standard treatment
   of the subject.
3. Read the pages of the node's `requires`, so your page assumes exactly what they give, and
   find the node's unlocks with `grep -l "^requires:.*\b<id>\b" nodes/*.md`, because `unlocks`
   is derived and never stored.
4. Write the body to a scratch file and land it:

   ```
   .venv/bin/python scripts/write_page.py --node <id> --body <scratch> --spends obj.hazard:credit obj.survival:credit
   ```

   The tool validates the body against the template, refuses a spend `objects.yaml` cannot
   render for that node, sets `status: drafted` and re-renders the record. Fix what it refuses
   and run it again. Never hand-edit frontmatter, and never set `reviewed`.
5. Record the node in your report, described below.

## The template

A body carries exactly three sections, in this order, under these headings, and nothing else.
Everything else on the rendered page (the title, the alias table, the unlocks and the sources)
is generated from the record.

1. `## Definition`. One or two sentences a reader could quote, naming the object, and giving a
   condition or degeneracy where one is worth stating. Not every object has one, and inventing
   a clause to fill the slot is the mistake the first draft of `survival-function` made. Leave
   it out sooner than invent it.
2. `## The expression`. The defining formula in one display block, between `$$` delimiters, in
   the spelling the node's spends declare, with every symbol in it named in the sentence
   beneath. One display block is the norm and two is the ceiling. A node that wants a third is a
   node that wants to be two nodes: write the page with two and record a split candidate in
   your report. Inline `$...$` in the prose is unrestricted, and is how the symbols get named.
3. `## Why this node exists`. Two or three sentences on what breaks without this node, ending
   on the node that needs it next where the graph has one, and otherwise on the consequence.
   The node you name must be one of the unlocks you found in step 3, named by its title in
   prose, since nothing validates a forward reference and an invented one promises a page that
   will never exist. Say "the prerequisite" or name the node, never "the previous node": a node
   sits in several paths and has no single previous node.

Four rules the tool enforces: exactly the three headings and no other heading of any level; one
or two display blocks; "rather than" at most once per page; and no currency written with a
dollar sign, since every `$` on the page is a maths delimiter. Write "2 million euro", never
"$2m".

## What a page spends

Declare a spend for every symbol on the page that `objects.yaml` holds for one of the node's
domains, in that domain's spelling. Declare nothing for a symbol the file does not hold. Where a
symbol on your page is one the node's domains would spell differently and the file lacks it,
which is the collision the notation contract exists for, write the page in the spelling of the
node's first-listed domain and record a collision candidate in your report: a proposed object
id, the spelling per domain, and what each domain calls the thing. Do not edit `objects.yaml`;
Mario grows it between waves from the candidates the reports name.

## Writing rules

British English. No em or en dashes as punctuation; use commas, full stops, colons or
parentheses. No negated counterpart clauses ("X, not Y", "not only X but also Y", "it's not
just X, it's Y"); front the contrast instead. "Rather than" at most once per page. Contractions
where they read naturally. Prose carries everything; a page has no bullet list. Define a term
on first use. Actions live in verbs: "the estimator divides", never "a division is performed".
Keep subject and verb close, and give a definition its own sentence. Concrete over abstract: the
field's own name for the thing, the actual condition. Connectives where the logic turns
(however, therefore, hence, consequently, since). Say it literally where a literal phrase
exists.

Mathematics: `$$ ... $$` for the display block and `$ ... $` inline; `\lt` and `\gt` for
comparisons, so a comparison can never be read as an HTML tag; `\mid` for conditioning; `\,`
before a differential. Every symbol in the display block is named in the sentence beneath it.
KaTeX renders the page, so no MathJax-only macro, no `\label`, and no `\begin{align}` outside a
display block.

## The report

Write `.staging/phase-3/report-<NN>.md` for a batch, or
`.staging/phase-3/measurement/report-arm-<x>.md` for a measurement arm. Open with three counts:
nodes written, nodes written from articles, nodes written without. Then one entry per node of
four lines at most: the sources read (slugs, or "stub and anchor only"); the spends declared;
collision candidates, if any; split candidates or anything else the template could not hold, if
any. Where the harness refuses the Write tool on a file named `report-NN.md`, write it with a
Bash heredoc; it is a required output of the batch.

## Finish

Run `.venv/bin/python scripts/check.py` and report its last line. Do not commit; the wave is
committed together once every batch is verified.
