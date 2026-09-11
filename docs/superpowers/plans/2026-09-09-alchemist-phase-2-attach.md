# Alchemist Phase 2 Attach implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Attach all 1,560 corpus nodes to the vault wiki articles that cover them, and record the
documents that would close every remaining gap, so Phase 3 can draft a page from what a node cites.

**Architecture:** Five tools land first, each test-driven. A build step reads the 477 vault wiki
articles into a gitignored index of slug, title, type, topics and confidentiality. A manifest
slices the sorted node ids into 39 batches of 40. Thirty-nine agents then run in three sequential
waves of thirteen, each reading the index once, opening each candidate article to test it against
the cover bar, and calling a small attach tool rather than hand-editing YAML. Node files are
disjoint across batches so agents write them directly, whereas the shared gap ledger stages as
one fragment per agent and merges once. A new check 11 fails the build on any attached slug that
does not resolve to a real wiki file or whose article is unclassified.

**Tech Stack:** Python 3.14, pytest, PyYAML. Python is always `.venv/bin/python`, never a system
`python3`.

**Spec:** `docs/superpowers/specs/2026-09-09-alchemist-phase-2-attach-design.md`. Read it before
task 1. Sections 3 and 5 carry the decisions and the agent contract that every task below
implements, and section 7 states what check 11 does and does not gate.

## Global constraints

- **Branch:** `feat/phase-2-attach`, cut from `main` **after both PR #4 and the tool-chores pull
  request have merged**. `docs/superpowers/plans/2026-09-09-alchemist-tool-chores.md` runs first.
- **Python is `.venv/bin/python`.** Never a system `python3`.
- **The vault is a separate private repo** at `ALCHEMIST_VAULT` or `~/Documents/Repos/vault`.
  Read it through `vault_root()` in `scripts/alchemist/checks.py` and never add a second way to
  find it. Nothing is ever written into the vault by this phase.
- **The cover bar, verbatim from spec D2.2:** an article attaches to a node only where it treats
  that node's subject directly enough that a Phase 3 writer could draft the page from it, meaning
  the article is about that thing or gives it a substantive section. A passing mention does not
  attach.
- **`vault_sources` stays empty this phase.** That field means the node quotes primary text, and
  no node carries prose until Phase 3.
- **A ledger fragment names the node's own anchor document by default.** An agent proposes a
  different document only where the anchor genuinely cannot cover the node, and says why in its
  report fragment. This rule is what bounds the ledger at roughly 59 entries.
- **This repo is public.** Assume anything committed is published. No client material, and the
  generated index is never committed.
- **The pre-commit hook runs `check.py` on every commit** and validates the working tree.
- **Never self-merge, never force-push `main` or `develop`, never `--no-verify`.**
- **Conventional Commits**, imperative and lowercase, no trailing period, ending with
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Explicit paths on `git add`.
- **British English throughout, and no em or en dashes as punctuation.**
- **Write currency with the unit word, never a bare dollar sign.** Every `$` on a page is a maths
  delimiter.
- The suite stands at **227 passed** once the tool chores merge. Every tool task adds tests, so
  the count rises and never falls.

## File structure

| File | Responsibility |
|---|---|
| `.gitignore` | Modify. Adds `.staging/`, so 39 agents' fragments never reach a commit. |
| `scripts/alchemist/vault.py` | Create. Reads the wiki into index records, and resolves a slug back to a file. The only module that knows the wiki's frontmatter shape. |
| `scripts/build_vault_index.py` | Create. CLI over `vault.py`, writing `data/vault-index.yaml`. |
| `scripts/alchemist/checks.py` | Modify. Adds check 11 and registers it in `run_all`. |
| `scripts/attach_articles.py` | Create. CLI an agent calls to set one node's `vault_articles`, so no agent hand-edits YAML. |
| `scripts/alchemist/batches.py` | Create. Slices the sorted node ids into the manifest, and verifies a diff against it. |
| `scripts/build_manifest.py` | Create. CLI over `batches.py`. |
| `scripts/alchemist/ledger.py` | Create. Unions the fragments into ledger entries. |
| `scripts/merge_ledger.py` | Create. CLI over `ledger.py`, the only writer of `sources/wanted.yaml` this phase. |
| `scripts/alchemist/coverage.py` | Create. Computes the coverage figures and renders the gate note. |
| `scripts/build_coverage_report.py` | Create. CLI over `coverage.py`. |
| `tests/test_vault_index.py` | Create. |
| `tests/test_check_attached_articles.py` | Create. |
| `tests/test_attach_articles.py` | Create. |
| `tests/test_batches.py` | Create. |
| `tests/test_ledger.py` | Create. |
| `tests/test_coverage.py` | Create. |

The logic sits in `scripts/alchemist/` and each CLI stays a thin argument parser over it, which is
the pattern `check.py` over `checks.py` and `merge_nodes.py` over `merges.py` already set. The
tests mirror the module rather than the CLI, per the relaxation `CLAUDE.md` records.

---

### Task 1: Ignore the staging directory

Thirteen agents write fragments under `.staging/phase-2/` and the pre-commit hook runs on every
commit, so a wave starting before this entry exists would dirty the tree. This is the first task
for that reason alone.

**Files:**
- Modify: `.gitignore`

**Interfaces:**
- Consumes: nothing.
- Produces: `.staging/` is ignored, which every later task relies on.

- [ ] **Step 1: Add the entry**

In `.gitignore`, after the `.superpowers/` line, add:

```
# Phase 2 writes one ledger and one report fragment per agent here, and the
# merge step consumes them. Nothing under it belongs in a commit: the fragments
# are an intermediate, and the manifest is rebuilt from the corpus.
.staging/
```

- [ ] **Step 2: Verify the ignore works**

```bash
mkdir -p .staging/phase-2 && touch .staging/phase-2/probe.yaml
git status --short
```

Expected: no mention of `.staging`. Then `rm -rf .staging`.

- [ ] **Step 3: Commit**

```bash
git add .gitignore
git commit -m "chore: ignore the Phase 2 staging directory

Thirteen agents per wave write fragments under .staging/phase-2 and the
pre-commit hook runs on every commit, so the entry lands before any wave.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 2: Build the vault index

**Files:**
- Create: `scripts/alchemist/vault.py`
- Create: `scripts/build_vault_index.py`
- Create: `tests/test_vault_index.py`

**Interfaces:**
- Consumes: `vault_root()` from `scripts.alchemist.checks`; `FRONTMATTER` from
  `scripts.alchemist.model`.
- Produces, and later tasks depend on these exact names:
  - `@dataclass(frozen=True) class Article: slug: str; title: str; type: str; topics: tuple[str, ...]; confidentiality: str`
  - `read_wiki(vault: Path) -> tuple[list[Article], list[str]]` returning the usable articles
    sorted by slug, and a list of human-readable skip reasons.
  - `article_path(vault: Path, slug: str) -> Path`, used by check 11 in task 3.
  - `PUBLISHABLE_ARTICLE = frozenset({"public-free", "public-paid"})`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_vault_index.py`:

