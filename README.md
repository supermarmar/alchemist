# Alchemist

A comprehensive quantitative syllabus, held as a dependency graph and rendered as a teaching
corpus. Credit risk is the trunk, life and general insurance run alongside it throughout, and
the roots reach down into mathematics, statistics, financial engineering, data engineering,
feature engineering, machine learning, economics, financial management and actuarial science.
The corpus has one job: teach this material to somebody else, now and in twenty years,
without the teacher present.

The graph currently holds 1,580 nodes across 10 paths, anchored against 20 published syllabi
and standards. Every node carries a reference page, and one trunk node carries a full lecture
so far.

Published at <https://supermarmar.github.io/alchemist/>. The full design is in
`docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`, and the conventions this
repo runs on are in `CLAUDE.md`.

## The two tiers

Every node in the graph is a markdown file at `nodes/<id>.md`, whose YAML frontmatter carries
its place in the graph (what it requires, which domains it belongs to, which symbols it
spends) and whose body is a reference page: definition, worked expression and why the node
exists. That reference page is tier 1, and every node has one.

Trunk nodes and the points where two branches meet additionally get a full lecture: a Quarto
document that teaches the node's material end to end, with its own PDF for offline reading.
That is tier 2, and a node carries it exactly when its `taught_in` field is set.

## Clone and run the checks

```bash
git clone https://github.com/supermarmar/alchemist.git
cd alchemist
uv venv --python 3.14.7 .venv
uv pip install --python .venv -r requirements-dev.txt
git config core.hooksPath .githooks   # not committed; run this once per clone
.venv/bin/python scripts/check.py
```

`check.py` enforces eleven rules over the corpus: that every declared symbol resolves and
stays unique within its domain, that the prerequisite graph is acyclic, that every teaching
path is actually teachable in the order it lists, that every quoted source is publishable,
that no reviewed node carries an open citation gap, that the committed symbol table matches
what the notation file would generate, that every node claiming a lecture names one that
exists, that every node id in the gap ledger resolves, that every title is sentence case, and
that every attached vault article resolves to a real wiki file and is public-free or
public-paid. It runs automatically on every commit once `core.hooksPath` is set, above.

Two of the eleven, publishable citations and attached vault articles, read a separate
**private** vault repository at the path in `ALCHEMIST_VAULT`, or `~/Documents/Repos/vault`
by default. **Cloning this public repo on its own gets you nine of the eleven checks; the
vault is not included and not needed to work on anything else.** Where it is absent,
`check.py` reports those two as skipped rather than failing, so the other nine still gate
every commit. Gap closure needs no vault, since `sources/wanted.yaml` lives here.

Run the full test suite with:

```bash
.venv/bin/python -m pytest
```

## Building the site

```bash
.venv/bin/python scripts/build_site.py
```

Generates `index.html`, one page per node, one page per teaching path, and one dependency
graph SVG per domain (via graphviz's `dot`, so install it first: `brew install graphviz`).
`notation/symbols.md` is also generated from `notation/objects.yaml` and is committed so it
reads on GitHub; `build_site.py` regenerates it every time, and `check.py`'s seventh rule
fails a commit where the committed copy has drifted from what `objects.yaml` would produce.

## Rendering a lecture

```bash
bash scripts/render_lecture.sh lectures/<id>.qmd
bash scripts/html_to_pdf.sh lectures/<id>.html
```

Quarto renders the `.qmd` against the vendored KaTeX in `vendor/katex/`, so a lecture
typesets its mathematics with no network connection and no content delivery network to go
stale on. Headless Chrome then prints the result to a PDF beside it. A lecture is not
finished until that PDF exists: rendering and printing are two separate commands because
printing depends on the freshly rendered HTML, and an edit to the `.qmd` means running both
again in that order.

## Licence and attribution

The trunk material in this corpus derives from the actuarial summer school **Deep Learning
for Actuarial Modeling**, run at Università Cattolica del Sacro Cuore, Milan, by Salvatore
Scognamiglio, Marco Maggi, Mario V. Wüthrich and Ronald Richman, licensed
**CC BY-NC 4.0**. This corpus reuses, remixes and adapts that material for non-commercial
teaching purposes, with attribution to the original authors and course, and each derived
lecture states in a header comment what it changed from the source and why. The corpus as a
whole therefore stays non-commercial; a lecture that spends this material and later needs a
commercial licence must first be re-sourced to the peer-reviewed papers behind the course
slides.

Ninety further node records anchor to that same lecture set, `ucsc.dl-actuarial-2026.l01`
through `.l12`. Each is a one- or two-sentence stub naming the concept its lecture teaches,
paraphrasing the source and quoting nothing from it, and this paragraph stands as their
statement of changes.

Everything else in this repo, the schema, the checker, the site generator and the render
chain, is original work, and nothing here carries Gini client data, parameters or figures:
this is a personal teaching project rather than a Gini deliverable. See `CLAUDE.md` for the
full public-repo rules and which Gini engineering conventions are relaxed here, and why.
