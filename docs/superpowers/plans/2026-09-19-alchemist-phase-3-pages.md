# Alchemist Phase 3 Pages implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace every stub body in the corpus with a tier-1 page written to the locked
template, after settling by measurement which model writes them.

**Architecture:** Three small tools land first, test-driven: a template validator shared by a
write tool and a new check 12, a depth-ordered batch manifest, and a page statistics report. Two
subagents, one on Fable 5.1 and one on Sonnet 5, then write the same ten survival-area pages
into blind staging directories, a grader on Opus scores both arms, Mario reads three pairs
blind, and a rule fixed in advance names the model. Thirty-nine agents on that model then write
the remaining 1,547 pages in three waves of thirteen, each wave verified, gated and merged on
its own pull request.

**Tech Stack:** Python 3.14, pytest, PyYAML. Python is always `.venv/bin/python`, never a
system `python3`. Subagents run through the Agent tool with `model` set explicitly on every
dispatch. `writing-guidelines-grader` produces the grades and reads its rubric from OneDrive.

**Spec:** `docs/superpowers/specs/2026-09-19-alchemist-phase-3-pages-design.md`. Read it before
task 1. Section 3 carries the eight decisions every task below implements, section 4 the
template, section 5 the measurement and its decision rule, and sections 8 to 10 the tool, the
batching and the gate.

## Global constraints

- **Branches.** `feat/phase-3-pages` for tasks 1 to 9, cut from `main` after the pull request
  carrying the spec and this plan has merged. `feat/phase-3-wave-1`, `feat/phase-3-wave-2` and
  `feat/phase-3-wave-3` for tasks 10 and 11, each cut from `main` after the previous pull
  request merged. `docs/phase-3-close-out` for task 12.
- **Python is `.venv/bin/python`.** Never a system `python3`.
- **The vault is a separate private repo** at `ALCHEMIST_VAULT` or `~/Documents/Repos/vault`,
  read through `vault_root()` in `scripts/alchemist/checks.py`. Nothing is written into it.
  Articles inform pages and are never quoted, and `vault_sources` stays empty (spec D3.7).
- **The template is spec section 4, verbatim.** Three sections under `## Definition`,
  `## The expression` and `## Why this node exists`; one display block the norm and two the
  ceiling; "rather than" at most once; the closing sentence names a real unlock.
- **Agents never hand-edit a record** (spec D3.5). Every page lands through
  `scripts/write_page.py`.
- **Agents never set `reviewed`.** `drafted` is the phase's ceiling; `reviewed` is Mario's after
  a gate.
- **The decision rule in spec section 5 is fixed** before the arms run and is applied as written
  once the grades are in.
- **This repo is public.** Assume every commit is published. `.staging/` is gitignored and holds
  every fragment; `notes/` holds what must survive a fresh clone.
- **The pre-commit hook runs `check.py` on every commit** and validates the working tree.
- **Never self-merge, never force-push `main`, never `--no-verify`.**
- **Conventional Commits**, imperative and lowercase, no trailing period, ending with the
  `Co-Authored-By` trailer the executing session's attribution reminder names. The snippets below
  show `Claude Fable 5.1`, which is this planning session's; substitute the executing session's.
  Explicit paths on `git add` except where a task says otherwise.
- **British English throughout, and no em or en dashes as punctuation**, in code comments, node
  bodies, the brief, the notes and commit messages.
- **Write currency with the unit word, never a bare dollar sign.** Every `$` on a page is a
  maths delimiter.
- The suite stands at **321 passed**. Tasks 1 to 5 add tests; the count rises and never falls.
- **Model routing.** Tasks 1 to 6 run on Sonnet. Task 7's two arms run on `fable` and `sonnet`,
  one each. Task 8's graders run on `opus`, a model neither arm uses, so neither arm is graded by
  its own family. Tasks 10 and 11 run on the model `notes/phase-3-model-decision-2026-09.md`
  names.

## File structure

| File | Responsibility |
|---|---|
| `scripts/alchemist/template.py` | Create. The template's rules and nothing else: `validate_body`. Imports nothing from the package, so both the check and the writer can import it. |
| `scripts/alchemist/pages.py` | Create. Writes one page through `render`, refusing a body or a spend the checks would refuse, and computes the gate's page statistics. |
| `scripts/write_page.py` | Create. CLI over `pages.py`; the only way an agent writes a page. |
| `scripts/alchemist/checks.py` | Modify. Adds check 12, registers it in `run_all`, and counts twelve in its docstring. |
| `scripts/alchemist/batches.py` | Modify. Adds `requires_depth`, `depth_key`, `phase_node_ids` and a `key` parameter on the slicer. |
| `scripts/build_manifest.py` | Modify. Adds `--phase` and `--order`. |
| `scripts/build_pages_report.py` | Create. CLI over `page_statistics`, printing the gate note's numbers. |
| `notes/phase-3-pages-brief.md` | Create. The brief every writing agent and both arms read. |
| `notes/phase-3-model-decision-2026-09.md` | Create. The measurement's record and verdict. |
| `notes/phase-3-reports/` | Create. The thirty-nine batch reports, copied out of staging at each wave, and a README. |
| `notes/phase-3-gate-2026-09.md` | Create. The closing gate note. |
| `tests/conftest.py` | Modify. Adds the page fixtures both page test modules share. |
| `tests/test_template.py`, `tests/test_pages.py`, `tests/test_write_page.py`, `tests/test_checks_template.py`, `tests/test_pages_report.py` | Create. |
| `tests/test_batches.py` | Modify. |
| `CLAUDE.md`, `README.md`, `.github/workflows/checks.yml`, `.github/workflows/pages.yml`, `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`, `scripts/anchor_audit.py` | Modify. The eleven-to-twelve sweep, and the parent spec's section 10 verdict. |

`template.py` is split from `pages.py` so that `checks.py` can import the validator while
`pages.py` imports check 1 from `checks.py`, with no import cycle. The logic sits in
`scripts/alchemist/` and each CLI stays a thin argument parser over it, the pattern `check.py`
over `checks.py` and `attach_articles.py` over `vault.py` already set. Tests mirror the module
rather than the CLI, per the relaxation `CLAUDE.md` records, and the CLI gets its own subprocess
tests as `attach_articles.py` has.

---

### Task 1: The template validator

**Files:**
- Create: `scripts/alchemist/template.py`
- Test: `tests/test_template.py`

**Interfaces:**
- Consumes: nothing beyond `re`.
- Produces: `HEADINGS: tuple[str, str, str]`, `DISPLAY: re.Pattern`, `RATHER_THAN: re.Pattern`,
  `MAX_RATHER_THAN: int = 1`, and `validate_body(body: str) -> list[str]`, an empty list
  meaning the body conforms and otherwise one sentence per breach, worded for the author who has
  to fix it. Tasks 2, 3 and 5 import these names.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_template.py`:

```python
from scripts.alchemist.template import HEADINGS, MAX_RATHER_THAN, validate_body


def body(definition="The object, defined in one sentence a reader could quote.",
         expression="$$\nS(t) = P(T \\gt t)\n$$\n\nHere $S$ is the survival function and $T$ the event time.",
         why="A hazard divides by survival, so the hazard rate needs it next."):
    return (f"## Definition\n\n{definition}\n\n## The expression\n\n{expression}\n\n"
            f"## Why this node exists\n\n{why}\n")


def test_the_headings_are_the_spec_s_three_in_order():
    assert HEADINGS == ("## Definition", "## The expression", "## Why this node exists")
    assert MAX_RATHER_THAN == 1


def test_a_conforming_body_has_no_problems():
    assert validate_body(body()) == []


def test_a_missing_section_is_one_problem_naming_the_order():
    missing = body().split("## Why this node exists")[0]
    problems = validate_body(missing)
    assert len(problems) == 1 and "in that order" in problems[0]


def test_sections_out_of_order_fail():
    swapped = (body().replace("## Definition", "## TEMP")
               .replace("## The expression", "## Definition")
               .replace("## TEMP", "## The expression"))
    problems = validate_body(swapped)
    assert len(problems) == 1 and "in that order" in problems[0]


def test_a_fourth_heading_of_any_level_fails():
    problems = validate_body(body() + "\n### A note\n\nMore.\n")
    assert len(problems) == 1 and "no other heading" in problems[0]


def test_text_before_the_first_heading_fails():
    problems = validate_body("A preamble.\n\n" + body())
    assert len(problems) == 1 and "before the first heading" in problems[0]


def test_an_empty_section_fails():
    problems = validate_body(body(why=""))
    assert len(problems) == 1 and "no text beneath" in problems[0]


def test_no_display_block_fails():
    problems = validate_body(body(expression="Inline $S(t) = P(T \\gt t)$ only."))
    assert len(problems) == 1 and "no display block" in problems[0]


def test_two_display_blocks_pass_and_three_fail():
    two = body(expression="$$\na\n$$\n\n$$\nb\n$$\n\nHere $a$ and $b$ are named.")
    assert validate_body(two) == []
    three = body(expression="$$\na\n$$\n\n$$\nb\n$$\n\n$$\nc\n$$\n\nHere $a$, $b$ and $c$.")
    problems = validate_body(three)
    assert len(problems) == 1 and "3 display blocks" in problems[0]


def test_an_em_dash_and_an_en_dash_each_fail_with_the_line_named():
    for dash in ("—", "–"):
        problems = validate_body(body(why=f"A hazard {dash} defined above {dash} divides by survival."))
        assert len(problems) == 2 and all("dash on line 15" in p for p in problems)


def test_a_hyphen_in_a_compound_passes():
    assert validate_body(body(definition="A left-truncated duration, defined.")) == []


def test_a_currency_amount_fails_and_inline_maths_does_not():
    """`$2m` and `$1,500` are currency and fail; `$1$` is the number one in
    maths and passes. Every `$` on the page is a maths delimiter, which is why
    the rule targets the amount pattern and never the bare sign."""
    assert any("currency" in p for p in validate_body(body(definition="An exposure of $2m, defined.")))
    assert any("currency" in p for p in validate_body(body(definition="An exposure of $1,500, defined.")))
    assert any("currency" in p for p in validate_body(body(definition="Some $1.5 billion of exposure.")))
    assert validate_body(body(definition="So $S(0) = 1$ holds, and exactly $1$ unit is at risk.")) == []


def test_rather_than_once_passes_and_twice_fails():
    once = body(why="A hazard is estimated rather than assumed, and the hazard rate needs it next.")
    assert validate_body(once) == []
    twice = body(definition="Defined rather than derived.",
                 why="A hazard is estimated rather than assumed, and the hazard rate needs it next.")
    problems = validate_body(twice)
    assert len(problems) == 1 and "'rather than' appears 2 times" in problems[0]
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_template.py -q`
Expected: every test errors with `ModuleNotFoundError: No module named 'scripts.alchemist.template'`.

- [ ] **Step 3: Write the validator**

Create `scripts/alchemist/template.py`:

```python
"""The tier-1 page template, as rules a machine can apply.

Three sections under fixed headings, one display block as the norm and two as
the ceiling, and a handful of house rules a page cannot carry. The Phase 0 plan
fixed the template at its Task 11 and the Phase 3 design restates it in section
4; this module is the one place the rules are code. Both `write_page.py` and
check 12 call it, so a page the tool accepts is a page the check passes, and a
hand edit that breaks the template fails the next commit.

It imports nothing from the package on purpose. `checks.py` imports it for
check 12 and `pages.py` imports check 1 from `checks.py`, and a validator that
imported either would close that into a cycle.
"""