```python
from pathlib import Path

import pytest
import yaml

from scripts.alchemist.vault import Article, article_path, read_wiki

ARTICLE = """---
title: {title}
slug: {slug}
type: method
topics: [{topics}]
sources: []
confidentiality: {confidentiality}
client_scope: []
last_updated: 2026-05-13
reviewed: false
---

A body.
"""


def write_article(vault, slug, *, title=None, topics="alpha, beta",
                  confidentiality="public-free"):
    path = vault / "wiki" / Path(slug + ".md")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ARTICLE.format(
        title=title or slug, slug=slug, topics=topics,
        confidentiality=confidentiality,
    ))
    return path


@pytest.fixture
def vault(tmp_path):
    (tmp_path / "wiki").mkdir()
    write_article(tmp_path, "methods/glm", title="Generalised linear models")
    write_article(tmp_path, "regulation/crr", title="Capital Requirements Regulation",
                  confidentiality="public-paid")
    return tmp_path


def test_an_article_reads_into_a_record(vault):
    articles, skipped = read_wiki(vault)
    assert skipped == []
    assert articles == [
        Article("methods/glm", "Generalised linear models", "method",
                ("alpha", "beta"), "public-free"),
        Article("regulation/crr", "Capital Requirements Regulation", "method",
                ("alpha", "beta"), "public-paid"),
    ]


def test_articles_come_back_sorted_by_slug(vault):
    write_article(vault, "concepts/aaa")
    articles, _ = read_wiki(vault)
    assert [a.slug for a in articles] == ["concepts/aaa", "methods/glm", "regulation/crr"]


def test_an_unclassified_article_is_skipped_and_named(vault):
    """The 34 real ones are the AI and engineering material. Excluding them is
    what stops an agent attaching a slug whose publishability is unknown."""
    path = vault / "wiki" / "methods" / "unclassified.md"
    path.write_text(ARTICLE.format(
        title="Unclassified", slug="methods/unclassified", topics="x",
        confidentiality="public-free",
    ).replace("confidentiality: public-free\n", ""))
    articles, skipped = read_wiki(vault)
    assert "methods/unclassified" not in [a.slug for a in articles]
    assert any("methods/unclassified" in s and "confidentiality" in s for s in skipped)


def test_unparseable_frontmatter_is_skipped_and_named(vault):
    (vault / "wiki" / "methods" / "broken.md").write_text("---\n: : :\n---\n\nBody.\n")
    articles, skipped = read_wiki(vault)
    assert "methods/broken" not in [a.slug for a in articles]
    assert any("methods/broken" in s for s in skipped)


def test_the_readme_and_meta_are_not_articles(vault):
    (vault / "wiki" / "README.md").write_text("# The wiki\n")
    (vault / "wiki" / "_meta" / "sources").mkdir(parents=True)
    (vault / "wiki" / "_meta" / "health.md").write_text("# Health\n")
    articles, skipped = read_wiki(vault)
    assert [a.slug for a in articles] == ["methods/glm", "regulation/crr"]
    assert skipped == []


def test_article_path_round_trips_a_slug(vault):
    assert article_path(vault, "methods/glm") == vault / "wiki" / "methods" / "glm.md"
    assert article_path(vault, "methods/glm").is_file()
```

- [ ] **Step 2: Run them to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_vault_index.py -v`
Expected: FAIL, all six collecting with `ModuleNotFoundError: No module named 'scripts.alchemist.vault'`.

- [ ] **Step 3: Write the module**

Create `scripts/alchemist/vault.py`:

```python
"""Reading the vault wiki into an index the attach agents can hold in context.

The wiki is a separate private repo of 477 articles, and an agent that grepped
it per node would spend forty searches per batch. One index of slug, title, type
and topics is small enough to read once and match forty nodes against, and
`topics` is the signal that makes it work: every article carries it, and it says
what the article covers in the vault's own vocabulary.

An article with no `confidentiality` field is excluded rather than defaulted.
This repo is public, so an attached slug whose publishability is unknown is
exactly the case check 11 exists to refuse, and excluding it here means no agent
ever sees it to attach.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from .model import FRONTMATTER

PUBLISHABLE_ARTICLE = frozenset({"public-free", "public-paid"})


@dataclass(frozen=True)
class Article:
    slug: str
    title: str
    type: str
    topics: tuple[str, ...]
    confidentiality: str


def article_path(vault: Path, slug: str) -> Path:
    """The file a `vault_articles` slug names. Check 11 resolves through here."""
    return vault / "wiki" / f"{slug}.md"


def read_wiki(vault: Path) -> tuple[list[Article], list[str]]:
    """Every usable article sorted by slug, plus a reason per article skipped.

    Skips are returned rather than logged, because the index writes them into
    its own foot and a silent exclusion is how 34 articles disappear unnoticed.
    """
    wiki = vault / "wiki"
    articles: list[Article] = []
    skipped: list[str] = []
    for path in sorted(wiki.rglob("*.md")):
        slug = path.relative_to(wiki).with_suffix("").as_posix()
        if slug == "README" or slug.startswith("_meta/"):
            continue
        match = FRONTMATTER.match(path.read_text())
        if match is None:
            skipped.append(f"{slug}: no frontmatter")
            continue
        try:
            meta = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            skipped.append(f"{slug}: frontmatter does not parse ({exc.__class__.__name__})")
            continue
        if not isinstance(meta, dict):
            skipped.append(f"{slug}: frontmatter is not a mapping")
            continue
        confidentiality = meta.get("confidentiality")
        if confidentiality is None:
            skipped.append(f"{slug}: carries no confidentiality field")
            continue
        articles.append(Article(
            slug=slug,
            title=str(meta.get("title") or slug),
            type=str(meta.get("type") or "unknown"),
            topics=tuple(str(t) for t in (meta.get("topics") or [])),
            confidentiality=str(confidentiality),
        ))
    return articles, skipped
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_vault_index.py -v`
Expected: 6 passed.

- [ ] **Step 5: Write the CLI**

Create `scripts/build_vault_index.py`:

```python
"""Write the vault wiki index the Phase 2 attach agents read once each.

    .venv/bin/python scripts/build_vault_index.py

The output is `data/vault-index.yaml`, which is gitignored along with the rest
of `data/`. It is never committed: the slugs reach this public repo anyway
through node frontmatter, whereas 477 vault article titles and topic lists
describe the shape of a private research base and buy nothing here. Rebuild it
rather than storing it; it takes seconds.
"""

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from scripts.alchemist.checks import vault_root
from scripts.alchemist.vault import read_wiki

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--vault", type=Path, default=None)
    parser.add_argument("--out", type=Path, default=REPO / "data" / "vault-index.yaml")
    args = parser.parse_args()

    vault = args.vault or vault_root()
    if not (vault / "wiki").is_dir():
        print(f"no vault wiki at {vault}", file=sys.stderr)
        return 2

    articles, skipped = read_wiki(vault)
    payload = {
        "built": date.today().isoformat(),
        "vault": str(vault),
        "articles": [
            {"slug": a.slug, "title": a.title, "type": a.type,
             "topics": list(a.topics), "confidentiality": a.confidentiality}
            for a in articles
        ],
        "skipped": skipped,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True))
    print(f"{len(articles)} articles indexed, {len(skipped)} skipped -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 6: Run it against the real vault**

Run: `.venv/bin/python scripts/build_vault_index.py`

Expected, as a relation rather than a magic number: the indexed count plus the skipped count
equals the number of articles in `<vault>/wiki/`, and the skipped count is 34. At the time of
writing that reads `449 articles indexed, 34 skipped`, against 483 articles. Check the relation
rather than the literal, because a hardcoded total goes stale the first time the vault gains an
article. Should the skipped count move, stop and report it: the design's coverage arithmetic rests
on the classification, and a change there means the vault moved under the design.

- [ ] **Step 7: Confirm the index is not tracked**

Run: `git status --short data/`
Expected: no output. `/data/` is already ignored whole.

- [ ] **Step 8: Run the suite and the checks**

Run: `.venv/bin/python -m pytest -q && .venv/bin/python scripts/check.py`
Expected: 233 passed, then ten rules ok at `1560 nodes, 13 paths, 0 failures`.

- [ ] **Step 9: Commit**

```bash
git add scripts/alchemist/vault.py scripts/build_vault_index.py tests/test_vault_index.py
git commit -m "feat(vault): index the wiki for the Phase 2 attach agents

One index of slug, title, type and topics, read once per agent instead of
forty greps per batch. An article with no confidentiality field is skipped
and named in the index foot rather than defaulted, because this repo is
public and an unknown classification is what check 11 refuses.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 3: Add check 11 and sweep the docs from ten to eleven

**Files:**
- Modify: `scripts/alchemist/checks.py` (add the check, register it in `run_all`, and the module
  docstring's first line)
- Create: `tests/test_check_attached_articles.py`
- Modify: `CLAUDE.md`, `README.md`, `.github/workflows/pages.yml`,
  `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`

**Interfaces:**
- Consumes: `article_path` and `PUBLISHABLE_ARTICLE` from `scripts.alchemist.vault` (task 2);
  `Result` and `vault_root` already in `checks.py`.
- Produces: `check_attached_articles(corpus: Corpus, vault: Path) -> Result`, registered last in
  `run_all`, so the CLI reports it as rule 11.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_check_attached_articles.py`:

```python
from pathlib import Path

import pytest

from scripts.alchemist.checks import check_attached_articles
from scripts.alchemist.model import load_corpus

from tests.test_vault_index import write_article

NODE = """---
id: {id}
title: {title}
domains: [stats]
status: stub
requires: []
spends: []
anchor: [chosen]
vault_articles: [{articles}]
vault_sources: []
taught_in: null
---

A body.
"""


@pytest.fixture
def corpus_and_vault(tmp_path):
    root, vault = tmp_path / "repo", tmp_path / "vault"
    for sub in ("nodes", "paths", "notation", "sources"):
        (root / sub).mkdir(parents=True)
    (root / "notation" / "objects.yaml").write_text("[]\n")
    (root / "sources" / "wanted.yaml").write_text("[]\n")
    (vault / "wiki").mkdir(parents=True)
    write_article(vault, "methods/glm")
    write_article(vault, "methods/paid", confidentiality="public-paid")
    return root, vault


def write_node(root, node_id, articles=""):
    (root / "nodes" / f"{node_id}.md").write_text(
        NODE.format(id=node_id, title=node_id, articles=articles))


def test_a_resolving_public_free_slug_passes(corpus_and_vault):
    root, vault = corpus_and_vault
    write_node(root, "a", "methods/glm")
    assert check_attached_articles(load_corpus(root), vault).failures == []


def test_a_resolving_public_paid_slug_passes(corpus_and_vault):
    """Check 5's rule, restated: purchased material informs a node through
    vault_articles because the article stays private and the prose is ours.
    Only vault_sources, which means the node quotes it, needs a waiver."""
    root, vault = corpus_and_vault
    write_node(root, "a", "methods/paid")
    assert check_attached_articles(load_corpus(root), vault).failures == []


def test_a_slug_resolving_to_nothing_fails_and_names_the_path(corpus_and_vault):
    """A fabricated slug or a stale rename. This is the arm that makes an
    agent's claim mechanically checkable."""
    root, vault = corpus_and_vault
    write_node(root, "a", "methods/invented")
    failures = check_attached_articles(load_corpus(root), vault).failures
    assert len(failures) == 1
    assert "does not resolve" in failures[0]
    assert "methods/invented.md" in failures[0]


def test_an_unclassified_article_fails_distinctly(corpus_and_vault):
    """Distinct from the resolution arm on purpose. This one fires when an
    article loses its classification in the vault after attachment, and a
    reclassification should not read as a rename."""
    root, vault = corpus_and_vault
    (vault / "wiki" / "methods" / "bare.md").write_text(
        "---\ntitle: Bare\nslug: methods/bare\ntype: method\ntopics: []\n---\n\nBody.\n")
    write_node(root, "a", "methods/bare")
    failures = check_attached_articles(load_corpus(root), vault).failures
    assert len(failures) == 1
    assert "carries no confidentiality field" in failures[0]
    assert "does not resolve" not in failures[0]


def test_the_check_skips_where_no_vault_is_present(corpus_and_vault):
    """CI has no vault, so this arm is what stops the deploy failing. It also
    means CI does not gate a fabricated slug; the pre-commit hook does."""
    root, _ = corpus_and_vault
    write_node(root, "a", "methods/invented")
    result = check_attached_articles(load_corpus(root), Path("/nonexistent"))
    assert result.skipped is not None
    assert result.failures == []
```

- [ ] **Step 2: Run them to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_check_attached_articles.py -v`
Expected: FAIL, collecting with `ImportError: cannot import name 'check_attached_articles'`.

- [ ] **Step 3: Write the check**

In `scripts/alchemist/checks.py`, add `from .vault import PUBLISHABLE_ARTICLE, article_path` to
the imports, then insert before `def run_all`:

```python
def check_attached_articles(corpus: Corpus, vault: Path) -> Result:
    """An attached slug has to name a real, classified wiki article.

    Phase 2 attaches through agents, and an agent can produce a plausible slug
    for an article that does not exist. Resolution is the mechanical answer:
    a fabricated slug fails here rather than waiting for a Phase 3 writer to
    open nothing.

    The two arms report differently on purpose. A slug naming no file is a
    fabrication or a stale rename, whereas a slug whose article carries no
    confidentiality field is an article reclassified in the vault after it was
    attached, and a debugging session should not have to guess which happened.
    """
    result = Result("11. attached vault articles resolve and are publishable")
    if not (vault / "wiki").is_dir():
        result.skipped = f"no vault wiki at {vault}"
        return result
    for node in sorted(corpus.nodes.values(), key=lambda n: n.id):
        for slug in node.vault_articles:
            path = article_path(vault, slug)
            if not path.is_file():
                result.failures.append(
                    f"{node.id}: attaches {slug!r}, which does not resolve; "
                    f"looked for {path}"
                )
                continue
            match = FRONTMATTER.match(path.read_text())
            meta = yaml.safe_load(match.group(1)) if match else None
            confidentiality = meta.get("confidentiality") if isinstance(meta, dict) else None
            if confidentiality is None:
                result.failures.append(
                    f"{node.id}: attaches {slug!r}, whose article at {path} "
                    f"carries no confidentiality field, so it cannot be read"
                )
            elif confidentiality not in PUBLISHABLE_ARTICLE:
                result.failures.append(
                    f"{node.id}: attaches {slug!r}, which is {confidentiality!r} "
                    f"rather than public-free or public-paid, and this repo is public"
                )
    return result
```

Then add it as the last entry of `run_all`'s list:

```python
        check_titles_sentence_case(corpus),
        check_attached_articles(corpus, vault),
    ]
```