from __future__ import annotations

import re

HEADINGS = ("## Definition", "## The expression", "## Why this node exists")
HEADING = re.compile(r"^#{1,6} .*$", re.M)
SECTION_BREAK = re.compile(r"^## .*$", re.M)
DISPLAY = re.compile(r"\$\$.+?\$\$", re.S)
DASH = re.compile(r"[–—]")
# An amount, never the bare sign: `$2m`, `$1.5 billion`, `$1,500`. Every `$`
# on a page is a maths delimiter, so `$1$` is the number one and passes. The
# one false positive is inline maths of the form `$2m$`, which the message
# tells the author to respace as `$2\,m$`.
CURRENCY = re.compile(
    r"\$\d[\d,]*(?:\.\d+)?\s?(?:m|bn|k|million|billion|thousand)\b"
    r"|\$\d{1,3}(?:,\d{3})+\b"
)
RATHER_THAN = re.compile(r"\brather than\b", re.I)
MAX_RATHER_THAN = 1  # G20: 200 of the 1,580 original stubs carried the phrase


def validate_body(body: str) -> list[str]:
    """Every breach of the template, one sentence each, worded for the author
    who has to fix it. An empty list means the body conforms."""
    problems: list[str] = []
    found = tuple(h.rstrip() for h in HEADING.findall(body))
    if found != HEADINGS:
        problems.append(
            f"headings are {list(found)!r}; the template wants exactly "
            f"{list(HEADINGS)!r} in that order and no other heading"
        )
    else:
        preamble, *sections = SECTION_BREAK.split(body)
        if preamble.strip():
            problems.append(
                f"text before the first heading: {preamble.strip()[:40]!r}; a "
                f"page opens on '## Definition'"
            )
        for heading, text in zip(HEADINGS, sections):
            if not text.strip():
                problems.append(f"{heading!r} has no text beneath it")
    blocks = len(DISPLAY.findall(body))
    if blocks == 0:
        problems.append(
            "no display block; 'The expression' carries the defining formula "
            "between $$ delimiters"
        )
    elif blocks > 2:
        problems.append(
            f"{blocks} display blocks; one is the norm and two the ceiling, so a "
            f"node wanting a third is a split candidate for the report"
        )
    for match in DASH.finditer(body):
        line = body.count("\n", 0, match.start()) + 1
        problems.append(
            f"em or en dash on line {line}; use a comma, full stop, colon or "
            f"parentheses"
        )
    for match in CURRENCY.finditer(body):
        problems.append(
            f"currency written with a dollar sign at {match.group()!r}; write the "
            f"unit word, since every $ on the page is a maths delimiter"
        )
    count = len(RATHER_THAN.findall(body))
    if count > MAX_RATHER_THAN:
        problems.append(
            f"'rather than' appears {count} times; the cap is {MAX_RATHER_THAN} "
            f"per page (G20)"
        )
    return problems
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_template.py -q`
Expected: `13 passed`.

- [ ] **Step 5: Run the validator over the three exemplars**

```bash
for n in conditional-probability survival-function hazard-rate; do
  .venv/bin/python - <<PY
import re, sys
sys.path.insert(0, ".")
from scripts.alchemist.template import validate_body
from scripts.alchemist.model import parse_node
from pathlib import Path
node = parse_node(Path("nodes/$n.md"))
print("$n", validate_body(node.body) or "conforms")
PY
done
```

Expected: `conforms` three times. The exemplars are the template's definition, so a problem here
is a validator bug and never an exemplar edit; fix the rule and re-run.

- [ ] **Step 6: Commit**

```bash
git add scripts/alchemist/template.py tests/test_template.py
git commit -m "feat(pages): add the tier-1 template validator

Three sections under fixed headings, one display block as the norm and
two as the ceiling, and the house rules a page cannot carry. One module,
so the write tool and check 12 apply the same rules.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 2: The page writer and its CLI

**Files:**
- Create: `scripts/alchemist/pages.py`
- Create: `scripts/write_page.py`
- Modify: `tests/conftest.py` (append the page fixtures)
- Test: `tests/test_pages.py`, `tests/test_write_page.py`

**Interfaces:**
- Consumes: `validate_body`, `DISPLAY`, `HEADINGS`, `RATHER_THAN` from task 1;
  `check_declared_symbols_resolve(corpus, objects) -> Result` from `checks.py`; `render(node)`
  from `staging.py`; `parse_node`, `load_objects`, `Corpus`, `Node`, `Objects`, `Spend` from
  `model.py`.
- Produces: `PageRefused(Exception)`; `parse_spend(text: str) -> Spend`;
  `write_page(node_file: Path, body: str, spends: tuple[Spend, ...], objects: Objects, *,
  force: bool = False) -> Node`; `page_statistics(corpus: Corpus) -> dict`; and the CLI
  `scripts/write_page.py` with `--node ID --body PATH [--spends OBJECT:DOMAIN ...] [--force]`
  and `--check PATH`, exit 0 on success and 2 on refusal. Tasks 5, 7, 8, 10 and 11 call them.

- [ ] **Step 1: Add the shared fixtures to `tests/conftest.py`**

Append to `tests/conftest.py`:

```python


# ---------------------------------------------------------------------------
# Page fixtures. `test_pages.py` and `test_write_page.py` both need a node whose
# domains and status they choose, an objects file with two hazard aliases, and
# one conforming body; they live here for the reason the header states.
# ---------------------------------------------------------------------------

PAGE_OBJECTS = """- id: obj.hazard
  name: Hazard rate
  canonical: 'h(t)'
  definition: The instantaneous rate at which the event occurs, given survival to t.
  aliases:
    - {domain: credit, symbol: 'h(t)', name: default hazard}
    - {domain: stats, symbol: '\\lambda(t)', name: hazard function}
"""

PAGE_NODE = """---
id: {id}
title: {title}
domains: [{domains}]
status: {status}
requires: []
spends: []
anchor: [chosen]
vault_articles: []
vault_sources: []
taught_in: null
---

A stub body awaiting its page.
"""

PAGE_BODY = """## Definition

The hazard rate at a time is the instantaneous rate at which the event occurs,
given that it has not occurred by then.

## The expression

$$
h(t) = \\lim_{\\Delta t \\to 0} \\frac{P(t \\le T \\lt t + \\Delta t \\mid T \\ge t)}{\\Delta t}
$$

Here $h(t)$ is the hazard, $T$ the event time and $\\Delta t$ a short interval.

## Why this node exists

A model of whether cannot say when, and the hazard supplies the timing. The
discrete-time hazard needs it next.
"""


def write_stub(root, node_id, *, domains="credit, stats", status="stub"):
    path = root / "nodes" / f"{node_id}.md"
    path.write_text(PAGE_NODE.format(
        id=node_id, title=node_id.capitalize(), domains=domains, status=status))
    return path


@pytest.fixture
def page_repo(tmp_path):
    (tmp_path / "nodes").mkdir()
    (tmp_path / "notation").mkdir()
    (tmp_path / "notation" / "objects.yaml").write_text(PAGE_OBJECTS)
    return tmp_path
```

The doubled backslashes are Python escapes inside a regular triple-quoted string: the file on
disk carries `\lambda(t)`, `\lim` and the rest with single backslashes, which is what YAML and
KaTeX read.

- [ ] **Step 2: Write the failing tests for the writer**

Create `tests/test_pages.py`:

```python
from pathlib import Path

import pytest

from conftest import PAGE_BODY, write_stub
from scripts.alchemist.model import Corpus, Node, Spend, load_objects, parse_node
from scripts.alchemist.pages import PageRefused, page_statistics, parse_spend, write_page


def test_it_writes_the_body_the_spends_and_drafted(page_repo):
    path = write_stub(page_repo, "hazard")
    write_page(path, PAGE_BODY, (Spend("obj.hazard", "credit"),), load_objects(page_repo))
    node = parse_node(path)
    assert node.status == "drafted"
    assert node.spends == (Spend("obj.hazard", "credit"),)
    assert node.body.strip() == PAGE_BODY.strip()
    assert node.domains == ("credit", "stats") and node.anchor == ("chosen",)  # untouched


def test_a_rerun_is_byte_identical_whatever_the_spend_order(page_repo):
    path = write_stub(page_repo, "hazard")
    spends = (Spend("obj.hazard", "stats"), Spend("obj.hazard", "credit"))
    write_page(path, PAGE_BODY, spends, load_objects(page_repo))
    first = path.read_bytes()
    write_page(path, PAGE_BODY, tuple(reversed(spends)), load_objects(page_repo))
    assert path.read_bytes() == first


def test_spends_are_sorted_and_deduplicated(page_repo):
    path = write_stub(page_repo, "hazard")
    spends = (Spend("obj.hazard", "stats"), Spend("obj.hazard", "credit"), Spend("obj.hazard", "stats"))
    written = write_page(path, PAGE_BODY, spends, load_objects(page_repo))
    assert written.spends == (Spend("obj.hazard", "credit"), Spend("obj.hazard", "stats"))


def test_a_body_breaking_the_template_is_refused_and_the_file_untouched(page_repo):
    path = write_stub(page_repo, "hazard")
    before = path.read_bytes()
    with pytest.raises(PageRefused, match="in that order"):
        write_page(path, PAGE_BODY.replace("## Why this node exists", "## Why"), (), load_objects(page_repo))
    assert path.read_bytes() == before


def test_a_spend_check_1_would_refuse_is_refused_here(page_repo):
    """The three arms of check 1, so the pre-commit hook never sees what the
    tool could have caught with the author present."""
    path = write_stub(page_repo, "hazard", domains="credit")
    objects = load_objects(page_repo)
    with pytest.raises(PageRefused, match="unknown object"):
        write_page(path, PAGE_BODY, (Spend("obj.ghost", "credit"),), objects)
    with pytest.raises(PageRefused, match="not among its own domains"):
        write_page(path, PAGE_BODY, (Spend("obj.hazard", "stats"),), objects)
    life = write_stub(page_repo, "life", domains="life")
    with pytest.raises(PageRefused, match="no alias for domain"):
        write_page(life, PAGE_BODY, (Spend("obj.hazard", "life"),), objects)
    assert parse_node(path).status == "stub" and parse_node(life).status == "stub"


def test_a_reviewed_page_is_refused_without_force_and_downgraded_with_it(page_repo):
    path = write_stub(page_repo, "hazard", status="reviewed")
    with pytest.raises(PageRefused, match="reviewed"):
        write_page(path, PAGE_BODY, (), load_objects(page_repo))
    assert write_page(path, PAGE_BODY, (), load_objects(page_repo), force=True).status == "drafted"


def test_parse_spend_reads_the_colon_form_and_refuses_anything_else():
    assert parse_spend("obj.hazard:credit") == Spend("obj.hazard", "credit")
    for bad in ("obj.hazard", "obj.hazard:", ":credit"):
        with pytest.raises(ValueError, match="object:domain"):
            parse_spend(bad)


def node(node_id, *, status="drafted", requires=(), domains=("stats",), body="", title=None):
    return Node(
        id=node_id, title=title or node_id.replace("-", " ").capitalize(), domains=domains,
        status=status, requires=tuple(requires), spends=(), anchor=(), vault_articles=(),
        vault_sources=(), taught_in=None, body=body, path=Path(f"nodes/{node_id}.md"),
    )


def test_statistics_count_status_domain_blocks_words_and_the_capped_phrase():
    corpus = Corpus({
        "a": node("a", status="stub", body="A stub."),
        "b": node("b", domains=("life", "stats"), body=PAGE_BODY),
        "c": node("c", body=PAGE_BODY + "\n$$\nx\n$$\n", requires=["b"]),
    }, {})
    stats = page_statistics(corpus)
    assert stats["by_status"] == {"stub": 1, "drafted": 2}
    assert stats["written_by_domain"] == {"life": 1, "stats": 2}
    assert stats["display_blocks"] == {1: 1, 2: 1}
    assert stats["words"]["min"] <= stats["words"]["median"] <= stats["words"]["max"]
    assert stats["rather_than"] == 0


def test_a_written_page_naming_none_of_its_unlocks_is_listed():
    """`hazard-rate` unlocks `cox-model` and its closing section never names
    that title, so it is listed; `cox-model` unlocks nothing and is exempt. The
    match is title or id in the closing section, lowercased, which is
    approximate and says so."""
    def corpus(hazard_body):
        return Corpus({
            "hazard-rate": node("hazard-rate", body=hazard_body, title="Hazard rate"),
            "cox-model": node("cox-model", body=PAGE_BODY, requires=["hazard-rate"], title="Cox model"),
        }, {})
    assert page_statistics(corpus(PAGE_BODY))["no_forward_reference"] == ["hazard-rate"]
    named = PAGE_BODY.replace("discrete-time hazard needs it next", "Cox model needs it next")
    assert page_statistics(corpus(named))["no_forward_reference"] == []
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_pages.py -q`
Expected: every test errors with `ModuleNotFoundError: No module named 'scripts.alchemist.pages'`.