And change the module docstring's first line from `"""The ten rules. Each returns a Result, so the
runner reports every failure in` to `"""The eleven rules. Each returns a Result, so the runner
reports every failure in`.

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_check_attached_articles.py -v`
Expected: 5 passed.

- [ ] **Step 5: Run the checks over the real corpus**

Run: `.venv/bin/python scripts/check.py`

Expected: eleven rules reported, all ok, at `1560 nodes, 13 paths, 0 failures`. Every node still
carries `vault_articles: []`, so check 11 has nothing to resolve yet and passes trivially. That
is the correct state before wave one.

- [ ] **Step 6: Confirm the skip arm behaves as the spec says**

Run: `ALCHEMIST_VAULT=/nonexistent .venv/bin/python scripts/check.py`

Expected: `SKIP  5. quoted sources are publishable` and `SKIP  11. attached vault articles resolve
and are publishable`, with the other nine ok and exit 0. This is what CI will print, and it is why
the spec says check 11 gates the hook rather than the build.

- [ ] **Step 7: Sweep the docs from ten to eleven**

Make exactly these edits. Each was located by
`grep -rn "ten check\|ten rule\|10 check"` and there are no others outside `.superpowers/` and
`site/`.

`CLAUDE.md`:
- Line 84, `## The ten checks` becomes `## The eleven checks`.
- Line 86, `enforces ten rules` becomes `enforces eleven rules`.
- In the rule list, after `Rule 10, added at gate 2, is that every title is sentence case.`
  append ` Rule 11, added for Phase 2, is that every attached vault article resolves to a real
  wiki file and is public-free or public-paid.`
- In the check 5 paragraph, replace `Measured with `ALCHEMIST_VAULT=/nonexistent`, it is the only
  rule that skips: check 6 reads` with `Measured with `ALCHEMIST_VAULT=/nonexistent`, checks 5
  and 11 are the two rules that skip, since both read the vault: check 6 reads`.
- Line 117, `# the ten checks` becomes `# the eleven checks`.
- Line 179, `` `checks.py` for the ten rules `` becomes `` `checks.py` for the eleven rules ``.

`README.md`:
- Line 40, `enforces ten rules` becomes `enforces eleven rules`, and add the rule 11 clause to
  the list that follows it.
- Line 50, `nine of the ten checks` becomes `nine of the eleven checks`, and correct the
  following sentence's count to match: two rules skip without a vault, not one.

`.github/workflows/pages.yml`:
- Line 91, `name: Run the ten checks` becomes `name: Run the eleven checks`.

`docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`:
- Line 286, `enforces ten rules` becomes `enforces eleven rules`.
- Line 364, `# the ten checks above` becomes `# the eleven checks above`.

Do **not** edit `notes/phase-1-close-out-report-2026-09.md`. It records a measurement taken on
8 September against ten checks, and a historical measurement is not corrected.

- [ ] **Step 8: Verify no stale count survives**

Run: `grep -rn "ten check\|ten rule\|nine of the ten" --include="*.md" --include="*.yml" --include="*.py" . | grep -v "^./.superpowers\|^./site/\|close-out-report\|plans/2026-09-08"`

Expected: no output. The Phase 1 plan and report are history and keep their counts.

- [ ] **Step 9: Run the suite**

Run: `.venv/bin/python -m pytest -q`
Expected: 238 passed. `tests/test_cli.py` may assert the reported rule count; if a test fails on
the number of rules, update it to eleven rather than working around it.

- [ ] **Step 10: Commit**

```bash
git add scripts/alchemist/checks.py tests/test_check_attached_articles.py CLAUDE.md README.md .github/workflows/pages.yml docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md
git commit -m "feat(checks): add check 11 on attached vault articles

Every vault_articles slug has to resolve to a real wiki file and be
public-free or public-paid, so an agent's fabricated slug fails
mechanically. The resolution and classification arms report separately,
because a rename and a reclassification are different problems. Like
check 5 it skips where no vault is mounted, so it gates the pre-commit
hook rather than CI, and the docs now count eleven rules.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 4: Write the attach tool

Thirty-nine agents editing YAML frontmatter by hand would produce thirty-nine styles and the
occasional broken file. One tool parses the node, replaces one field and re-renders through the
existing `render`, so every write is identical in shape and a bad slug is refused at the door.

**Files:**
- Create: `scripts/attach_articles.py`
- Create: `tests/test_attach_articles.py`

**Interfaces:**
- Consumes: `parse_node` from `scripts.alchemist.model`, `render` from
  `scripts.alchemist.staging`, `article_path` and `PUBLISHABLE_ARTICLE` from
  `scripts.alchemist.vault`, `vault_root` from `scripts.alchemist.checks`.
- Produces: a CLI only. Agents call
  `.venv/bin/python scripts/attach_articles.py --node <id> --articles <slug> [<slug> ...]`,
  and `--articles` with no values clears the field.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_attach_articles.py`:

```python
import subprocess
import sys
from pathlib import Path

import pytest

from scripts.alchemist.model import parse_node

from tests.test_check_attached_articles import NODE, corpus_and_vault, write_node
from tests.test_vault_index import write_article

REPO = Path(__file__).resolve().parents[1]


def run(root, vault, *args):
    return subprocess.run(
        [sys.executable, "scripts/attach_articles.py",
         "--root", str(root), "--vault", str(vault), *args],
        capture_output=True, text=True, cwd=REPO,
    )


def test_it_sets_the_field_sorted(corpus_and_vault):
    """Sorted, so a rerun of the same batch is byte-identical."""
    root, vault = corpus_and_vault
    write_node(root, "a")
    result = run(root, vault, "--node", "a", "--articles", "methods/paid", "methods/glm")
    assert result.returncode == 0
    assert parse_node(root / "nodes" / "a.md").vault_articles == ("methods/glm", "methods/paid")


def test_it_refuses_a_slug_that_does_not_resolve(corpus_and_vault):
    root, vault = corpus_and_vault
    write_node(root, "a")
    result = run(root, vault, "--node", "a", "--articles", "methods/invented")
    assert result.returncode == 2
    assert "does not resolve" in result.stderr
    assert parse_node(root / "nodes" / "a.md").vault_articles == ()


def test_it_refuses_an_unclassified_article(corpus_and_vault):
    root, vault = corpus_and_vault
    (vault / "wiki" / "methods" / "bare.md").write_text(
        "---\ntitle: Bare\nslug: methods/bare\ntype: method\ntopics: []\n---\n\nBody.\n")
    write_node(root, "a")
    result = run(root, vault, "--node", "a", "--articles", "methods/bare")
    assert result.returncode == 2
    assert "confidentiality" in result.stderr
    assert parse_node(root / "nodes" / "a.md").vault_articles == ()


def test_it_refuses_an_unknown_node(corpus_and_vault):
    root, vault = corpus_and_vault
    result = run(root, vault, "--node", "ghost", "--articles", "methods/glm")
    assert result.returncode == 2
    assert "no such node" in result.stderr


def test_no_articles_clears_the_field_and_touches_nothing_else(corpus_and_vault):
    """An uncovered node keeps an empty list, and the rest of the record has
    to survive the round trip through render untouched."""
    root, vault = corpus_and_vault
    write_node(root, "a", "methods/glm")
    before = parse_node(root / "nodes" / "a.md")
    assert run(root, vault, "--node", "a", "--articles").returncode == 0
    after = parse_node(root / "nodes" / "a.md")
    assert after.vault_articles == ()
    assert (after.id, after.title, after.domains, after.status,
            after.requires, after.anchor, after.body) == (
        before.id, before.title, before.domains, before.status,
        before.requires, before.anchor, before.body)
```

- [ ] **Step 2: Run them to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_attach_articles.py -v`
Expected: FAIL, every test returning a non-zero code with
`can't open file 'scripts/attach_articles.py'` on stderr.

- [ ] **Step 3: Write the tool**

Create `scripts/attach_articles.py`:

```python
"""Set one node's vault_articles, refusing a slug that will not survive check 11.

    .venv/bin/python scripts/attach_articles.py --node hazard-rate \
        --articles methods/survival-analysis concepts/default-intensity

    .venv/bin/python scripts/attach_articles.py --node hazard-rate --articles

The second form clears the field, which is what an uncovered node keeps.

Thirty-nine Phase 2 agents write these fields, and hand-edited YAML would give
thirty-nine styles and the occasional unparseable record. This tool re-renders
the whole record through the same `render` the staging merge uses, so every
write is identical in shape, and it validates each slug against the vault first
so a fabrication is refused here rather than at the pre-commit hook.
"""

import argparse
import sys
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from scripts.alchemist.checks import vault_root
from scripts.alchemist.model import FRONTMATTER, parse_node
from scripts.alchemist.staging import render
from scripts.alchemist.vault import PUBLISHABLE_ARTICLE, article_path

REPO = Path(__file__).resolve().parents[1]


def _complaint(vault: Path, slug: str) -> str | None:
    """None where the slug is attachable, otherwise why it is not."""
    path = article_path(vault, slug)
    if not path.is_file():
        return f"{slug!r} does not resolve; looked for {path}"
    match = FRONTMATTER.match(path.read_text())
    meta = yaml.safe_load(match.group(1)) if match else None
    confidentiality = meta.get("confidentiality") if isinstance(meta, dict) else None
    if confidentiality is None:
        return f"{slug!r} carries no confidentiality field at {path}"
    if confidentiality not in PUBLISHABLE_ARTICLE:
        return f"{slug!r} is {confidentiality!r} rather than public-free or public-paid"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--node", required=True)
    parser.add_argument("--articles", nargs="*", default=[])
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--vault", type=Path, default=None)
    args = parser.parse_args()

    vault = args.vault or vault_root()
    node_file = args.root / "nodes" / f"{args.node}.md"
    if not node_file.is_file():
        print(f"no such node {args.node!r} at {node_file}", file=sys.stderr)
        return 2

    slugs = sorted(set(args.articles))
    complaints = [c for c in (_complaint(vault, s) for s in slugs) if c]
    if complaints:
        for complaint in complaints:
            print(f"{args.node}: {complaint}", file=sys.stderr)
        return 2

    node = parse_node(node_file)
    node_file.write_text(render(replace(node, vault_articles=tuple(slugs))))
    print(f"{args.node}: {len(slugs)} articles attached")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_attach_articles.py -v`
Expected: 5 passed.

- [ ] **Step 5: Prove the round trip is lossless on a real record**

```bash
cp nodes/hazard-rate.md /tmp/hazard-rate.before
.venv/bin/python scripts/attach_articles.py --node hazard-rate --articles
diff /tmp/hazard-rate.before nodes/hazard-rate.md && echo "byte-identical"
```

Expected: `byte-identical`. Clearing an already-empty field has to be a no-op at the byte level,
which is what proves `render` reproduces a committed record exactly. Should the diff show
anything, stop: `render` disagrees with the committed corpus and 1,560 files are about to be
reformatted. Report it rather than proceeding.

- [ ] **Step 6: Run the suite and the checks**

Run: `.venv/bin/python -m pytest -q && .venv/bin/python scripts/check.py && git status --short`
Expected: 243 passed, eleven rules ok, clean tree.

- [ ] **Step 7: Commit**

```bash
git add scripts/attach_articles.py tests/test_attach_articles.py
git commit -m "feat(attach): set vault_articles through a tool rather than by hand

Thirty-nine agents hand-editing frontmatter would give thirty-nine styles
and the occasional unparseable record. This re-renders the whole record
through the staging renderer and validates each slug against the vault
first, so a fabrication is refused at the door and every write sorts.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 5: Build the batch manifest, and the diff verifier

**Files:**
- Create: `scripts/alchemist/batches.py`
- Create: `scripts/build_manifest.py`
- Create: `tests/test_batches.py`
- Modify: `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md` (section 10's cap
  sentence, per spec section 12)

**Interfaces:**
- Consumes: `load_corpus` from `scripts.alchemist.model`.
- Produces:
  - `slice_batches(node_ids: list[str], size: int = 40) -> list[list[str]]`
  - `wave_of(batch_number: int, per_wave: int = 13) -> int`, one-based batch to one-based wave.
  - `stray_writes(manifest: dict, batch_number: int, changed: list[str]) -> list[str]`, returning
    the changed node ids that the batch does not own.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_batches.py`:

```python
import pytest

from scripts.alchemist.batches import slice_batches, stray_writes, wave_of


def test_the_corpus_slices_into_thirty_nine_batches_of_forty():
    ids = [f"n{i:04d}" for i in range(1560)]
    batches = slice_batches(ids)
    assert len(batches) == 39
    assert all(len(b) == 40 for b in batches)
    assert batches[0][0] == "n0000"
    assert batches[38][-1] == "n1559"
    assert [i for b in batches for i in b] == ids


def test_a_short_final_batch_is_kept_rather_than_padded():
    assert [len(b) for b in slice_batches([f"n{i}" for i in range(85)])] == [40, 40, 5]


def test_batches_map_to_three_waves_of_thirteen():
    """Thirty-nine agents exceed the fifteen-agent guideline, so the batches
    run in waves. Spec section 10 said forty per agent fits inside the cap,
    which it does not; three waves of thirteen is what does."""
    assert wave_of(1) == 1
    assert wave_of(13) == 1
    assert wave_of(14) == 2
    assert wave_of(26) == 2
    assert wave_of(27) == 3
    assert wave_of(39) == 3


def test_a_write_outside_the_batch_is_reported():
    manifest = {"batches": {1: ["a", "b"], 2: ["c"]}}
    assert stray_writes(manifest, 1, ["a", "b"]) == []
    assert stray_writes(manifest, 1, ["a", "c", "zz"]) == ["c", "zz"]
```

- [ ] **Step 2: Run them to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_batches.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'scripts.alchemist.batches'`.

- [ ] **Step 3: Write the module**

Create `scripts/alchemist/batches.py`:

```python
"""Slicing the corpus into agent batches, and catching a write outside one.