- [ ] **Step 4: Write the writer and the statistics**

Create `scripts/alchemist/pages.py`:

```python
"""Writing one tier-1 page, and the numbers the gate reads over all of them.

Thirty-nine Phase 3 agents write pages, and hand-edited frontmatter would give
thirty-nine styles and the occasional record `parse_node` rejects. `write_page`
re-renders the whole record through the same `render` the attach tool and the
staging merge use, so every write is identical in shape, and it refuses a body
the template rejects or a spend check 1 would reject, so the refusal happens
here with the author present rather than at the pre-commit hook after the agent
has moved on.

Check 1 is called on a one-node corpus rather than re-implemented, for the
reason `attach_articles.py` gives about `attachment_complaint`: a second copy of
a rule drifts from the first.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import replace
from pathlib import Path

from .checks import check_declared_symbols_resolve
from .model import Corpus, Node, Objects, Spend, parse_node
from .staging import render
from .template import DISPLAY, HEADINGS, RATHER_THAN, validate_body


class PageRefused(Exception):
    """The body or the spends would fail a check; the message names each reason."""


def parse_spend(text: str) -> Spend:
    """`obj.hazard:credit` -> Spend. The colon keeps a spend one shell word."""
    obj, sep, domain = text.partition(":")
    if not sep or not obj or not domain:
        raise ValueError(f"spend {text!r} is not of the form object:domain")
    return Spend(obj, domain)


def write_page(
    node_file: Path,
    body: str,
    spends: tuple[Spend, ...],
    objects: Objects,
    *,
    force: bool = False,
) -> Node:
    """Replace the body, declare the spends, set `drafted`, and re-render.

    Spends are sorted and deduplicated so a rerun with the same inputs is
    byte-identical. A `reviewed` node is refused without `force`, because
    `reviewed` is Mario's verdict after a gate and a rerun batch must not undo
    it silently; with `force` the page goes back to `drafted`, since a rewritten
    page needs reviewing again.
    """
    node = parse_node(node_file)
    if node.status == "reviewed" and not force:
        raise PageRefused(
            f"{node.id} is reviewed; pass --force to overwrite a reviewed page"
        )
    ordered = tuple(sorted(set(spends), key=lambda s: (s.object, s.domain)))
    updated = replace(node, status="drafted", spends=ordered, body=body.strip() + "\n")
    problems = validate_body(updated.body)
    one_node = Corpus({node.id: updated}, {})
    prefix = f"{node.id}: "
    problems += [
        failure.removeprefix(prefix)
        for failure in check_declared_symbols_resolve(one_node, objects).failures
    ]
    if problems:
        raise PageRefused("\n".join(problems))
    node_file.write_text(render(updated))
    return updated


def page_statistics(corpus: Corpus) -> dict:
    """The numbers a gate note reads over the written pages.

    Word counts split on whitespace and so count TeX tokens as words, which is
    the same measure across pages and is all a distribution needs. The
    forward-reference test looks for an unlock's title or id, lowercased, in the
    closing section, and it is approximate: a page naming its unlock by an
    inflection is listed, and the gate reads the list as candidates for a look
    rather than as failures.
    """
    written = [n for n in corpus.nodes.values() if n.status != "stub"]
    words = sorted(len(n.body.split()) for n in written)

    def quantile(p: float) -> int:
        return words[min(len(words) - 1, int(p * len(words)))] if words else 0

    unlocks: dict[str, list[Node]] = defaultdict(list)
    for n in corpus.nodes.values():
        for r in n.requires:
            unlocks[r].append(n)
    missing = []
    for n in written:
        if not unlocks[n.id]:
            continue
        closing = n.body.split(HEADINGS[2], 1)[-1].lower()
        if not any(u.title.lower() in closing or u.id in closing for u in unlocks[n.id]):
            missing.append(n.id)

    return {
        "by_status": dict(Counter(n.status for n in corpus.nodes.values())),
        "written_by_domain": dict(Counter(d for n in written for d in n.domains)),
        "display_blocks": dict(Counter(len(DISPLAY.findall(n.body)) for n in written)),
        "words": {
            "min": quantile(0), "q1": quantile(0.25), "median": quantile(0.5),
            "q3": quantile(0.75), "max": words[-1] if words else 0,
        },
        "rather_than": sum(len(RATHER_THAN.findall(n.body)) for n in written),
        "no_forward_reference": sorted(missing),
    }
```

- [ ] **Step 5: Run the writer tests to verify they pass**

Run: `.venv/bin/python -m pytest tests/test_pages.py -q`
Expected: `9 passed`.

- [ ] **Step 6: Write the failing CLI tests**

Create `tests/test_write_page.py`:

```python
import subprocess
import sys
from pathlib import Path

from conftest import PAGE_BODY, write_stub
from scripts.alchemist.model import Spend, parse_node

REPO = Path(__file__).resolve().parents[1]


def run(root, *args):
    return subprocess.run(
        [sys.executable, "scripts/write_page.py", "--root", str(root), *args],
        capture_output=True, text=True, cwd=REPO,
    )


def body_file(tmp_path, text=PAGE_BODY):
    path = tmp_path / "body.md"
    path.write_text(text)
    return str(path)


def test_it_writes_a_page_and_reports_the_spends(page_repo, tmp_path):
    write_stub(page_repo, "hazard")
    result = run(page_repo, "--node", "hazard", "--body", body_file(tmp_path),
                 "--spends", "obj.hazard:credit")
    assert result.returncode == 0, result.stderr
    assert "hazard: drafted, 1 spends declared" in result.stdout
    node = parse_node(page_repo / "nodes" / "hazard.md")
    assert node.status == "drafted" and node.spends == (Spend("obj.hazard", "credit"),)


def test_check_alone_writes_nothing_and_exits_2_on_a_breach(page_repo, tmp_path):
    broken = body_file(tmp_path, PAGE_BODY.replace("## The expression", "## Formula"))
    result = run(page_repo, "--check", broken)
    assert result.returncode == 2 and "in that order" in result.stderr
    result = run(page_repo, "--check", body_file(tmp_path))
    assert result.returncode == 0 and "conforms" in result.stdout
    assert not list((page_repo / "nodes").iterdir())


def test_a_refused_spend_leaves_the_node_a_stub(page_repo, tmp_path):
    write_stub(page_repo, "hazard")
    result = run(page_repo, "--node", "hazard", "--body", body_file(tmp_path),
                 "--spends", "obj.ghost:credit")
    assert result.returncode == 2 and "unknown object" in result.stderr
    assert parse_node(page_repo / "nodes" / "hazard.md").status == "stub"


def test_a_malformed_spend_is_refused(page_repo, tmp_path):
    write_stub(page_repo, "hazard")
    result = run(page_repo, "--node", "hazard", "--body", body_file(tmp_path),
                 "--spends", "obj.hazard")
    assert result.returncode == 2 and "object:domain" in result.stderr


def test_a_reviewed_node_needs_force(page_repo, tmp_path):
    write_stub(page_repo, "hazard", status="reviewed")
    body = body_file(tmp_path)
    assert run(page_repo, "--node", "hazard", "--body", body).returncode == 2
    assert run(page_repo, "--node", "hazard", "--body", body, "--force").returncode == 0
    assert parse_node(page_repo / "nodes" / "hazard.md").status == "drafted"


def test_an_unknown_node_is_refused(page_repo, tmp_path):
    result = run(page_repo, "--node", "ghost", "--body", body_file(tmp_path))
    assert result.returncode == 2 and "no such node" in result.stderr


def test_omitting_node_or_body_without_check_is_an_error(page_repo):
    result = run(page_repo, "--node", "hazard")
    assert result.returncode == 2 and "--node and --body are required" in result.stderr
```

- [ ] **Step 7: Run the CLI tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_write_page.py -q`
Expected: `7 failed`, each on a missing `scripts/write_page.py` (Python exits 2 with
`can't open file`, so the return-code assertions on refusal tests may pass by accident; the
success test fails, which is enough to show the tool is absent).

- [ ] **Step 8: Write the CLI**

Create `scripts/write_page.py`:

```python
r"""Write one tier-1 page, refusing a body or a spend the checks would refuse.

    .venv/bin/python scripts/write_page.py --node hazard-rate --body /tmp/hazard.md \
        --spends obj.hazard:credit obj.survival:credit

    .venv/bin/python scripts/write_page.py --check /tmp/hazard.md

The first form validates the body against the template and every spend against
check 1, sets `status: drafted`, replaces the body and re-renders the whole
record, so thirty-nine agents produce one shape of file. It touches no other
field, and it refuses to overwrite a `reviewed` node without `--force`, because
`reviewed` is Mario's verdict after a gate and a rerun batch must not undo it.

The second form runs the validator alone on a body file and exits 2 naming each
breach. The model measurement's two arms call it, since they write bodies into
staging rather than into `nodes/`.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.model import load_objects
from scripts.alchemist.pages import PageRefused, parse_spend, write_page
from scripts.alchemist.template import validate_body

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--check", type=Path, help="validate this body file and write nothing")
    parser.add_argument("--node")
    parser.add_argument("--body", type=Path)
    parser.add_argument("--spends", nargs="*", default=[], metavar="OBJECT:DOMAIN")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    if args.check is not None:
        problems = validate_body(args.check.read_text())
        for problem in problems:
            print(f"{args.check}: {problem}", file=sys.stderr)
        if not problems:
            print(f"{args.check}: conforms to the template")
        return 2 if problems else 0

    if args.node is None or args.body is None:
        parser.error("--node and --body are required unless --check is given")
    node_file = args.root / "nodes" / f"{args.node}.md"
    if not node_file.is_file():
        print(f"no such node {args.node!r} at {node_file}", file=sys.stderr)
        return 2
    try:
        spends = tuple(parse_spend(s) for s in args.spends)
        written = write_page(
            node_file, args.body.read_text(), spends, load_objects(args.root), force=args.force
        )
    except (ValueError, PageRefused) as exc:
        for line in str(exc).splitlines():
            print(f"{args.node}: {line}", file=sys.stderr)
        return 2
    print(f"{args.node}: drafted, {len(written.spends)} spends declared")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 9: Run the whole suite**

Run: `.venv/bin/python -m pytest -q`
Expected: `350 passed` (321, plus 13 from task 1, plus 9 and 7 here).

- [ ] **Step 10: Commit**

```bash
git add scripts/alchemist/pages.py scripts/write_page.py tests/conftest.py tests/test_pages.py tests/test_write_page.py
git commit -m "feat(pages): add the write tool that lands a tier-1 page

Validates the body against the template and every spend against check 1,
sets drafted, and re-renders the record through render, so every agent's
write has one shape. Refuses a reviewed node without --force. The
--check form validates a body file alone, for the measurement arms.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 3: Check 12, and the sweep from eleven to twelve