The slice runs over sorted node ids, so a rerun reproduces the same batches.
The manifest then records the ids explicitly rather than the slice bounds: a
manifest read after the corpus has changed still describes the work that was
actually done, whereas bounds would silently re-point at different nodes.
"""

from __future__ import annotations

BATCH_SIZE = 40
PER_WAVE = 13


def slice_batches(node_ids: list[str], size: int = BATCH_SIZE) -> list[list[str]]:
    ordered = sorted(node_ids)
    return [ordered[i:i + size] for i in range(0, len(ordered), size)]


def wave_of(batch_number: int, per_wave: int = PER_WAVE) -> int:
    """One-based batch to one-based wave. Thirty-nine batches at thirteen a
    wave is three waves, which is what fits the fifteen-agent guideline."""
    return (batch_number - 1) // per_wave + 1


def stray_writes(manifest: dict, batch_number: int, changed: list[str]) -> list[str]:
    """Changed node ids the batch does not own, sorted.

    Batches are disjoint, which is the whole reason agents write node files
    directly. This is what verifies the assumption instead of trusting it.
    """
    owned = set(manifest["batches"][batch_number])
    return sorted(set(changed) - owned)
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_batches.py -v`
Expected: 4 passed.

- [ ] **Step 5: Write the CLI**

Create `scripts/build_manifest.py`:

```python
"""Write the Phase 2 batch manifest.

    .venv/bin/python scripts/build_manifest.py

Writes `.staging/phase-2/manifest.yaml`: one entry per batch, carrying its wave
and its explicit node ids. The directory is gitignored, and the manifest is
rebuilt from the corpus rather than kept.
"""

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from scripts.alchemist.batches import slice_batches, wave_of
from scripts.alchemist.model import load_corpus

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--out", type=Path, default=REPO / ".staging" / "phase-2" / "manifest.yaml")
    args = parser.parse_args()

    corpus = load_corpus(args.root)
    batches = slice_batches(list(corpus.nodes))
    payload = {
        "built": date.today().isoformat(),
        "nodes": len(corpus.nodes),
        "batches": {
            number: {"wave": wave_of(number), "nodes": ids}
            for number, ids in enumerate(batches, start=1)
        },
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(yaml.safe_dump(payload, sort_keys=False))
    waves = max(wave_of(n) for n in range(1, len(batches) + 1))
    print(f"{len(corpus.nodes)} nodes -> {len(batches)} batches across {waves} waves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 6: Run it against the real corpus**

Run: `.venv/bin/python scripts/build_manifest.py`
Expected: `1560 nodes -> 39 batches across 3 waves`.

Then `git status --short` and expect no output, since `.staging/` is ignored from task 1.

- [ ] **Step 7: Amend spec section 10's cap sentence**

In `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`, section 10, replace:

```
Batch roughly forty nodes per
agent, which fits inside the cap and is better practice anyway: an agent that reads the
notation contract once should spend it on more than one node.
```

with:

```
Batch roughly forty nodes per
agent, which is better practice anyway, since an agent that reads the notation contract once
should spend it on more than one node. Forty per agent does not fit inside the cap in one go:
Phase 2's 1,560 nodes come to thirty-nine agents, so the batches run as three sequential waves
of thirteen. Phase 3 will need the same arithmetic.
```

- [ ] **Step 8: Strike the `guides` instruction from spec section 9**

In the same file, section 9's Phase 2 row, remove `Read `guides` once as hints, then drop it` and
the sentence connecting it. No node carries a `guides` field, measured across all 1,560 records on
9 September 2026, so the instruction sends a future reader hunting for something that is not there.

- [ ] **Step 9: Run the suite and the checks**

Run: `.venv/bin/python -m pytest -q && .venv/bin/python scripts/check.py`
Expected: 247 passed, eleven rules ok.

- [ ] **Step 10: Commit**

```bash
git add scripts/alchemist/batches.py scripts/build_manifest.py tests/test_batches.py docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md
git commit -m "feat(batches): slice the corpus into 39 batches across 3 waves

The manifest names each batch's ids explicitly rather than its slice
bounds, so it still describes the work after the corpus changes, and
stray_writes checks the disjointness that direct node writes assume.
Section 10's claim that forty per agent fits inside the fifteen-agent cap
is corrected, and section 9's guides instruction struck: no node has that
field.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 6: Write the ledger merge

**Files:**
- Create: `scripts/alchemist/ledger.py`
- Create: `scripts/merge_ledger.py`
- Create: `tests/test_ledger.py`

**Interfaces:**
- Consumes: nothing from earlier tasks beyond the fragment shape task 8 writes.
- Produces:
  - `read_fragments(staging: Path) -> tuple[list[dict], list[str]]`
  - `union_entries(seeded: list[dict], proposed: list[dict]) -> tuple[list[dict], list[str]]`,
    returning merged entries sorted by id, and a list of field-disagreement complaints.

A fragment is a YAML list of mappings, each carrying `id`, `needed_by`, `claim`, `document`,
`expected_tier`, `acquisition` and optionally `url` and `note`, matching the header vocabulary of
`sources/wanted.yaml`.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_ledger.py`:

```python
import pytest
import yaml

from scripts.alchemist.ledger import read_fragments, union_entries

ENTRY = {
    "id": "ifoa-cs2-core-reading-2026",
    "needed_by": ["hazard-rate"],
    "claim": "The standard treatment of the hazard function.",
    "document": "IFoA CS2 Core Reading, 2026",
    "expected_tier": "T4",
    "acquisition": "purchased-personal",
    "status": "wanted",
}


def fragment(staging, number, entries):
    staging.mkdir(parents=True, exist_ok=True)
    path = staging / f"ledger-{number:02d}.yaml"
    path.write_text(yaml.safe_dump(entries, sort_keys=False))
    return path


def test_two_fragments_naming_one_document_union_their_needed_by(tmp_path):
    a = dict(ENTRY, needed_by=["hazard-rate"])
    b = dict(ENTRY, needed_by=["survival-function", "hazard-rate"])
    merged, complaints = union_entries([], [a, b])
    assert complaints == []
    assert len(merged) == 1
    assert merged[0]["needed_by"] == ["hazard-rate", "survival-function"]


def test_a_seeded_entry_is_preserved_and_only_extended(tmp_path):
    """The four Phase 1 entries keep every field. A fragment naming one of
    them adds node ids and changes nothing else."""
    seeded = dict(ENTRY, claim="The seeded claim.", note="Keep me.")
    proposed = dict(ENTRY, needed_by=["new-node"], claim="A different claim.")
    merged, complaints = union_entries([seeded], [proposed])
    assert merged[0]["claim"] == "The seeded claim."
    assert merged[0]["note"] == "Keep me."
    assert merged[0]["needed_by"] == ["hazard-rate", "new-node"]
    assert any("claim" in c for c in complaints)


def test_distinct_documents_stay_distinct_and_sort_by_id(tmp_path):
    other = dict(ENTRY, id="assa-f107-notes", needed_by=["binning"])
    merged, _ = union_entries([], [ENTRY, other])
    assert [e["id"] for e in merged] == ["assa-f107-notes", "ifoa-cs2-core-reading-2026"]


def test_read_fragments_collects_every_file_in_order(tmp_path):
    staging = tmp_path / "phase-2"
    fragment(staging, 2, [dict(ENTRY, needed_by=["b"])])
    fragment(staging, 1, [dict(ENTRY, needed_by=["a"])])
    entries, complaints = read_fragments(staging)
    assert complaints == []
    assert [e["needed_by"] for e in entries] == [["a"], ["b"]]


def test_a_malformed_fragment_is_a_complaint_rather_than_a_trace(tmp_path):
    """Following _ledger_entries' precedent in checks.py, whose docstring
    records the three shapes that used to crash: a bare string in the list,
    a mapping where a list belongs, and a missing id."""
    staging = tmp_path / "phase-2"
    fragment(staging, 1, [ENTRY])
    (staging / "ledger-02.yaml").write_text("- just a string\n")
    (staging / "ledger-03.yaml").write_text(yaml.safe_dump([{"needed_by": ["a"]}]))
    (staging / "ledger-04.yaml").write_text("id: not a list\n")
    entries, complaints = read_fragments(staging)
    assert len(complaints) == 3
    assert any("ledger-02" in c for c in complaints)
    assert any("ledger-03" in c and "id" in c for c in complaints)
    assert any("ledger-04" in c for c in complaints)


def test_a_missing_needed_by_becomes_an_empty_list(tmp_path):
    """checks.py's rule 9 reads needed_by on every entry, so an entry that
    reaches the ledger without one would disable check 6 silently."""
    merged, _ = union_entries([], [{k: v for k, v in ENTRY.items() if k != "needed_by"}])
    assert merged[0]["needed_by"] == []
```

- [ ] **Step 2: Run them to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_ledger.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'scripts.alchemist.ledger'`.

- [ ] **Step 3: Write the module**

Create `scripts/alchemist/ledger.py`:

```python
"""Unioning the Phase 2 agents' ledger fragments into one gap ledger.

Thirty-nine agents each propose the documents their uncovered nodes need, and
many propose the same document. Unioning by document id is what turns roughly a
thousand uncovered nodes into a ledger Mario can read in one sitting.

A seeded entry wins every field it already carries. Phase 1 wrote those four by
hand with a considered claim and a primary alternative, and an agent's guess at
the same document should extend the node list rather than overwrite the
reasoning. The disagreement is reported rather than dropped.
"""

from __future__ import annotations

from pathlib import Path

import yaml


def _normalise(entry: dict) -> dict:
    """A returned entry always carries a needed_by list, sorted and unique.

    Rule 9 reads needed_by on every entry, and rule 6 enforces gap closure
    through it, so an entry arriving without one would disable check 6 for its
    nodes silently and permanently.
    """
    needed_by = entry.get("needed_by")
    if not isinstance(needed_by, list):
        needed_by = []
    return {**entry, "needed_by": sorted({str(n) for n in needed_by})}


def read_fragments(staging: Path) -> tuple[list[dict], list[str]]:
    """Every proposed entry across the fragments, plus a complaint per bad shape."""
    entries: list[dict] = []
    complaints: list[str] = []
    for path in sorted(staging.glob("ledger-*.yaml")):
        try:
            loaded = yaml.safe_load(path.read_text())
        except yaml.YAMLError as exc:
            complaints.append(f"{path.name}: does not parse ({exc.__class__.__name__})")
            continue
        if not isinstance(loaded, list):
            complaints.append(f"{path.name}: is not a list of entries")
            continue
        for position, entry in enumerate(loaded, start=1):
            if not isinstance(entry, dict):
                complaints.append(f"{path.name}: entry {position} is not a mapping")
            elif not entry.get("id"):
                complaints.append(f"{path.name}: entry {position} has no id")
            else:
                entries.append(entry)
    return entries, complaints


def union_entries(
    seeded: list[dict], proposed: list[dict]
) -> tuple[list[dict], list[str]]:
    """Merged entries sorted by id, plus a complaint per field disagreement."""
    merged: dict[str, dict] = {}
    complaints: list[str] = []
    for entry in [_normalise(e) for e in seeded]:
        merged[entry["id"]] = entry
    for entry in [_normalise(e) for e in proposed]:
        key = entry["id"]
        if key not in merged:
            merged[key] = entry
            continue
        held = merged[key]
        for field, value in entry.items():
            if field == "needed_by":
                continue
            if field in held and held[field] != value:
                complaints.append(
                    f"{key}: {field} differs; keeping {held[field]!r} over {value!r}"
                )
            elif field not in held:
                held[field] = value
        held["needed_by"] = sorted(set(held["needed_by"]) | set(entry["needed_by"]))
    return [merged[key] for key in sorted(merged)], complaints
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_ledger.py -v`
Expected: 6 passed.

- [ ] **Step 5: Write the CLI**

Create `scripts/merge_ledger.py`:

```python
"""Merge the Phase 2 ledger fragments into sources/wanted.yaml.

    .venv/bin/python scripts/merge_ledger.py

The only writer of that file during Phase 2. It refuses to write at all where
any fragment is malformed, because a partial ledger reaching the gate wearing
the appearance of a complete one is worse than no ledger: acquisition is
decided off it.

Field disagreements are printed and do not block. The seeded entry's value
stands, and the note tells you where an agent thought otherwise.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from scripts.alchemist.ledger import read_fragments, union_entries

REPO = Path(__file__).resolve().parents[1]
HEADER_MARK = "# Sources the corpus needs"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--staging", type=Path, default=REPO / ".staging" / "phase-2")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    ledger = args.root / "sources" / "wanted.yaml"
    text = ledger.read_text()
    header = text[:text.index("- id:")] if "- id:" in text else text
    seeded = yaml.safe_load(text) or []

    proposed, complaints = read_fragments(args.staging)
    if complaints:
        for complaint in complaints:
            print(f"malformed: {complaint}", file=sys.stderr)
        print(f"{len(complaints)} malformed fragments; nothing written", file=sys.stderr)
        return 2

    merged, disagreements = union_entries(seeded, proposed)
    for disagreement in disagreements:
        print(f"note: {disagreement}", file=sys.stderr)

    if args.dry_run:
        print(f"would write {len(merged)} entries ({len(seeded)} seeded)")
        return 0

    ledger.write_text(header + yaml.safe_dump(merged, sort_keys=False, allow_unicode=True))
    print(f"{len(merged)} entries written ({len(seeded)} seeded, "
          f"{len(merged) - len(seeded)} new), {len(disagreements)} disagreements")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 6: Dry-run it against the real ledger with no fragments**

Run: `.venv/bin/python scripts/merge_ledger.py --dry-run`
Expected: `would write 4 entries (4 seeded)`. With no fragments present the union is the identity,
which is the cheapest proof the header split and the seeded read are right.

- [ ] **Step 7: Run the suite and the checks**

Run: `.venv/bin/python -m pytest -q && .venv/bin/python scripts/check.py && git status --short`
Expected: 253 passed, eleven rules ok, clean tree.

- [ ] **Step 8: Commit**

```bash
git add scripts/alchemist/ledger.py scripts/merge_ledger.py tests/test_ledger.py
git commit -m "feat(ledger): union the Phase 2 fragments into one gap ledger

Unioning by document id turns roughly a thousand uncovered nodes into a
ledger of tens. A seeded entry keeps every field it carries and only
gains node ids, with any disagreement reported, and a malformed fragment
blocks the whole write rather than producing a partial ledger that looks
complete.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 7: Write the coverage report

**Files:**
- Create: `scripts/alchemist/coverage.py`
- Create: `scripts/build_coverage_report.py`
- Create: `tests/test_coverage.py`

**Interfaces:**
- Consumes: `load_corpus` from `scripts.alchemist.model`.
- Produces:
  - `by_domain(corpus) -> list[tuple[str, int, int]]`, being domain, members, attached.
  - `by_anchor_document(corpus) -> list[tuple[str, int, int]]`, being the `<body>.<subject>`
    prefix, members, attached.
  - `attachment_histogram(corpus) -> dict[int, int]`, attachments per node to node count.
  - `render_report(corpus, index_built: str) -> str`.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_coverage.py`:

```python
import pytest

from scripts.alchemist.coverage import (
    attachment_histogram, by_anchor_document, by_domain, render_report,
)
from scripts.alchemist.model import load_corpus

from tests.test_check_attached_articles import corpus_and_vault, write_node


def test_domain_counts_split_members_from_attached(corpus_and_vault):
    root, _ = corpus_and_vault
    write_node(root, "a", "methods/glm")
    write_node(root, "b")
    assert by_domain(load_corpus(root)) == [("stats", 2, 1)]


def test_anchor_documents_group_on_body_and_subject(corpus_and_vault):
    """The ledger bound rests on this grouping: 59 documents across the whole
    corpus, so an uncovered node's entry names one of 59 rather than a new one."""
    root, _ = corpus_and_vault
    (root / "nodes" / "a.md").write_text(
        (root / "nodes" / "a.md").read_text().replace(
            "anchor: [chosen]", "anchor: [ifoa.cs2.1.1-5]"))
    rows = by_anchor_document(load_corpus(root))
    assert ("ifoa.cs2", 1, 0) in rows


def test_the_histogram_counts_nodes_per_attachment_count(corpus_and_vault):
    root, _ = corpus_and_vault
    write_node(root, "a", "methods/glm")
    write_node(root, "b", "methods/glm, methods/paid")
    write_node(root, "c")
    assert attachment_histogram(load_corpus(root)) == {0: 1, 1: 1, 2: 1}


def test_the_report_names_the_index_build_date(corpus_and_vault):
    """A stale index is what makes an attachment wrong, so the report has to
    say which index produced it."""
    root, _ = corpus_and_vault
    write_node(root, "a")
    report = render_report(load_corpus(root), "2026-09-10")
    assert "2026-09-10" in report
    assert "Coverage by domain" in report
```

- [ ] **Step 2: Run them to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_coverage.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'scripts.alchemist.coverage'`.

- [ ] **Step 3: Write the module and the CLI**

Create `scripts/alchemist/coverage.py` implementing the four functions above. `by_domain` and
`by_anchor_document` both return rows sorted by member count descending then by name, and
`by_anchor_document` takes the first two dot-separated segments of each anchor, skipping the
literal `chosen`. `render_report` writes markdown with a title, the index build date, a totals
line, a "Coverage by domain" table, a "Coverage by anchor document" table, an "Attachments per
node" table from the histogram, and a closing section listing every anchor document with no
attachment at all, which is the acquisition question stated plainly.

Create `scripts/build_coverage_report.py` as a thin CLI taking `--root`, `--index` (default
`data/vault-index.yaml`, read only for its `built` date) and `--out` (default
`notes/phase-2-coverage-2026-09.md`), and printing the totals line it wrote.

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_coverage.py -v`
Expected: 4 passed.

- [ ] **Step 5: Run it against the unattached corpus as a baseline**

```bash
.venv/bin/python scripts/build_vault_index.py
.venv/bin/python scripts/build_coverage_report.py --out /tmp/phase-2-baseline.md
head -40 /tmp/phase-2-baseline.md
```

Expected: 1,560 nodes, 0 attached, and 59 anchor documents in the table. The 59 is the check that
matters: it is the figure the spec's ledger bound rests on. Write to `/tmp` here, so the real note
is generated once after the waves rather than committed empty.

- [ ] **Step 6: Run the suite and the checks**

Run: `.venv/bin/python -m pytest -q && .venv/bin/python scripts/check.py`
Expected: 257 passed, eleven rules ok.

- [ ] **Step 7: Commit**