**Files:**
- Modify: `scripts/alchemist/checks.py` (import, the check, `run_all`, and the docstring's first line)
- Test: `tests/test_checks_template.py`
- Modify: `CLAUDE.md`, `README.md`, `.github/workflows/checks.yml`, `.github/workflows/pages.yml`,
  `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`, `scripts/anchor_audit.py`

**Interfaces:**
- Consumes: `validate_body` from task 1; `Result`, `Corpus` already in `checks.py`.
- Produces: `check_template_conformance(corpus: Corpus) -> Result`, registered last in
  `run_all`, so the CLI reports it as rule 12.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_checks_template.py`:

```python
from pathlib import Path

from conftest import PAGE_BODY
from scripts.alchemist.checks import check_template_conformance, run_all
from scripts.alchemist.model import Corpus, Node, load_corpus, load_objects

REPO = Path(__file__).resolve().parents[1]


def node(node_id: str, status: str, body: str) -> Node:
    return Node(
        id=node_id, title=node_id, domains=("stats",), status=status, requires=(), spends=(),
        anchor=(), vault_articles=(), vault_sources=(), taught_in=None, body=body,
        path=Path(f"nodes/{node_id}.md"),
    )


def failures(*nodes: Node) -> list[str]:
    return check_template_conformance(Corpus({n.id: n for n in nodes}, {})).failures


def test_a_stub_is_exempt_whatever_its_body():
    assert failures(node("a", "stub", "One sentence of scope, no headings.")) == []


def test_a_conforming_drafted_page_passes():
    assert failures(node("a", "drafted", PAGE_BODY)) == []


def test_a_drafted_page_missing_a_heading_fails_and_names_the_node():
    result = failures(node("a", "drafted", PAGE_BODY.replace("## Why this node exists", "## Why")))
    assert len(result) == 1 and result[0].startswith("a: ") and "in that order" in result[0]


def test_a_reviewed_page_is_checked_too():
    result = failures(node("a", "reviewed", PAGE_BODY + "\n$$\nx\n$$\n\n$$\ny\n$$\n"))
    assert len(result) == 1 and result[0].startswith("a: 3 display blocks")


def test_run_all_reports_twelve_rules_with_the_template_last():
    """The rule number is the CLI's contract with every document that counts
    the checks, so pin it here rather than in prose alone."""
    results = run_all(load_corpus(REPO), load_objects(REPO), REPO, Path("/nonexistent"))
    assert len(results) == 12
    assert results[-1].rule == "12. written pages follow the template"
    assert results[-1].ok
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_checks_template.py -q`
Expected: `ImportError: cannot import name 'check_template_conformance'`.

- [ ] **Step 3: Add the check**

In `scripts/alchemist/checks.py`, add to the imports beneath `from .site import render_symbols`:

```python
from .template import validate_body
```

Change the docstring's first line from `"""The eleven rules. Each returns a Result, so the runner reports every failure in`
to `"""The twelve rules. Each returns a Result, so the runner reports every failure in`.

Add after `check_attached_articles`:

```python
def check_template_conformance(corpus: Corpus) -> Result:
    """A written page carries exactly the template.

    The parent spec's gate row says the checker owns structure and Mario reads
    for voice, and this is the rule that makes the first half true: three
    sections under fixed headings, one display block as the norm and two as
    the ceiling, and the house rules `template.py` states. `write_page.py`
    calls the same validator, so a page the tool accepted passes here, and a
    hand edit that breaks the template fails the next commit instead of
    publishing quietly. Stubs are exempt: their bodies are the transcribers'
    scope statements, awaiting replacement.
    """
    result = Result("12. written pages follow the template")
    for node in sorted(corpus.nodes.values(), key=lambda n: n.id):
        if node.status == "stub":
            continue
        for problem in validate_body(node.body):
            result.failures.append(f"{node.id}: {problem}")
    return result
```

In `run_all`, add `check_template_conformance(corpus),` as the last entry of the list, after
`check_attached_articles(corpus, vault),`.

- [ ] **Step 4: Run the tests and the checks**

Run: `.venv/bin/python -m pytest tests/test_checks_template.py -q`
Expected: `5 passed`.

Run: `.venv/bin/python scripts/check.py`
Expected: twelve `ok` lines, the last `ok    12. written pages follow the template`, and
`1560 nodes, 13 paths, 0 failures`. The three exemplars are the only non-stub nodes and task 1
step 5 showed they conform.

- [ ] **Step 5: Sweep every document that counts eleven**

Each edit below names the exact text. Nothing else in these files changes.

`scripts/alchemist/checks.py`: done in step 3.

`CLAUDE.md`:
- `## The eleven checks` becomes `## The twelve checks`.
- `enforces eleven rules over the whole corpus` becomes `enforces twelve rules over the whole corpus`.
- After the sentence ending `wiki file and is public-free or public-paid.` insert:
  ` Rule 12, added for Phase 3, is that every written page, meaning every node whose status is
  not `stub`, follows the three-section template; `scripts/write_page.py` runs the same
  validator at write time, so the rule catches a hand edit rather than an agent's write.`
- `so a clone with no vault still gets nine of the eleven` becomes `so a clone with no vault still gets ten of the twelve`.
- In Build commands, `# the eleven checks` becomes `# the twelve checks`, and beneath the
  `check.py` line add:
  ```
  .venv/bin/python scripts/write_page.py --node <id> --body <file> --spends obj:domain   # the only way a page is written
  ```
- `` `checks.py` for the eleven rules `` becomes `` `checks.py` for the twelve rules ``.

`README.md`:
- `enforces eleven rules over the corpus` becomes `enforces twelve rules over the corpus`.
- `that every title is sentence case, and\nthat every attached vault article resolves to a real wiki file and is public-free or\npublic-paid.` becomes `that every title is sentence case, that every attached vault article resolves to a real wiki file and is public-free or public-paid, and that every written page follows the three-section template.` (rewrap to the paragraph's width).
- `Two of the eleven` becomes `Two of the twelve`.
- `nine of the eleven checks` becomes `ten of the twelve checks`.
- `so the other nine still gate` becomes `so the other ten still gate`.

`.github/workflows/checks.yml`:
- Line 1: `# Runs the eleven checks, the build and the test suite against every pull` becomes `# Runs the twelve checks, ...`.
- `# Nine of the eleven on this runner. Checks 5 and 11 read the vault, a` becomes `# Ten of the twelve on this runner. Checks 5 and 11 read the vault, a`.
- `- name: Run the eleven checks` becomes `- name: Run the twelve checks`.

`.github/workflows/pages.yml`: `- name: Run the eleven checks` becomes `- name: Run the twelve checks`.

`docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`:
- `enforces eleven rules and blocks a commit` becomes `enforces twelve rules and blocks a commit`.
- After the paragraph beginning `Rules 8 and 9 were added in the Phase 0 fix wave` add:
  ```
  Rules 10, 11 and 12 arrived with gate 2, Phase 2 and Phase 3 respectively: every title is
  sentence case, every attached vault article resolves to a real wiki file and is public-free or
  public-paid, and every written page follows the three-section template. `CLAUDE.md` states
  each in full, and section 8 of `2026-09-19-alchemist-phase-3-pages-design.md` argues for the
  twelfth.
  ```
- `this public repo still runs nine of the eleven` becomes `this public repo still runs ten of the twelve`.
- `# the eleven checks above` becomes `# the twelve checks above`.

`scripts/anchor_audit.py`, in the module docstring:
- `No check can do this job. Rule 12 was considered and rejected on 17 September` becomes
  `No check can do this job. An anchor rule, which would then have been rule 12, was considered and rejected on 17 September`.
- `false-positive cost and the corpus keeps its eleven checks.` becomes
  `false-positive cost, and no anchor rule joined the checks. The rule 12 that now exists is Phase 3's template rule, which has nothing to do with anchors.`
Rewrap the docstring to its existing width.

- [ ] **Step 6: Verify nothing still says eleven**

```bash
grep -rn -i "eleven" --include='*.py' --include='*.md' --include='*.yml' . \
  | grep -v "\.venv/\|notes/\|docs/superpowers/plans/\|docs/superpowers/specs/2026-09-09\|docs/superpowers/rulings\|sources/"
```

Expected: no output. (`notes/`, the earlier plans, the Phase 2 spec and the rulings file are
history and keep their counts; `sources/wanted.yaml` says "eleven nodes" about something else.)

Run: `.venv/bin/python -m pytest -q`
Expected: `355 passed`.

- [ ] **Step 7: Commit**

```bash
git add scripts/alchemist/checks.py tests/test_checks_template.py CLAUDE.md README.md .github/workflows/checks.yml .github/workflows/pages.yml docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md scripts/anchor_audit.py
git commit -m "feat(checks): add rule 12, written pages follow the template

Every non-stub node's body passes the validator write_page.py applies, so
a hand edit that breaks the template fails the next commit. Counts move
from eleven to twelve in CLAUDE.md, the README, both workflows, the
parent spec and the anchor audit's docstring.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 4: Depth-ordered batches for Phase 3

**Files:**
- Modify: `scripts/alchemist/batches.py`
- Modify: `scripts/build_manifest.py`
- Test: `tests/test_batches.py` (append)

**Interfaces:**
- Consumes: `Node` from `model.py`.
- Produces: `requires_depth(nodes: dict[str, Node]) -> dict[str, int]`;
  `depth_key(nodes: dict[str, Node]) -> Callable[[str], tuple[int, str]]`;
  `phase_node_ids(nodes: dict[str, Node], phase: int) -> list[str]`; `slice_batches(node_ids,
  size=BATCH_SIZE, key=None)` and `manifest_payload(node_ids, size=BATCH_SIZE,
  per_wave=PER_WAVE, key=None)` gain the `key` parameter; and the CLI
  `build_manifest.py --phase {2,3} --order {id,depth}` writing
  `.staging/phase-<n>/manifest.yaml`. Tasks 10 and 11 run it.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_batches.py`, and extend its import line to
`from scripts.alchemist.batches import depth_key, manifest_payload, phase_node_ids, requires_depth, slice_batches, stray_writes, wave_of`
plus `from pathlib import Path` and `from scripts.alchemist.model import Node`:

```python


def node(node_id, requires=(), status="stub"):
    return Node(
        id=node_id, title=node_id, domains=("stats",), status=status, requires=tuple(requires),
        spends=(), anchor=(), vault_articles=(), vault_sources=(), taught_in=None, body="",
        path=Path(f"nodes/{node_id}.md"),
    )


def test_requires_depth_is_the_longest_chain_beneath_a_node():
    nodes = {"a": node("a"), "b": node("b", ["a"]), "c": node("c", ["a", "b"]), "d": node("d")}
    assert requires_depth(nodes) == {"a": 0, "b": 1, "c": 2, "d": 0}


def test_the_depth_key_orders_by_depth_then_id():
    """Roots first, alphabetical within a depth, so a prerequisite lands in an
    earlier wave than its dependents more often than the alphabetical order
    Phase 2 used: 456 against 232 of the 1,107 non-root nodes, measured on
    19 September 2026."""
    nodes = {"z": node("z"), "a": node("a", ["z"]), "m": node("m"), "b": node("b", ["a"])}
    assert slice_batches(list(nodes), key=depth_key(nodes)) == [["m", "z", "a", "b"]]


def test_slice_batches_still_sorts_alphabetically_without_a_key():
    assert slice_batches(["b", "a"], size=1) == [["a"], ["b"]]


def test_manifest_payload_passes_the_key_through():
    nodes = {"z": node("z"), "a": node("a", ["z"])}
    payload = manifest_payload(list(nodes), size=1, key=depth_key(nodes))
    assert payload["batches"][1]["nodes"] == ["z"]
    assert payload["batches"][2]["nodes"] == ["a"]


def test_phase_3_batches_only_the_stubs_and_phase_2_batches_everything():
    nodes = {"a": node("a"), "b": node("b", status="drafted"), "c": node("c", status="reviewed")}
    assert phase_node_ids(nodes, 3) == ["a"]
    assert phase_node_ids(nodes, 2) == ["a", "b", "c"]
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `.venv/bin/python -m pytest tests/test_batches.py -q`
Expected: `ImportError: cannot import name 'depth_key'`.

- [ ] **Step 3: Extend `batches.py`**

Add beneath `from __future__ import annotations`:

```python
from collections.abc import Callable

from .model import Node
```

Replace `slice_batches` and `manifest_payload` with:

```python
def slice_batches(
    node_ids: list[str], size: int = BATCH_SIZE, key: Callable[[str], object] | None = None
) -> list[list[str]]:
    ordered = sorted(node_ids, key=key)
    return [ordered[i:i + size] for i in range(0, len(ordered), size)]
```

and

```python
def manifest_payload(
    node_ids: list[str],
    size: int = BATCH_SIZE,
    per_wave: int = PER_WAVE,
    key: Callable[[str], object] | None = None,
) -> dict:
    """The batches section of the manifest: number, wave and explicit ids.

    `build_manifest.py` and `stray_writes` both need to agree on this shape, so
    it lives here once rather than as two copies that could drift apart, one
    writing the manifest and the other reading it back.
    """
    batches = slice_batches(node_ids, size, key)
    return {
        "nodes": len(node_ids),
        "batches": {
            number: {"wave": wave_of(number, per_wave), "nodes": ids}
            for number, ids in enumerate(batches, start=1)
        },
    }
```

Add after `wave_of`:

```python
def requires_depth(nodes: dict[str, Node]) -> dict[str, int]:
    """Longest prerequisite chain beneath each node, a root being 0. Check 3
    keeps the graph acyclic, so the recursion terminates; the deepest node in
    the corpus sits at 12."""
    depth: dict[str, int] = {}

    def visit(node_id: str) -> int:
        if node_id not in depth:
            requires = nodes[node_id].requires
            depth[node_id] = 0 if not requires else 1 + max(visit(r) for r in requires)
        return depth[node_id]

    for node_id in nodes:
        visit(node_id)
    return depth


def depth_key(nodes: dict[str, Node]) -> Callable[[str], tuple[int, str]]:
    """A sort key putting shallower nodes first and ids alphabetical within a
    depth. Phase 3 slices on it so that an agent writing a page's closing
    section reads a drafted prerequisite more often than a stub."""
    depth = requires_depth(nodes)
    return lambda node_id: (depth[node_id], node_id)


def phase_node_ids(nodes: dict[str, Node], phase: int) -> list[str]:
    """Phase 2 batched every node; Phase 3 batches the stubs, since a drafted
    node already carries its page and a rerun must not overwrite it."""
    if phase == 2:
        return list(nodes)
    return [n.id for n in nodes.values() if n.status == "stub"]
```

- [ ] **Step 4: Extend the CLI**

Replace `scripts/build_manifest.py` in full:

```python
"""Write a phase's batch manifest.

    .venv/bin/python scripts/build_manifest.py                      # Phase 2, every node, by id
    .venv/bin/python scripts/build_manifest.py --phase 3 --order depth

Writes `.staging/phase-<n>/manifest.yaml`: one entry per batch, carrying its
wave and its explicit node ids. The directory is gitignored, and the manifest is
rebuilt from the corpus rather than kept. Phase 3 batches only the stubs and
orders them by depth in the `requires` graph, so prerequisites tend to land in
an earlier wave than the pages that cite them.
"""

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import yaml

from scripts.alchemist.batches import depth_key, manifest_payload, phase_node_ids
from scripts.alchemist.model import load_corpus

REPO = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--phase", type=int, choices=(2, 3), default=2)
    parser.add_argument("--order", choices=("id", "depth"), default="id")
    parser.add_argument("--out", type=Path, default=None,
                        help="defaults to .staging/phase-<phase>/manifest.yaml")
    args = parser.parse_args()
    out = args.out or REPO / ".staging" / f"phase-{args.phase}" / "manifest.yaml"

    corpus = load_corpus(args.root)
    ids = phase_node_ids(corpus.nodes, args.phase)
    key = depth_key(corpus.nodes) if args.order == "depth" else None
    payload = {
        "built": date.today().isoformat(),
        "phase": args.phase,
        "order": args.order,
        **manifest_payload(ids, key=key),
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(payload, sort_keys=False))
    waves = max(batch["wave"] for batch in payload["batches"].values())
    print(f"{payload['nodes']} nodes -> {len(payload['batches'])} batches across {waves} waves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 5: Run the tests and a dry manifest**

Run: `.venv/bin/python -m pytest tests/test_batches.py -q`
Expected: `13 passed` (eight existing plus five).

Run: `.venv/bin/python scripts/build_manifest.py --phase 3 --order depth --out /tmp/phase-3-manifest-dry.yaml`
Expected: `1557 nodes -> 39 batches across 3 waves`, since the ten measured pages have not
landed yet. Task 10 rebuilds it and expects 1,547.

Run: `.venv/bin/python -m pytest -q`
Expected: `360 passed`.

- [ ] **Step 6: Commit**

```bash
git add scripts/alchemist/batches.py scripts/build_manifest.py tests/test_batches.py
git commit -m "feat(batches): order Phase 3 batches by prerequisite depth

Sorting stubs by depth in the requires graph before slicing puts every
prerequisite in an earlier wave for 456 of the 1,107 non-root nodes,
against 232 alphabetically. The manifest gains phase and order fields.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 5: The page statistics report

**Files:**
- Create: `scripts/build_pages_report.py`
- Test: `tests/test_pages_report.py`

**Interfaces:**
- Consumes: `page_statistics` from task 2; `load_corpus`.
- Produces: the CLI, printing seven lines of figures the gate notes copy. Tasks 8, 10, 11 and 12
  run it.

- [ ] **Step 1: Write the failing test**

Create `tests/test_pages_report.py`:

```python
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def test_the_report_prints_every_figure_the_gate_reads():
    result = subprocess.run(
        [sys.executable, "scripts/build_pages_report.py"],
        capture_output=True, text=True, cwd=REPO,
    )
    assert result.returncode == 0, result.stderr
    for line in ("Pages by status:", "Written pages by domain:", "Display blocks per written page:",
                 "Words per written page:", "'rather than' across written pages:",
                 "Written pages naming none of their unlocks in the closing section:"):
        assert line in result.stdout
    assert "stub" in result.stdout and "drafted" in result.stdout
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_pages_report.py -q`
Expected: `1 failed` on the return code, since the script does not exist.

- [ ] **Step 3: Write the CLI**

Create `scripts/build_pages_report.py`:

```python
"""Print the numbers a Phase 3 gate note reads.

    .venv/bin/python scripts/build_pages_report.py

Pages per status and per domain, the display-block and word-count distributions
over written pages, the "rather than" total, and the written pages whose closing
section names none of their unlocks. It reports and never gates, following
`grain_audit.py`: these are the figures Mario reads at a wave's gate, beside the
grader's sample and his own spot-read.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.model import load_corpus
from scripts.alchemist.pages import page_statistics

REPO = Path(__file__).resolve().parents[1]


def _counts(counter: dict) -> str:
    return ", ".join(f"{key} {value}" for key, value in sorted(counter.items(), key=lambda kv: str(kv[0])))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=REPO)
    args = parser.parse_args()

    stats = page_statistics(load_corpus(args.root))
    words = stats["words"]
    print(f"Pages by status: {_counts(stats['by_status'])}")
    print(f"Written pages by domain: {_counts(stats['written_by_domain']) or 'none'}")
    print(f"Display blocks per written page: {_counts(stats['display_blocks']) or 'none'}")
    print(f"Words per written page: min {words['min']}, q1 {words['q1']}, "
          f"median {words['median']}, q3 {words['q3']}, max {words['max']}")
    print(f"'rather than' across written pages: {stats['rather_than']}")
    missing = stats["no_forward_reference"]
    print(f"Written pages naming none of their unlocks in the closing section: {len(missing)}")
    for node_id in missing:
        print(f"  {node_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run it and the suite**

Run: `.venv/bin/python scripts/build_pages_report.py`
Expected, measured on 19 September 2026 against the three exemplars:

```
Pages by status: drafted 3, stub 1557
Written pages by domain: credit 2, gi 1, life 2, maths 1, stats 3
Display blocks per written page: 1 3
Words per written page: min 192, q1 192, median 213, q3 273, max 273
'rather than' across written pages: 1
Written pages naming none of their unlocks in the closing section: 1
  hazard-rate
```

The last line is a real finding and the report's first. `hazard-rate` closes on "that
discrete-time hazard needs it next", and no node of that title exists: its six unlocks are the
Gompertz law, the Nelson-Aalen estimator, the proportional hazards model, the multiple-state
Markov model, dependent probabilities from forces of transition, and the survival, density and
hazard relationships. The exemplar therefore breaks the forward-reference rule the template
states, which is exactly what the report exists to surface. It is logged as G33 in the Phase 3
design and left for the exemplar's next touch; do not fix it in this task.

Run: `.venv/bin/python -m pytest -q`
Expected: `361 passed`.

- [ ] **Step 5: Commit**

```bash
git add scripts/build_pages_report.py tests/test_pages_report.py
git commit -m "feat(pages): report the figures a wave's gate reads

Status and domain counts, display-block and word-count distributions,
the capped phrase's total, and written pages whose closing section names
no unlock. Reports and never gates, like grain_audit.py.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 6: The brief

**Files:**
- Create: `notes/phase-3-pages-brief.md`

**Interfaces:**
- Consumes: the tool from task 2 and the template from task 1, by name.
- Produces: the file both measurement arms (task 7) and every wave agent (tasks 10 and 11) read
  first. It is tracked because Phase 2's wave 1 brief lived only in a session and had to be
  reconstructed.

- [ ] **Step 1: Write the brief**

Create `notes/phase-3-pages-brief.md` with exactly this content:

````markdown
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
````

- [ ] **Step 2: Check the brief against the tool it describes**

```bash
.venv/bin/python scripts/write_page.py --help | head -20
grep -c "rather than" notes/phase-3-pages-brief.md
```

Expected: the help text shows `--node`, `--body`, `--spends`, `--force`, `--check`, matching the
brief; and the phrase count is 4, since the brief names the phrase it caps, which is fine in a
brief and would fail on a page.

- [ ] **Step 3: Commit**

```bash
git add notes/phase-3-pages-brief.md
git commit -m "docs(notes): write the Phase 3 pages brief

The brief every writing agent and both measurement arms read first,
tracked so it survives a fresh clone.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 7: Run the two measurement arms

**Files:**
- Create (gitignored): `.staging/phase-3/measurement/arms.yaml`,
  `.staging/phase-3/measurement/arm-a/<id>.md` and `arm-b/<id>.md`, ten each,
  `.staging/phase-3/measurement/report-arm-a.md` and `report-arm-b.md`,
  `.staging/phase-3/measurement/usage.yaml`

**Interfaces:**
- Consumes: `scripts/write_page.py --check` (task 2), the brief (task 6).
- Produces: twenty body files and two reports for task 8 to grade, and the sealed arm mapping.

- [ ] **Step 1: Confirm the preconditions**

```bash
ls ~/Documents/Repos/vault/wiki >/dev/null && echo vault ok
ls "$HOME/Library/CloudStorage/OneDrive-Gini/Gini - Documents/01 Guidelines/_rubrics/writing-guidelines-global.md" && echo rubric ok
git status --short
```

Expected: `vault ok`, the rubric path, and a clean tree. The rubric is what task 8's grader reads,
so it is confirmed before the arms spend anything.

- [ ] **Step 2: Seal the arm mapping**

```bash
.venv/bin/python - <<'PY'
import random, yaml
from pathlib import Path
a = random.choice(["fable", "sonnet"])
b = "sonnet" if a == "fable" else "fable"
root = Path(".staging/phase-3/measurement")
for arm in ("arm-a", "arm-b"):
    (root / arm).mkdir(parents=True, exist_ok=True)
(root / "arms.yaml").write_text(yaml.safe_dump({
    "arm-a": a, "arm-b": b, "sealed": "2026-09-19",
    "unseal": "only after the grades and the blind read are recorded in the decision note",
}))
print("sealed; do not print the mapping")
PY
```

The executor reads `arms.yaml` once, to set `model` on each dispatch, and does not repeat the
mapping in any message, report or note until task 8 step 6. The grader and Mario see arm letters
only.

- [ ] **Step 3: Dispatch both arms in one message**

Two Agent calls in the same message, so they run concurrently. Read `arms.yaml`, and for
`arm-a` set `model` to its value, for `arm-b` to the other. The prompt is identical to the byte
except the arm letter:

> You are writing the Phase 3 model measurement for the alchemist corpus, arm `<x>`. Work in
> `~/Documents/Repos/alchemist` and use `.venv/bin/python` for everything.
>
> Read `notes/phase-3-pages-brief.md` first and follow it exactly, with two differences. Write
> each body to `.staging/phase-3/measurement/arm-<x>/<id>.md` instead of landing it with
> `write_page.py`, and validate each with
> `.venv/bin/python scripts/write_page.py --check .staging/phase-3/measurement/arm-<x>/<id>.md`,
> fixing whatever it refuses until it prints `conforms to the template`. Write your report to
> `.staging/phase-3/measurement/report-arm-<x>.md`, naming per node the `--spends` pairs the page
> would declare, in the form `obj.hazard:credit`.
>
> Your ten nodes, in this order: `future-lifetime-random-variable`, `life-table`,
> `lifetime-distribution-function`, `survival-hazard-relationships`, `censoring`,
> `empirical-survival-function`, `kaplan-meier-estimator`, `nelson-aalen-estimator`,
> `proportional-hazards-model`, `survival-model-credit-risk`.
>
> Do not modify anything under `nodes/`, `notation/` or `sources/`. Finish by listing the ten
> files you wrote and the check result for each.

- [ ] **Step 4: Verify the arms**

```bash
for arm in arm-a arm-b; do
  echo "== $arm: $(ls .staging/phase-3/measurement/$arm/*.md | wc -l) files"
  for f in .staging/phase-3/measurement/$arm/*.md; do
    .venv/bin/python scripts/write_page.py --check "$f" >/dev/null 2>&1 || echo "FAILS: $f"
  done
done
ls .staging/phase-3/measurement/report-arm-a.md .staging/phase-3/measurement/report-arm-b.md
git status --short
```

Expected: `10 files` for each arm, no `FAILS` line, both reports present, and a clean tree. A
page that fails `--check` here counts as a fail for its arm under rule 1 of the decision rule
and is left as written; do not fix it.

- [ ] **Step 5: Record the token usage**

Each Agent completion notice carries the subagent's token usage where the harness reports it.
Write both figures to `.staging/phase-3/measurement/usage.yaml` as
`arm-a: {input: N, output: N, source: "harness completion notice"}` and the same for `arm-b`,
or `source: "not reported"` where it is absent. The decision note carries these in task 8.

---

### Task 8: Grade, read blind, decide, and land the ten

**Files:**
- Create (gitignored): `.staging/phase-3/measurement/arm-a/grading-report.md`,
  `.staging/phase-3/measurement/arm-b/grading-report.md`
- Create: `notes/phase-3-model-decision-2026-09.md`
- Modify: `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md` (section 10's Phase 3
  row, and one line in section 9)
- Modify: `nodes/<id>.md` for the ten measured nodes
- Modify: `notes/phase-3-pages-brief.md` only if step 7 finds a rule the pages showed missing

**Interfaces:**
- Consumes: the twenty bodies and two reports from task 7; `scripts/write_page.py` from task 2;
  `scripts/build_pages_report.py` from task 5; `writing-guidelines-grader`.
- Produces: the decision note the waves read their model from, and the first ten drafted pages.

- [ ] **Step 1: Dispatch two graders on Opus, in one message**

Two Agent calls with `model: "opus"`, one per arm, identical except the letter:

> Grade the directory `~/Documents/Repos/alchemist/.staging/phase-3/measurement/arm-<x>/` with
> the `writing-guidelines-grader` skill in non-interactive mode, as if invoked
> `/writing-guidelines-grader --auto <that directory>`. Grade every `.md` file directly in the
> directory; there are ten, each a short three-section page. Read the rubric in full first, as
> the skill requires. Write the report where the skill specifies, `grading-report.md` inside
> that directory. Return the compact verdict: for each file its fail count and warn count, and
> the two totals. Do not edit any file other than the report.

- [ ] **Step 2: Read both reports directly**

Open `.staging/phase-3/measurement/arm-a/grading-report.md` and `arm-b/grading-report.md`
yourself and tabulate, per arm, the total `fail` verdicts and total `warn` verdicts across the
ten pages, and the per-criterion counts. A grader agent's summary is a pointer and never the
record, per `~/.claude/rules/subagent-verification.md`; where the report and the summary
disagree, the report stands.

- [ ] **Step 3: Draw the blind pairs**

```bash
.venv/bin/python - <<'PY'
import random
TEN = ["future-lifetime-random-variable", "life-table", "lifetime-distribution-function",
       "survival-hazard-relationships", "censoring", "empirical-survival-function",
       "kaplan-meier-estimator", "nelson-aalen-estimator", "proportional-hazards-model",
       "survival-model-credit-risk"]
for n in random.Random(20260919).sample(TEN, 3):
    print(f".staging/phase-3/measurement/arm-a/{n}.md  against  .staging/phase-3/measurement/arm-b/{n}.md")
PY
```

- [ ] **Step 4: Stop for Mario's blind read**

Give Mario the three pairs of paths and nothing about which arm is which model. Ask for a
preference per pair, correctness of the mathematics first and voice second, in a sentence each.
Wait. Nothing below this line runs until the three verdicts are in hand.

- [ ] **Step 5: Apply the rule**

From spec section 5, applied as written:

1. A page that failed `--check` in task 7 step 4 adds one fail to its arm's total.
2. Primary score: total fails per arm. Secondary: total warns.
3. Sonnet writes Phase 3 unless Fable both records at least three fewer fails across the ten
   pages and takes at least two of the three blind pairs.

Compute it on the arm letters first, then unseal.

- [ ] **Step 6: Unseal and write the decision note**

```bash
cat .staging/phase-3/measurement/arms.yaml
```

Create `notes/phase-3-model-decision-2026-09.md` with these sections, every table filled from
steps 2, 4 and 5 and from `usage.yaml`:

```markdown
# Phase 3 model decision

Measured on <date> to the rule in section 5 of
`docs/superpowers/specs/2026-09-19-alchemist-phase-3-pages-design.md`, which was fixed before
either arm ran. Both arms wrote the same ten survival-area pages from
`notes/phase-3-pages-brief.md`, into staging directories named by arm letter; the grader ran on
Opus 5 and saw letters only, as did the blind read.

## The ten nodes

<the ten ids, one line each with depth, coverage and domains, from spec section 5's table>

## Template filter

arm-a: <n> of 10 passed `write_page.py --check`. arm-b: <n> of 10.

## Grades

| Criterion | arm-a fails | arm-a warns | arm-b fails | arm-b warns |
|---|---|---|---|---|
<one row per criterion that produced a fail or warn in either arm>
| **Total** | | | | |

## Blind read

| Pair | Preference | Mario's reason |
|---|---|---|
<three rows>

## Tokens

| Arm | Input | Output | Source |
|---|---|---|---|
<two rows from usage.yaml>

## Verdict

arm-a was <model> and arm-b was <model>, unsealed from `arms.yaml` after every row above was
written. Under the rule, <model> writes Phase 3, because <one sentence applying the three
conditions to the totals>.

## What the pages showed

<two or three observations both arms shared, and whether any becomes a brief amendment>
```

The observations feed step 7. Every number in the note traces to a file the executor read, and
the two `grading-report.md` files stay in staging as the raw record.

- [ ] **Step 7: Amend the brief if, and only if, both arms missed the same thing**

Where the grades or the blind read show a rule both arms broke, add it to
`notes/phase-3-pages-brief.md` under Writing rules and say so in the note's last section. Where
they differ, leave the brief alone: the difference is what the measurement measured.

- [ ] **Step 8: Record the verdict in the parent spec**

In `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`, section 10's table has
one row whose first cell is `3. Pages`; its cells are padded to the column widths. Replace its
second cell, `To be measured`, with `<Model>, measured`, and its third cell, `The only phase
with the volume for a per-token difference to matter`, with `Ten paired pages per arm, graded
blind; see notes/phase-3-model-decision-2026-09.md`, keeping the padding consistent with the
rows around it.

In section 9, after the paragraph beginning `Phase 1 exists as a distinct phase`, add:

```
Phase 3 ran ahead of Phase 2a for the 1,204 nodes no vault article covered, writing them as
drafts from the stub's scope, the anchor and standard material, under D3.3 of the Phase 3
design. Check 6 holds `reviewed` back for every one of them until its ledgered document arrives,
so the ordering the table gives still governs the status that matters.
```

- [ ] **Step 9: Land the winning arm's ten pages**

With `W` the winning arm's letter, and each node's `--spends` copied from
`.staging/phase-3/measurement/report-arm-W.md`:

```bash
W=<a or b>
for n in future-lifetime-random-variable life-table lifetime-distribution-function \
         survival-hazard-relationships censoring empirical-survival-function \
         kaplan-meier-estimator nelson-aalen-estimator proportional-hazards-model \
         survival-model-credit-risk; do
  .venv/bin/python scripts/write_page.py --node $n \
      --body .staging/phase-3/measurement/arm-$W/$n.md --spends <pairs from the report for $n>
done
.venv/bin/python scripts/check.py
.venv/bin/python scripts/build_site.py >/dev/null
.venv/bin/python scripts/katex_sweep.py nodes/future-lifetime-random-variable.md nodes/life-table.md \
    nodes/lifetime-distribution-function.md nodes/survival-hazard-relationships.md nodes/censoring.md \
    nodes/empirical-survival-function.md nodes/kaplan-meier-estimator.md nodes/nelson-aalen-estimator.md \
    nodes/proportional-hazards-model.md nodes/survival-model-credit-risk.md
.venv/bin/python scripts/build_pages_report.py
git status --short
```

Expected: ten `drafted` lines; twelve rules ok and `1560 nodes, 13 paths, 0 failures`; the
sweep reporting `0 unsupported`; `Pages by status: drafted 13, stub 1547`; and `git status`
showing exactly the ten node files, the note, the spec and possibly the brief. A spend the tool
refuses here is a spend the arm's report got wrong: correct the pair from the page's own
symbols, and say so in the note.

Open `site/nodes/lifetime-distribution-function.html` in a browser and confirm the alias table
renders three rows under "One object, several names", which is the reason that node is in the
ten.

- [ ] **Step 10: Commit**

```bash
git add nodes/future-lifetime-random-variable.md nodes/life-table.md nodes/lifetime-distribution-function.md nodes/survival-hazard-relationships.md nodes/censoring.md nodes/empirical-survival-function.md nodes/kaplan-meier-estimator.md nodes/nelson-aalen-estimator.md nodes/proportional-hazards-model.md nodes/survival-model-credit-risk.md notes/phase-3-model-decision-2026-09.md docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md notes/phase-3-pages-brief.md
git commit -m "feat(pages): settle the writing model and land the ten measured pages

Both arms wrote the same ten survival-area pages blind; an Opus grader
and a three-pair blind read decided under the rule fixed in advance.
The note records the grades, the tokens and the verdict, and the parent
spec's section 10 row takes it.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

### Task 9: Open the first pull request

**Files:** none.

- [ ] **Step 1: Full verification**

```bash
git status --short
.venv/bin/python scripts/check.py
.venv/bin/python -m pytest -q
ALCHEMIST_VAULT=/nonexistent .venv/bin/python scripts/check.py
```

Expected: a clean tree; twelve rules ok; `361 passed`; and with no vault, checks 5 and 11
skipping while the other ten pass, which is what CI will do.

- [ ] **Step 2: Push and open the pull request**

```bash
git push -u origin feat/phase-3-pages
gh pr create --base main --head feat/phase-3-pages \
  --title "feat(pages): add the write tool, check 12 and the model decision" \
  --body-file <body saved to a file first>
```

The body states: the tool and its refusals; check 12 and the eleven-to-twelve sweep; the
depth-ordered manifest and its 456-against-232 figure; the measurement's grade totals per arm,
the blind read's three verdicts, the token figures and the verdict, pointing at
`notes/phase-3-model-decision-2026-09.md`; and the ten pages landed. End with
`🤖 Generated with [Claude Code](https://claude.com/claude-code)`.

- [ ] **Step 3: Stop**

**Never self-merge.** Hand Mario the pull request and the decision note and wait. Task 10 starts
only after this pull request has merged, because its branch is cut from `main`.

---

### Task 10: Wave one, thirteen agents over batches 1 to 13

**Files:**
- Create (gitignored): `.staging/phase-3/manifest.yaml`, `.staging/phase-3/report-01.md` to
  `report-13.md`, `.staging/phase-3/grading-wave-1/`
- Modify: `nodes/*.md` for batches 1 to 13 (520 nodes)
- Create: `notes/phase-3-reports/README.md`, `notes/phase-3-reports/report-01.md` to `report-13.md`

**Interfaces:**
- Consumes: `build_manifest.py --phase 3 --order depth` (task 4), `write_page.py` (task 2), the
  brief (task 6), the model named in `notes/phase-3-model-decision-2026-09.md` (task 8),
  `build_pages_report.py` (task 5), `stray_writes` from `batches.py`.
- Produces: 520 drafted pages and thirteen reports.

- [ ] **Step 1: Cut the branch and build the manifest**

```bash
git checkout main && git pull --ff-only
git checkout -b feat/phase-3-wave-1
.venv/bin/python scripts/build_manifest.py --phase 3 --order depth
```

Expected: `1547 nodes -> 39 batches across 3 waves`. The 1,547 are the stubs left after the three
exemplars and the ten measured pages.

- [ ] **Step 2: Dispatch thirteen agents, one per batch, in one message**

Read the model from the Verdict section of `notes/phase-3-model-decision-2026-09.md` and set it
as `model` on every dispatch. The brief for batch NN is exactly this, with NN substituted and
zero-padded to two digits:

> You are writing Phase 3 pages for the alchemist corpus, batch NN. Work in
> `~/Documents/Repos/alchemist` and use `.venv/bin/python` for everything.
>
> Read `notes/phase-3-pages-brief.md` first and follow it exactly. Your node ids are the `nodes`
> list under `batches: NN:` in `.staging/phase-3/manifest.yaml`; work them in that order. Land
> every page with `scripts/write_page.py` as the brief says, and write your report to
> `.staging/phase-3/report-NN.md`.
>
> Never touch a node outside your list, never edit `notation/objects.yaml` or anything under
> `sources/`, and never set `reviewed`. Finish by running `.venv/bin/python scripts/check.py`
> and reporting its last line.

- [ ] **Step 3: Verify no agent wrote outside its batch**

```bash
.venv/bin/python - <<'PY'
import subprocess, sys, yaml
sys.path.insert(0, ".")
from scripts.alchemist.batches import stray_writes
manifest = yaml.safe_load(open(".staging/phase-3/manifest.yaml"))
changed = [l.split("/")[-1].removesuffix(".md")
           for l in subprocess.run(["git", "diff", "--name-only", "--", "nodes/"],
                                   capture_output=True, text=True).stdout.split()]
owned = {i for n in range(1, 14) for i in manifest["batches"][n]["nodes"]}
stray = sorted(set(changed) - owned)
print(f"{len(changed)} nodes changed, {len(stray)} stray")
if stray:
    print("STRAY:", stray[:20])
other = subprocess.run(["git", "status", "--short"], capture_output=True, text=True).stdout
print("outside nodes/:", [l for l in other.splitlines() if " nodes/" not in l] or "nothing")
PY
```

Expected: `520 nodes changed, 0 stray` and `outside nodes/: nothing`. A stray write means an
agent left its assignment: `git checkout -- nodes/<id>.md` for each and rerun that batch. A
change outside `nodes/` is reverted the same way.

- [ ] **Step 4: Run the checks, the build, the sweep and the report**

```bash
.venv/bin/python scripts/check.py
.venv/bin/python scripts/build_site.py >/dev/null && echo built
.venv/bin/python scripts/katex_sweep.py $(git diff --name-only -- nodes/)
.venv/bin/python scripts/build_pages_report.py
```

Expected: twelve rules ok with `0 failures`; `built`; the sweep ending `0 unsupported`; and
`Pages by status: drafted 533, stub 1027`. A check 12 failure here cannot come from the tool and
means a hand edit: find it with the failure's node id and re-land the page through the tool. A
check 1 failure means the same. An unsupported KaTeX span is fixed by re-landing that page with
the construct rewritten. Keep every number the report prints for the gate note.

- [ ] **Step 5: Grade a sample of five pages per batch**

```bash
.venv/bin/python - <<'PY'
import random, re
from pathlib import Path
import yaml
WAVE = 1
manifest = yaml.safe_load(Path(".staging/phase-3/manifest.yaml").read_text())
rng = random.Random(20260919 + WAVE)
out = Path(f".staging/phase-3/grading-wave-{WAVE}")
out.mkdir(parents=True, exist_ok=True)
for number, batch in sorted(manifest["batches"].items()):
    if batch["wave"] != WAVE:
        continue
    for node_id in rng.sample(batch["nodes"], 5):
        text = Path(f"nodes/{node_id}.md").read_text()
        (out / f"{node_id}.md").write_text(re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S))
print(len(list(out.glob("*.md"))), "bodies staged for grading")
PY
```

Expected: `65 bodies staged for grading`. Then one Agent call with `model: "opus"`:

> Grade the directory `~/Documents/Repos/alchemist/.staging/phase-3/grading-wave-1/` with the
> `writing-guidelines-grader` skill in non-interactive mode, as if invoked
> `/writing-guidelines-grader --auto <that directory>`. There are 65 short three-section pages.
> Read the rubric in full first. Write `grading-report.md` inside that directory and return the
> compact verdict: total fails, total warns, and the five files with the most fails.

Read `grading-report.md` yourself and record the totals and the criteria that failed most. A
page with a hard fail is re-landed through the tool with the breach fixed, never hand-edited.

- [ ] **Step 6: Keep the reports**

```bash
mkdir -p notes/phase-3-reports
cp .staging/phase-3/report-0[1-9].md .staging/phase-3/report-1[0-3].md notes/phase-3-reports/
cp .staging/phase-3/manifest.yaml notes/phase-3-reports/manifest.yaml
```

Create `notes/phase-3-reports/README.md`:

```markdown
# Phase 3 pages reports

One report per batch, thirty-nine once every wave has run, written by the agents that worked
batches 1 to 39 across three waves from September 2026. Each names, per node, what the page was
written from, the spends it declared, any collision candidate for the notation contract and any
split candidate the template could not hold.

They are here because `.staging/phase-3/` is gitignored, so it exists only in the working tree
that ran the phase; a fresh clone has neither the manifest nor the fragments, and these are the
durable record. The brief they were written to is `notes/phase-3-pages-brief.md`, and the
collision and split candidates they name feed G30 and G31 in section 16 of the Phase 3 design.
```

- [ ] **Step 7: Commit the wave**

```bash
git status --short | grep -v "^ M nodes/\|^?? notes/phase-3-reports/\|^A  notes/phase-3-reports/"
git add nodes/ notes/phase-3-reports/
git commit -m "feat(pages): write wave one, batches 1 to 13

520 pages landed through write_page.py against the template, from the
attached vault articles where a node has them and from the stub's scope
and anchor where it has none. Twelve checks clean, KaTeX sweep clean,
grader sample of 65 recorded in the pull request.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

The first line must print nothing: `git add nodes/` is the whole directory deliberately, since
the wave touches 520 files in it and nothing else in the tree, and that grep is what confirms
the "nothing else".

- [ ] **Step 8: Draw Mario's spot-read and stop**

```bash
.venv/bin/python - <<'PY'
import random
from pathlib import Path
import yaml
WAVE = 1
manifest = yaml.safe_load(Path(".staging/phase-3/manifest.yaml").read_text())
rng = random.Random(20260919 + WAVE + 100)
for number, batch in sorted(manifest["batches"].items()):
    if batch["wave"] == WAVE:
        print(f"batch {number:02d}: site/nodes/{rng.choice(batch['nodes'])}.html")
PY
```

Give Mario the thirteen paths on the built site, correctness first and voice second, together
with the report's figures and the grader's totals. Wait. A page he sends back is re-landed
through the tool as a follow-up commit on this branch.

- [ ] **Step 9: Push and open the pull request**

```bash
git push -u origin feat/phase-3-wave-1
gh pr create --base main --head feat/phase-3-wave-1 \
  --title "feat(pages): write wave one, batches 1 to 13" \
  --body-file <body saved to a file first>
```

The body carries the gate note: the seven lines `build_pages_report.py` printed, the grader's
totals and most-failed criteria, the stray-write result, the sweep result, the number of
collision candidates and split candidates across the thirteen reports (`grep -c -i "collision"
notes/phase-3-reports/report-0*.md` and the same for `split`), and what Mario's spot-read found.
End with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.

**Never self-merge.** Task 11 starts only after this pull request has merged.

---

### Task 11: Waves two and three

**Files:** as task 10, for batches 14 to 26 and then 27 to 39, on `feat/phase-3-wave-2` and
`feat/phase-3-wave-3`.

Each wave repeats task 10's nine steps with these substitutions and nothing else changed. The
manifest is **not** rebuilt: `.staging/phase-3/manifest.yaml` from task 10 step 1 still holds
every batch, and rebuilding it after 520 pages landed would renumber the remaining stubs into
different batches, which is why `build_manifest.py` refuses to overwrite it without `--force`.
Where the working tree that ran task 10 is gone, restore it with
`cp notes/phase-3-reports/manifest.yaml .staging/phase-3/manifest.yaml`, the tracked copy task
10 made, and never rebuild it.

| | Wave 2 | Wave 3 |
|---|---|---|
| Branch (step 1) | `feat/phase-3-wave-2` | `feat/phase-3-wave-3` |
| Batches dispatched (step 2) | 14 to 26 | 27 to 39 |
| `owned` range (step 3) | `range(14, 27)` | `range(27, 40)` |
| Expected changed nodes (step 3) | 520 | 507 |
| Expected report line (step 4) | `drafted 1053, stub 507` | `drafted 1560` and no `stub` |
| `WAVE` (steps 5 and 8) | 2 | 3 |
| Expected bodies staged (step 5) | 65 | 65 (batch 39 holds 27, and 5 are drawn from it as from the others) |
| Reports copied (step 6) | `report-1[4-9].md report-2[0-6].md` | `report-2[7-9].md report-3[0-9].md` |
| Commit title (step 7) | `feat(pages): write wave two, batches 14 to 26` | `feat(pages): write wave three, batches 27 to 39` |
| Pull request title (step 9) | same as the commit | same as the commit |

The README in `notes/phase-3-reports/` needs no edit for wave 2. For wave 3, change "thirty-nine
once every wave has run" to "thirty-nine" and commit it with the wave.

Between waves, Mario may grow `notation/objects.yaml` from the collision candidates (G30). Where
he has, run `.venv/bin/python scripts/build_site.py` so `notation/symbols.md` regenerates and
check 7 passes, and note in the next wave's pull request which objects were added; the sweep
that declares the new spends on already-written pages is G30's own task and is not part of a
wave.

---

### Task 12: Close the phase

**Files:**
- Create: `notes/phase-3-gate-2026-09.md`
- Modify: `notes/phase-3-reports/README.md` if wave 3 did not already amend the count

- [ ] **Step 1: Cut the branch and gather the figures**

```bash
git checkout main && git pull --ff-only
git checkout -b docs/phase-3-close-out
.venv/bin/python scripts/check.py | tail -1
.venv/bin/python scripts/build_pages_report.py
grep -il "collision" notes/phase-3-reports/report-*.md | wc -l
grep -il "split" notes/phase-3-reports/report-*.md | wc -l
```

Expected: `1560 nodes, 13 paths, 0 failures`; `Pages by status: drafted 1560`; and the two
counts of reports naming at least one collision or split candidate.

- [ ] **Step 2: Write the gate note**

Create `notes/phase-3-gate-2026-09.md` with these sections, every figure from step 1, the three
pull requests' bodies and the decision note:

```markdown
# Phase 3 gate

Closed on <date>. Every one of the 1,560 nodes carries a written page, 1,557 of them landed this
phase through `scripts/write_page.py` and three as Phase 0's exemplars, and every page passes
check 12.

## The figures

<the seven lines build_pages_report.py printed, verbatim>

## The three waves

| Wave | Batches | Pages | Grader sample fails | Grader sample warns | Spot-read findings |
|---|---|---|---|---|---|
<three rows from the pull requests>

## The model

<one paragraph: which model wrote, from notes/phase-3-model-decision-2026-09.md, and the
measured tokens per page from the three waves' harness notices where reported>

## Collision candidates, for G30

<one line per proposed object across the thirty-nine reports, deduplicated: id, domains, spelling>

## Split candidates, for G31

<one line per node the reports named as wanting a third display block or a fourth section>

## Pages naming no unlock

<the list build_pages_report.py printed, with a one-line reading of whether each is a real
omission or an inflection the approximate match missed>

## What Phase 4 inherits

<two or three sentences: the trunk is drafted end to end, the survival braid's pages are the
first S-track lecture's reading, and reviewed is still gated by acquisition through check 6>
```

- [ ] **Step 3: Commit, push and open the pull request**

```bash
git add notes/phase-3-gate-2026-09.md notes/phase-3-reports/README.md
git commit -m "docs(notes): close Phase 3 with the gate note

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
git push -u origin docs/phase-3-close-out
gh pr create --base main --head docs/phase-3-close-out \
  --title "docs(notes): close Phase 3 with the gate note" \
  --body "The gate note for Phase 3: the corpus's figures at 1,560 written pages, the three waves' grades and spot-reads, and the collision and split candidates G30 and G31 take up.

🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

**Never self-merge.** Hand Mario the note. Phase 4 gets its own plan.

---

## Self-review

**Spec coverage.** Section 4 (template): tasks 1 and 6. Section 5 (measurement, rule, record,
landing, tokens): tasks 7 and 8. Section 6 (writing without an article): the brief's step 2 in
task 6, and D3.3's line in the parent spec in task 8 step 8. Section 7 (notation at scale): the
tool's spend refusal in task 2 and the brief's spends section in task 6; G30's sweep is
deliberately outside the waves, stated in task 11. Section 8 (tool and check 12): tasks 2 and 3,
including the eleven-to-twelve sweep. Section 9 (batching and contract): tasks 4, 6 and 10.
Section 10 (gate): tasks 5, 10, 11 and 12, with per-wave pull requests. Section 11 (failure
handling): task 10 steps 3 and 4. Section 12 (testing): tasks 1 to 5. Section 14 (amendments):
task 3 step 5 and task 8 step 8. Section 15 (order): the task order. Section 16 (backlog): task 12
gathers G30 and G31's inputs.

**Two departures from the spec, both recorded here.** The spec's section 10 keeps the grader's
reports in staging, and this plan does too, but it also copies the thirty-nine batch reports
into `notes/phase-3-reports/`, following what Phase 2 did after its README found the staging
directory was the only copy. And the spec's section 5 first placed the arm report inside the arm
directory; the grader grades every markdown file in a directory, so the spec was amended before
commit to `report-arm-<x>.md` beside the directories, which is what task 7 writes.

**Placeholder scan.** Every code step carries its code. The angle-bracket fields in tasks 8, 9,
10 and 12 are values the executor reads off a file or a notice at that step (the winning arm,
the grade totals, the spend pairs, the pull request body) and each names where it comes from.

**Type consistency.** `validate_body(body: str) -> list[str]` in tasks 1, 2 and 3.
`write_page(node_file, body, spends, objects, *, force=False) -> Node` and `parse_spend(text)
-> Spend` in tasks 2 and 8. `page_statistics(corpus) -> dict` with keys `by_status`,
`written_by_domain`, `display_blocks`, `words`, `rather_than`, `no_forward_reference` in tasks 2
and 5. `depth_key(nodes)`, `phase_node_ids(nodes, phase)`, `slice_batches(node_ids, size, key)`
and `manifest_payload(node_ids, size, per_wave, key)` in task 4 and the CLI it rewrites.
`check_template_conformance(corpus) -> Result` with rule string `12. written pages follow the
template` in task 3's code and test. `Result`, `Corpus`, `Node`, `Spend`, `Objects` as
`model.py` and `checks.py` already define them.

**Test count.** 321, then 334 (task 1), 350 (task 2), 355 (task 3), 360 (task 4), 361 (task 5).
Where an executor writes a different number of tests the total moves with it; it never falls.