```bash
git add scripts/alchemist/coverage.py scripts/build_coverage_report.py tests/test_coverage.py
git commit -m "feat(coverage): generate the Phase 2 gate report

Coverage by domain and by anchor document, the attachments-per-node
histogram, and the anchor documents with nothing attached at all, which
is the acquisition question the gate exists to put. The report names the
index build date, because a stale index is what makes an attachment wrong.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

---

### Task 8: Run wave one, thirteen agents over batches 1 to 13

The tools are done and tested. From here the work is dispatch and review rather than code.

**Files:**
- Modify: `nodes/*.md` for batches 1 to 13 (520 nodes), `vault_articles` only
- Create: `.staging/phase-2/ledger-01.yaml` to `ledger-13.yaml` and
  `report-01.md` to `report-13.md` (gitignored)

**Interfaces:**
- Consumes: `scripts/attach_articles.py` (task 4), `data/vault-index.yaml` (task 2),
  `.staging/phase-2/manifest.yaml` (task 5).
- Produces: 520 nodes carrying their attachments, and thirteen fragment pairs task 10 merges.

- [ ] **Step 1: Rebuild the index and the manifest**

```bash
.venv/bin/python scripts/build_vault_index.py
.venv/bin/python scripts/build_manifest.py
```

Expected: `477 articles indexed, 34 skipped` and `1560 nodes -> 39 batches across 3 waves`.

- [ ] **Step 2: Dispatch thirteen agents, one per batch**

Each agent gets `model: "sonnet"` set explicitly, per spec section 10 and the global rules. The
brief for batch NN is exactly this, with NN substituted:

> You are attaching Phase 2 of the alchemist corpus, batch NN. Work in
> `~/Documents/Repos/alchemist` and use `.venv/bin/python` for everything.
>
> Read `.staging/phase-2/manifest.yaml` and take the `nodes` list for batch NN. Read
> `data/vault-index.yaml` once; it holds every attachable vault wiki article as slug, title, type
> and topics. Do not read the vault wiki directory listing; the index is the catalogue.
>
> For each node in your batch, in order:
> 1. Read `nodes/<id>.md`.
> 2. Draw up candidate articles by matching the node's title and subject against the index's
>    titles and `topics`.
> 3. Open each candidate at `<vault>/wiki/<slug>.md` and test it against the cover bar: an
>    article attaches only where it treats that node's subject directly enough that a Phase 3
>    writer could draft the page from it, meaning the article is about that thing or gives it a
>    substantive section. A passing mention does not attach. You must open the article; never
>    attach on the strength of the index alone.
> 4. Attach the survivors with
>    `.venv/bin/python scripts/attach_articles.py --node <id> --articles <slug> [<slug> ...]`.
>    Never hand-edit frontmatter. For an uncovered node, run it with `--articles` and no values.
> 5. Never touch `vault_sources`, `status`, or any node outside your batch's list.
>
> Write `.staging/phase-2/ledger-NN.yaml` as a YAML list. Add one entry per document your
> uncovered nodes need, with `id` (a kebab-case slug), `needed_by` (the node ids), `claim` (what
> the document would support), `document` (its full citation), `expected_tier`, `acquisition`
> (one of public-download, regulator, journal, purchased-personal), `status: wanted`, and `url`
> where you have one. **Name the node's own anchor document by default**: read the node's
> `anchor` field and propose that body's document unless it genuinely cannot cover the node, in
> which case say why in your report. Group nodes under shared documents rather than writing one
> entry per node.
>
> Write `.staging/phase-2/report-NN.md` recording, per node, the candidates considered, what you
> attached, and one sentence on each rejection.
>
> Finish by running `.venv/bin/python scripts/check.py` and reporting its output. British
> English, and no em or en dashes.

- [ ] **Step 3: Verify no agent wrote outside its batch**

```bash
.venv/bin/python - <<'PY'
import subprocess, sys, yaml
sys.path.insert(0, ".")
from scripts.alchemist.batches import stray_writes
manifest = yaml.safe_load(open(".staging/phase-2/manifest.yaml"))
flat = {n: {"batches": {n: manifest["batches"][n]["nodes"]}} for n in manifest["batches"]}
changed = [l.split("/")[-1].removesuffix(".md")
           for l in subprocess.run(["git", "diff", "--name-only", "--", "nodes/"],
                                   capture_output=True, text=True).stdout.split()]
owned = {i for n in range(1, 14) for i in manifest["batches"][n]["nodes"]}
stray = sorted(set(changed) - owned)
print(f"{len(changed)} nodes changed, {len(stray)} stray")
if stray:
    print("STRAY:", stray[:20])
PY
```

Expected: up to 520 nodes changed, 0 stray. Any stray write means an agent left its assignment;
revert that file with `git checkout -- nodes/<id>.md` and re-run its batch.

- [ ] **Step 4: Run the checks**

Run: `.venv/bin/python scripts/check.py`

Expected: eleven rules ok. Check 11 is now doing real work: it resolves every slug the thirteen
agents attached. A failure here names a fabricated or renamed slug, and the repair is to re-open
the article and correct the attachment, never to delete the check.

- [ ] **Step 5: Spot-read three report fragments against the corpus**

Pick three of the thirteen reports and, for four nodes in each, open the node and the article it
attached and judge the cover bar yourself. This is the only check on whether the bar was applied
rather than merely quoted, and per `~/.claude/rules/subagent-verification.md` an agent's claim
about a document is not evidence until a direct read confirms it. Record what you found.

- [ ] **Step 6: Commit wave one**

```bash
git add nodes/
git commit -m "feat(attach): attach wave one, batches 1 to 13

520 nodes searched against the vault index, each candidate opened and
tested against the cover bar before attaching. Check 11 resolves every
attached slug. Ledger fragments staged for the merge.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

Note that `git add nodes/` is the whole directory here deliberately, since the wave touches up to
520 files in it and nothing else in the tree. Confirm with `git status --short` first that nothing
outside `nodes/` is staged.

---

### Task 9: Run waves two and three, batches 14 to 39

**Files:**
- Modify: `nodes/*.md` for batches 14 to 39 (1,040 nodes)
- Create: `.staging/phase-2/ledger-14.yaml` to `ledger-39.yaml` and the matching reports

**Interfaces:** identical to task 8.

- [ ] **Step 1: Feed wave one's spot-read findings into the brief**

Where the spot-read in task 8 step 5 found the bar applied too loosely or too tightly, add one
sentence to the brief naming the pattern and the correction. Do not rewrite the brief wholesale;
the cover-bar wording is the spec's and stays verbatim.

- [ ] **Step 2: Dispatch wave two, thirteen agents over batches 14 to 26**

Use task 8's brief with NN substituted, `model: "sonnet"` set explicitly.

- [ ] **Step 3: Verify, check, and commit wave two**

Repeat task 8 steps 3, 4 and 6 with the owned set built from batches 14 to 26. Commit message:
`feat(attach): attach wave two, batches 14 to 26`.

- [ ] **Step 4: Dispatch wave three, thirteen agents over batches 27 to 39**

Same brief, same model.

- [ ] **Step 5: Verify, check, and commit wave three**

Repeat with the owned set from batches 27 to 39. Commit message:
`feat(attach): attach wave three, batches 27 to 39`.

- [ ] **Step 6: Confirm the whole corpus was covered exactly once**

```bash
.venv/bin/python - <<'PY'
import sys, yaml
sys.path.insert(0, ".")
from scripts.alchemist.model import load_corpus
manifest = yaml.safe_load(open(".staging/phase-2/manifest.yaml"))
assigned = [i for b in manifest["batches"].values() for i in b["nodes"]]
corpus = load_corpus()
print(f"assigned {len(assigned)}, unique {len(set(assigned))}, corpus {len(corpus.nodes)}")
assert len(assigned) == len(set(assigned)) == len(corpus.nodes)
attached = sum(1 for n in corpus.nodes.values() if n.vault_articles)
print(f"{attached} nodes attached, {len(corpus.nodes) - attached} uncovered")
PY
```

Expected: assigned, unique and corpus all 1,560, and a printed split of attached against
uncovered. Given the vault's shape the uncovered figure will be large, and the spec says so; that
is the gap ledger's job rather than a defect.

- [ ] **Step 7: Confirm all 39 fragment pairs exist**

Run: `ls .staging/phase-2/ledger-*.yaml | wc -l && ls .staging/phase-2/report-*.md | wc -l`
Expected: 39 and 39. A missing fragment means a batch produced no ledger file, which for a batch
with uncovered nodes is a failure rather than a clean result; re-run that batch.

---

### Task 10: Merge the ledger and generate the gate

**Files:**
- Modify: `sources/wanted.yaml`
- Create: `notes/phase-2-coverage-2026-09.md`

**Interfaces:**
- Consumes: `scripts/merge_ledger.py` (task 6), `scripts/build_coverage_report.py` (task 7).
- Produces: the two artefacts Mario reads as the gate.

- [ ] **Step 1: Dry-run the merge**

Run: `.venv/bin/python scripts/merge_ledger.py --dry-run`

Expected: `would write N entries (4 seeded)`. **N should be at or near 59 and must not exceed it
by much.** The spec's bound rests on agents naming the node's own anchor document, of which the
corpus has 59. Should N come back at, say, 200, the anchor-default rule was not followed: stop,
read a sample of fragments, and re-run the offending batches rather than merging a ledger nobody
can read.

- [ ] **Step 2: Merge**

Run: `.venv/bin/python scripts/merge_ledger.py`
Expected: the entry counts and any field disagreements on stderr. Read every disagreement; each is
a place an agent's reading differed from Phase 1's.

- [ ] **Step 3: Run the checks**

Run: `.venv/bin/python scripts/check.py`

Expected: eleven rules ok. Rule 9 resolves every `needed_by` id in the grown ledger, and rule 6
holds trivially because no node is `reviewed` yet.

- [ ] **Step 4: Generate the coverage report**

```bash
.venv/bin/python scripts/build_vault_index.py
.venv/bin/python scripts/build_coverage_report.py
```

Then read `notes/phase-2-coverage-2026-09.md` end to end yourself before handing it over. A gate
artefact nobody has read is not a gate.

- [ ] **Step 5: Commit the gate**

```bash
git add sources/wanted.yaml notes/phase-2-coverage-2026-09.md
git commit -m "feat(ledger): merge the Phase 2 gap ledger and report coverage

The 39 fragments union into N entries, bounded by the corpus's 59 anchor
documents. The coverage report gives the split by domain and by anchor
document, the attachments-per-node distribution, and the documents with
nothing attached, which is the acquisition list Mario rules on.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

Substitute the real N.

---

### Task 11: Open the pull request and put the gate

**Files:** none.

- [ ] **Step 1: Full verification**

```bash
git status --short
.venv/bin/python scripts/check.py
.venv/bin/python -m pytest -q
ALCHEMIST_VAULT=/nonexistent .venv/bin/python scripts/check.py
```

Expected: clean tree; eleven rules ok; 257 passed; and with no vault, checks 5 and 11 skipping
while the other nine pass, which is what CI will do.

- [ ] **Step 2: Push and open the pull request**

```bash
git push -u origin feat/phase-2-attach
gh pr create --base main --head feat/phase-2-attach \
  --title "feat: attach the corpus to the vault and ledger the gaps" \
  --body-file <body saved to a file first>
```

The body must state the attached and uncovered counts, the ledger's entry count against the
59-document bound, the wave-one spot-read findings, the check 11 CI caveat, and it must point at
`notes/phase-2-coverage-2026-09.md` and `sources/wanted.yaml` as the two artefacts to read. End
with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.

- [ ] **Step 3: Stop**

**Never self-merge.** The gap ledger is Mario's call per section 9 of the parent spec. Hand him
the pull request and the coverage note and wait.

---

## Self-review

**Spec coverage.** Section 4's index is task 2. Section 5's manifest, waves and agent contract are
tasks 5, 8 and 9, and the attach tool in task 4 is what makes the contract's "never hand-edit
frontmatter" enforceable. Section 6's ledger merge is task 6. Section 7's check 11, both its
failure arms and its skip, is task 3. Section 8's two gate artefacts are tasks 7 and 10. Section
9's reproducibility is covered by the manifest's explicit ids and the attach tool's sorted write,
tested in tasks 5 and 4. Section 10's three test suites are tasks 2, 3, 6 and 7. Section 11's
exclusions are respected: nothing writes `vault_sources` or `status`, and no task places a no-path
node. Section 12's three amendments land in task 3 (the ten-to-eleven sweep and `CLAUDE.md`) and
task 5 (section 10's cap sentence and section 9's `guides` instruction). Section 13's ordering,
`.gitignore` first, is task 1. Section 14's G25, G26 and G27 are backlog for Mario rather than
tasks here, and the plan does not smuggle them in.

**Placeholders.** One task is deliberately specified rather than written out in full: task 7's
`coverage.py`, whose four function contracts, sort orders and report sections are named precisely
while the table-rendering code is left to the implementer. Every other code step carries literal
code. No step says "add error handling" or "write tests for the above".

**Type consistency.** `Article` is defined in task 2 and consumed nowhere by field, only through
`read_wiki`. `article_path(vault, slug)` and `PUBLISHABLE_ARTICLE` are defined in task 2 and used
in tasks 3 and 4 under exactly those names. `check_attached_articles(corpus, vault)` matches
`run_all`'s call. `slice_batches`, `wave_of` and `stray_writes` are defined and used in task 5.
`read_fragments` and `union_entries` are defined in task 6 and called by `merge_ledger.py` in the
same task. Test counts run 227, 233, 238, 243, 247, 253, 257, consistent with six, five, five,
four, six and four tests added.

**Two risks worth naming.** Task 4 step 5 is a tripwire rather than a test: if `render` does not
reproduce a committed record byte for byte, 1,560 files are about to be reformatted, and the step
says stop. Task 10 step 1 is the other: the ledger's size is the spec's central claim, and the
dry-run is where a broken anchor-default rule shows up while re-running a batch is still cheap.
