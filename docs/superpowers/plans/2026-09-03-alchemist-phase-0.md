# Alchemist Phase 0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the machinery the syllabus corpus runs on: the graph schema, the seven-rule checker, the site generator, and a network-free Quarto render and print chain, proven end to end on two exemplars.

**Architecture:** A node is a markdown file whose YAML frontmatter is the graph, so there is no separate registry to drift. A small Python package under `scripts/alchemist/` loads those files into typed records; `check.py` runs seven rules over them and `build_site.py` generates every derived artefact. Lectures render through Quarto with KaTeX vendored locally, then a post-render step inlines the three assets that remain, so a lecture opens from a bare disk with no network.

**Tech Stack:** Python 3.14.7 under `uv` in an in-repo `.venv`; PyYAML and pytest for the tooling; Quarto 1.10.18 for lectures; graphviz `dot` for the graph views; headless Chrome for PDFs.

**Spec:** `docs/superpowers/specs/2026-09-03-alchemist-syllabus-design.md`

**Scope:** This plan covers Phase 0 only, which is the whole of the software. Phases 1 to 4 are content runs against this machinery, and their orchestration depends on what Phase 1 actually produces, so each gets its own plan after gate 1.

## Global Constraints

- Python is always `.venv/bin/python`. Never a system `python3`: this machine carries 3.14.3 under `/Library/Frameworks` and 3.14.7 under `/opt/homebrew`, and neither has the packages.
- The repo is public. Assume anything committed is published on landing. Nothing from a Gini engagement, no client parameters or figures, and no example borrowing either.
- `data/` is gitignored. Public datasets only, each rebuilt by a script from its public URL.
- ETH-derived material is licensed **CC BY-NC 4.0**, so the corpus stays non-commercial, with attribution and a statement of changes.
- Node ids are stable slugs matching `^[a-z0-9]+(-[a-z0-9]+)*$` and are never renamed.
- `domains` draws on a closed vocabulary: `maths`, `stats`, `ml`, `data-eng`, `fin-eng`, `actuarial`, `life`, `gi`, `credit`, `regulation`.
- `anchor` follows `<body>.<subject>.<section>[.<item>]`, lowercase and dot-separated, or the literal `chosen`.
- Quarto's KaTeX `url` **must end with a trailing slash**. Verified 3 September 2026: Quarto concatenates the url with the filename with no separator, so `url: "../vendor/katex"` emits `vendor/katexkatex.min.js` and the maths silently fails to typeset.
- Writing rules apply to every file, `CLAUDE.md` included: British English, and no em or en dashes as punctuation.
- Conventional Commits, one concern per commit.

---

## File Structure

| Path | Responsibility |
|---|---|
| `scripts/alchemist/model.py` | Typed records (`Node`, `TeachingPath`, `Objects`, `Corpus`) and the loaders that parse them off disk. Validates shape, never semantics. |
| `scripts/alchemist/checks.py` | The seven rules. Each is a function taking a `Corpus` and returning a list of failure strings. No I/O beyond the vault register. |
| `scripts/alchemist/site.py` | Every generated artefact: `symbols.md`, `index.html`, one page per path, one DOT graph per domain. |
| `scripts/check.py` | CLI entry point. Runs the rules, prints failures, exits non-zero on any. |
| `scripts/build_site.py` | CLI entry point for the generators. |
| `scripts/inline_assets.py` | Post-render: inlines `assets/lecture.css` and the KaTeX pair into one self-contained file. |
| `scripts/katex_embed_fonts.py` | One-off: rewrites `vendor/katex/katex.min.css` font URLs as base64 data URIs. |
| `scripts/render_lecture.sh` | Carried from the trunk repo. Quarto render, then strip Quarto's theme assets, then relocate figures. |
| `scripts/html_to_pdf.sh` | Carried from the trunk repo. Headless Chrome with a watchdog and a `%%EOF` check. |
| `scripts/fetch_credit_data.py` | Rebuilds the public credit parquets the exemplar lecture reads. |
| `tests/` | One test module per checks group, plus `test_model.py` and `test_site.py`. |

---

### Task 1: Repo skeleton and the graph loader

**Files:**
- Create: `.python-version`, `.gitignore`, `.prettierignore`, `requirements-dev.txt`, `requirements.txt`
- Create: `scripts/alchemist/__init__.py`, `scripts/alchemist/model.py`
- Test: `tests/test_model.py`

**Interfaces:**
- Consumes: nothing.
- Produces: `DOMAINS: frozenset[str]`, `STATUSES: frozenset[str]`, `Spend(object: str, domain: str)`, `Node(id, title, domains, status, requires, spends, anchor, vault_articles, vault_sources, taught_in, body, path)`, `TeachingPath(id, title, builds_on, preamble, nodes)`, `Corpus(nodes: dict[str, Node], paths: dict[str, TeachingPath])`, `parse_node(path: Path) -> Node`, `parse_path(path: Path) -> TeachingPath`, `load_corpus(root: Path) -> Corpus`.

- [ ] **Step 1: Create the skeleton and the environment**

```bash
cd ~/Documents/Repos/alchemist
mkdir -p scripts/alchemist tests nodes paths notation sources lectures/figures notes assets vendor data
echo "3.14.7" > .python-version
printf 'pyyaml==6.0.2\npytest==8.4.2\nmarkdown-it-py==3.0.0\nnbformat==5.10.4\nnbclient==0.10.2\n' > requirements-dev.txt
cp ../actuarial_deep_learning/requirements.txt requirements.txt
printf '/data/\n.venv/\n__pycache__/\n.pytest_cache/\n*.pyc\n.DS_Store\nlectures/*.html\nsite/\n' > .gitignore
printf 'lectures/*.html\nvendor/\n' > .prettierignore
uv venv --python 3.14.7 .venv
uv pip install --python .venv -r requirements-dev.txt
```

`requirements.txt` is copied rather than curated: the exemplar lecture was authored against those pins, and a divergence turns a render failure into a debugging job. `lectures/*.html` is gitignored here because, unlike the trunk repo, Alchemist assembles its site in the Pages workflow and the rendered HTML is a build artefact.

- [ ] **Step 2: Write the failing test**

```python
# tests/test_model.py
from pathlib import Path

import pytest

from scripts.alchemist.model import DOMAINS, Node, Spend, parse_node

VALID = """---
id: hazard-rate
title: Hazard rate
domains: [stats, credit]
status: stub
requires: [survival-function]
spends:
  - {object: obj.hazard, domain: credit}
anchor: [ifoa.cs2.3.2]
vault_articles: [methods/exponential-dispersion-family-and-glm]
vault_sources: []
taught_in: null
---

The instantaneous rate of default.
"""


def write(tmp_path: Path, name: str, text: str) -> Path:
    target = tmp_path / name
    target.write_text(text)
    return target


def test_parses_a_valid_node(tmp_path):
    node = parse_node(write(tmp_path, "hazard-rate.md", VALID))
    assert node.id == "hazard-rate"
    assert node.domains == ("stats", "credit")
    assert node.spends == (Spend("obj.hazard", "credit"),)
    assert node.taught_in is None
    assert node.body.strip() == "The instantaneous rate of default."


def test_rejects_a_filename_that_disagrees_with_the_id(tmp_path):
    with pytest.raises(ValueError, match="does not match id"):
        parse_node(write(tmp_path, "hazard.md", VALID))


def test_rejects_a_domain_outside_the_vocabulary(tmp_path):
    bad = VALID.replace("[stats, credit]", "[stats, insurance]")
    with pytest.raises(ValueError, match="unknown domains"):
        parse_node(write(tmp_path, "hazard-rate.md", bad))


def test_rejects_a_malformed_anchor(tmp_path):
    bad = VALID.replace("[ifoa.cs2.3.2]", "[CS2 section 3.2]")
    with pytest.raises(ValueError, match="malformed anchor"):
        parse_node(write(tmp_path, "hazard-rate.md", bad))


def test_domain_vocabulary_is_closed():
    assert "regulation" in DOMAINS and "insurance" not in DOMAINS
```

- [ ] **Step 3: Run the test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_model.py -v`
Expected: FAIL, collection error, `ModuleNotFoundError: No module named 'scripts'`.

- [ ] **Step 4: Write the minimal implementation**

```python
# scripts/alchemist/model.py
"""Typed records for the Alchemist graph, and the loaders that read them off disk.

Shape is validated here and semantics in checks.py, so a malformed file fails at
parse time with its own path in the message, and a well-formed file that breaks a
rule fails later with the rule named.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]

DOMAINS = frozenset({
    "maths", "stats", "ml", "data-eng", "fin-eng",
    "actuarial", "life", "gi", "credit", "regulation",
})
STATUSES = frozenset({"stub", "drafted", "reviewed"})

SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ANCHOR = re.compile(r"^[a-z0-9]+(\.[a-z0-9-]+){2,3}$")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.S)


@dataclass(frozen=True)
class Spend:
    object: str
    domain: str


@dataclass(frozen=True)
class Node:
    id: str
    title: str
    domains: tuple[str, ...]
    status: str
    requires: tuple[str, ...]
    spends: tuple[Spend, ...]
    anchor: tuple[str, ...]
    vault_articles: tuple[str, ...]
    vault_sources: tuple[str, ...]
    taught_in: str | None
    body: str
    path: Path


@dataclass(frozen=True)
class TeachingPath:
    id: str
    title: str
    builds_on: tuple[str, ...]
    preamble: str
    nodes: tuple[str, ...]


@dataclass(frozen=True)
class Corpus:
    nodes: dict[str, Node]
    paths: dict[str, TeachingPath]


def parse_node(path: Path) -> Node:
    match = FRONTMATTER.match(path.read_text())
    if match is None:
        raise ValueError(f"{path}: no YAML frontmatter")
    meta = yaml.safe_load(match.group(1)) or {}

    missing = {"id", "title", "domains", "status"} - meta.keys()
    if missing:
        raise ValueError(f"{path}: missing required keys {sorted(missing)}")
    if not SLUG.match(str(meta["id"])):
        raise ValueError(f"{path}: id {meta['id']!r} is not a slug")
    if path.stem != meta["id"]:
        raise ValueError(f"{path}: filename does not match id {meta['id']!r}")
    unknown = set(meta["domains"]) - DOMAINS
    if unknown:
        raise ValueError(f"{path}: unknown domains {sorted(unknown)}")
    if meta["status"] not in STATUSES:
        raise ValueError(f"{path}: unknown status {meta['status']!r}")
    for anchor in meta.get("anchor") or []:
        if anchor != "chosen" and not ANCHOR.match(anchor):
            raise ValueError(f"{path}: malformed anchor {anchor!r}")

    return Node(
        id=meta["id"],
        title=meta["title"],
        domains=tuple(meta["domains"]),
        status=meta["status"],
        requires=tuple(meta.get("requires") or []),
        spends=tuple(
            Spend(s["object"], s["domain"]) for s in meta.get("spends") or []
        ),
        anchor=tuple(meta.get("anchor") or []),
        vault_articles=tuple(meta.get("vault_articles") or []),
        vault_sources=tuple(meta.get("vault_sources") or []),
        taught_in=meta.get("taught_in"),
        body=match.group(2),
        path=path,
    )


def parse_path(path: Path) -> TeachingPath:
    meta = yaml.safe_load(path.read_text()) or {}
    missing = {"id", "title", "nodes"} - meta.keys()
    if missing:
        raise ValueError(f"{path}: missing required keys {sorted(missing)}")
    if path.stem != meta["id"]:
        raise ValueError(f"{path}: filename does not match id {meta['id']!r}")
    return TeachingPath(
        id=meta["id"],
        title=meta["title"],
        builds_on=tuple(meta.get("builds_on") or []),
        preamble=meta.get("preamble", ""),
        nodes=tuple(meta["nodes"]),
    )


def load_corpus(root: Path = REPO) -> Corpus:
    nodes = {n.id: n for n in map(parse_node, sorted((root / "nodes").glob("*.md")))}
    paths = {p.id: p for p in map(parse_path, sorted((root / "paths").glob("*.yaml")))}
    return Corpus(nodes=nodes, paths=paths)
```

- [ ] **Step 5: Make the package importable from the repo root, then run the test**

```bash
touch scripts/__init__.py scripts/alchemist/__init__.py
printf '[tool.pytest.ini_options]\npythonpath = ["."]\ntestpaths = ["tests"]\n' > pyproject.toml
.venv/bin/python -m pytest tests/test_model.py -v
```

Expected: 5 passed.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(model): parse node and path files into typed records"
```

---

### Task 2: The notation contract

**Files:**
- Create: `notation/objects.yaml`
- Modify: `scripts/alchemist/model.py` (append the objects loader)
- Test: `tests/test_notation.py`

**Interfaces:**
- Consumes: `Corpus`, `Spend` from Task 1.
- Produces: `MathObject(id: str, name: str, canonical: str, definition: str, aliases: tuple[Alias, ...])`, `Alias(domain: str, symbol: str, name: str, note: str | None)`, `Objects(by_id: dict[str, MathObject])` with method `rendering(self, spend: Spend) -> str` raising `KeyError` on an unknown object and `LookupError` on an object with no alias for that domain, and `load_objects(root: Path) -> Objects`.

- [ ] **Step 1: Seed the contract with the twelve collisions from the spec**

Write `notation/objects.yaml`. The twelve entries are the collision table in spec section 4.2, and each `canonical` is the rendering a domain-neutral node uses. Where a domain genuinely has no rendering for an object, it gets no alias row, and a node in that domain that tries to spend it fails check 1.

```yaml
# The canonical objects of the corpus. A domain keeps its own notation as an
# alias; the corpus keeps one meaning per object. Cross-domain bridge tables are
# generated from the alias rows, so this file is the only place a symbol is
# spelled out.
- id: obj.hazard
  name: Hazard rate
  canonical: 'h(t)'
  definition: The instantaneous rate at which the event occurs, conditional on survival to t.
  aliases:
    - {domain: life, symbol: '\mu_x', name: force of mortality, note: age-indexed and continuous}
    - {domain: gi, symbol: '\lambda', name: claim intensity}
    - {domain: credit, symbol: 'h(t)', name: default hazard}
    - {domain: stats, symbol: '\lambda(t)', name: hazard function}
- id: obj.survival
  name: Survival function
  canonical: 'S(t)'
  definition: The probability that the event has not occurred by time t.
  aliases:
    - {domain: life, symbol: '{}_tp_x', name: survival probability}
    - {domain: credit, symbol: 'S(t)', name: survival function}
    - {domain: stats, symbol: 'S(t)', name: survival function}
- id: obj.lifetime-cdf
  name: Lifetime distribution function
  canonical: 'F(t)'
  definition: The probability that the event has occurred by time t.
  aliases:
    - {domain: life, symbol: '{}_tq_x', name: mortality probability}
    - {domain: credit, symbol: 'F(t)', name: cumulative default probability}
    - {domain: stats, symbol: 'F(t)', name: distribution function}
- id: obj.normal-cdf
  name: Standard normal distribution function
  canonical: '\Phi(\cdot)'
  definition: The distribution function of a standard normal variate.
  aliases:
    - {domain: credit, symbol: 'N(\cdot)', name: normal distribution function, note: the Basel formula's own notation}
    - {domain: stats, symbol: '\Phi(\cdot)', name: standard normal CDF}
- id: obj.normal-quantile
  name: Standard normal quantile function
  canonical: '\Phi^{-1}(\cdot)'
  definition: The inverse of the standard normal distribution function.
  aliases:
    - {domain: credit, symbol: 'G(\cdot)', name: inverse normal, note: the Basel formula's own notation}
    - {domain: stats, symbol: '\Phi^{-1}(\cdot)', name: normal quantile}
- id: obj.asset-correlation
  name: Asset correlation
  canonical: '\rho'
  definition: The correlation between the latent asset returns of two obligors.
  aliases:
    - {domain: credit, symbol: 'R', name: asset correlation, note: the Basel formula's own notation}
    - {domain: stats, symbol: '\rho', name: correlation}
- id: obj.response-mean
  name: Expected response
  canonical: '\mu'
  definition: The expectation of the response variable under the fitted model.
  aliases:
    - {domain: gi, symbol: '\mu', name: expected claim frequency}
    - {domain: stats, symbol: '\mu', name: mean}
    - {domain: ml, symbol: '\hat{y}', name: prediction}
- id: obj.dispersion
  name: Dispersion parameter
  canonical: '\varphi'
  definition: The dispersion parameter of an exponential dispersion family.
  aliases:
    - {domain: gi, symbol: '\varphi', name: dispersion}
    - {domain: stats, symbol: '\varphi', name: dispersion}
- id: obj.regularisation
  name: Regularisation weight
  canonical: '\lambda_{\mathrm{reg}}'
  definition: The weight on a penalty term in a regularised objective.
  aliases:
    - {domain: ml, symbol: '\lambda_{\mathrm{reg}}', name: regularisation weight, note: subscripted deliberately, because bare lambda is the claim intensity and the hazard}
    - {domain: stats, symbol: '\lambda_{\mathrm{reg}}', name: penalty weight}
- id: obj.exposure
  name: Exposure
  canonical: 'e_i'
  definition: The amount at risk for observation i, which the response is measured against.
  aliases:
    - {domain: gi, symbol: 'v_i', name: exposure years}
    - {domain: credit, symbol: '\mathrm{EAD}_i', name: exposure at default}
    - {domain: ml, symbol: 'e_i', name: offset}
- id: obj.discount-factor
  name: Discount factor
  canonical: 'v'
  definition: The present value of one unit payable in one period.
  aliases:
    - {domain: actuarial, symbol: 'v', name: discount factor, note: v = 1/(1+i). Collides with the general-insurance exposure weight, which is why exposure is canonically e_i here}
    - {domain: fin-eng, symbol: 'v', name: discount factor}
- id: obj.coefficients
  name: Regression coefficients
  canonical: '\beta'
  definition: The parameter vector of a linear or generalised linear predictor.
  aliases:
    - {domain: gi, symbol: '\beta', name: GLM coefficients}
    - {domain: credit, symbol: '\beta', name: scorecard coefficients}
    - {domain: stats, symbol: '\beta', name: coefficients}
    - {domain: ml, symbol: '\theta', name: parameters, note: network weights, where beta would imply linearity}
```

- [ ] **Step 2: Write the failing test**

```python
# tests/test_notation.py
import pytest

from scripts.alchemist.model import REPO, Spend, load_objects


@pytest.fixture(scope="module")
def objects():
    return load_objects(REPO)


def test_a_domain_alias_wins_over_the_canonical(objects):
    assert objects.rendering(Spend("obj.hazard", "life")) == r"\mu_x"
    assert objects.rendering(Spend("obj.hazard", "credit")) == "h(t)"


def test_an_object_with_no_alias_for_the_domain_is_a_lookup_error(objects):
    with pytest.raises(LookupError, match="no alias"):
        objects.rendering(Spend("obj.discount-factor", "credit"))


def test_an_unknown_object_is_a_key_error(objects):
    with pytest.raises(KeyError):
        objects.rendering(Spend("obj.nonsense", "credit"))


def test_the_seeded_collisions_are_all_present(objects):
    assert {"obj.hazard", "obj.exposure", "obj.discount-factor"} <= objects.by_id.keys()


def test_bare_lambda_is_never_the_regularisation_weight(objects):
    """The collision the contract exists to prevent: lambda is the intensity."""
    assert objects.rendering(Spend("obj.regularisation", "ml")) != r"\lambda"
    assert objects.rendering(Spend("obj.hazard", "gi")) == r"\lambda"
```

- [ ] **Step 3: Run the test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_notation.py -v`
Expected: FAIL, `ImportError: cannot import name 'load_objects'`.

- [ ] **Step 4: Append the loader to `scripts/alchemist/model.py`**

```python
@dataclass(frozen=True)
class Alias:
    domain: str
    symbol: str
    name: str
    note: str | None = None


@dataclass(frozen=True)
class MathObject:
    id: str
    name: str
    canonical: str
    definition: str
    aliases: tuple[Alias, ...]

    def for_domain(self, domain: str) -> Alias | None:
        return next((a for a in self.aliases if a.domain == domain), None)


@dataclass(frozen=True)
class Objects:
    by_id: dict[str, MathObject]

    def rendering(self, spend: Spend) -> str:
        obj = self.by_id[spend.object]
        alias = obj.for_domain(spend.domain)
        if alias is None:
            raise LookupError(
                f"{obj.id} has no alias for domain {spend.domain!r}"
            )
        return alias.symbol


def load_objects(root: Path = REPO) -> Objects:
    raw = yaml.safe_load((root / "notation" / "objects.yaml").read_text()) or []
    by_id: dict[str, MathObject] = {}
    for entry in raw:
        unknown = {a["domain"] for a in entry["aliases"]} - DOMAINS
        if unknown:
            raise ValueError(f"{entry['id']}: unknown alias domains {sorted(unknown)}")
        by_id[entry["id"]] = MathObject(
            id=entry["id"],
            name=entry["name"],
            canonical=entry["canonical"],
            definition=entry["definition"],
            aliases=tuple(
                Alias(a["domain"], a["symbol"], a["name"], a.get("note"))
                for a in entry["aliases"]
            ),
        )
    return Objects(by_id=by_id)
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_notation.py -v`
Expected: 5 passed.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(notation): seed the object contract with the twelve collisions"
```

---

### Task 3: Checks 1 and 2, the notation rules

**Files:**
- Create: `scripts/alchemist/checks.py`
- Test: `tests/test_checks_notation.py`

**Interfaces:**
- Consumes: `Corpus`, `Objects`, `Spend`, `load_corpus`, `load_objects` from Tasks 1 and 2.
- Produces: `Result(rule: str, failures: list[str], skipped: str | None)`, `check_declared_symbols_resolve(corpus, objects) -> Result`, `check_symbol_uniqueness_within_domain(objects) -> Result`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_checks_notation.py
from scripts.alchemist.checks import (
    check_declared_symbols_resolve,
    check_symbol_uniqueness_within_domain,
)
from scripts.alchemist.model import (
    Alias, Corpus, MathObject, Node, Objects, Spend,
)
from pathlib import Path


def node(node_id: str, domains, spends) -> Node:
    return Node(
        id=node_id, title=node_id, domains=tuple(domains), status="stub",
        requires=(), spends=tuple(spends), anchor=(), vault_articles=(),
        vault_sources=(), taught_in=None, body="", path=Path(f"nodes/{node_id}.md"),
    )


HAZARD = MathObject(
    id="obj.hazard", name="Hazard", canonical="h(t)", definition="d",
    aliases=(Alias("life", r"\mu_x", "force of mortality"),
             Alias("gi", r"\lambda", "claim intensity")),
)
INTENSITY_CLASH = MathObject(
    id="obj.other", name="Other", canonical="z", definition="d",
    aliases=(Alias("gi", r"\lambda", "something else"),),
)


def test_a_resolvable_spend_passes():
    corpus = Corpus(nodes={"n": node("n", ["life"], [Spend("obj.hazard", "life")])}, paths={})
    assert check_declared_symbols_resolve(corpus, Objects({"obj.hazard": HAZARD})).failures == []


def test_an_unknown_object_fails():
    """Asserts the message prefix, not just the object id. A bare
    `except LookupError` would also mention obj.ghost, because KeyError is a
    LookupError subclass, so an id-substring assertion passes under the very bug
    the explicit `not in objects.by_id` guard exists to prevent."""
    corpus = Corpus(nodes={"n": node("n", ["life"], [Spend("obj.ghost", "life")])}, paths={})
    result = check_declared_symbols_resolve(corpus, Objects({"obj.hazard": HAZARD}))
    assert len(result.failures) == 1
    assert "spends unknown object" in result.failures[0]
    assert "obj.ghost" in result.failures[0]


def test_spending_an_object_in_an_undeclared_domain_fails():
    """Covers check 1's third branch. Without this test, deleting the
    domain-membership guard leaves every other test green."""
    corpus = Corpus(nodes={"n": node("n", ["credit"], [Spend("obj.hazard", "life")])}, paths={})
    result = check_declared_symbols_resolve(corpus, Objects({"obj.hazard": HAZARD}))
    assert len(result.failures) == 1
    assert "not among its own domains" in result.failures[0]


def test_a_domain_with_no_alias_fails():
    corpus = Corpus(nodes={"n": node("n", ["credit"], [Spend("obj.hazard", "credit")])}, paths={})
    result = check_declared_symbols_resolve(corpus, Objects({"obj.hazard": HAZARD}))
    assert len(result.failures) == 1 and "no alias" in result.failures[0]


def test_two_spends_rendering_the_same_symbol_in_one_node_fails():
    corpus = Corpus(
        nodes={"n": node("n", ["gi"], [Spend("obj.hazard", "gi"), Spend("obj.other", "gi")])},
        paths={},
    )
    result = check_declared_symbols_resolve(
        corpus, Objects({"obj.hazard": HAZARD, "obj.other": INTENSITY_CLASH})
    )
    assert len(result.failures) == 1 and "both render" in result.failures[0]


def test_one_object_spelled_alike_in_two_domains_is_not_a_collision():
    """obj.survival is S(t) in both statistics and credit. That is one meaning,
    so keying the collision map on the symbol alone would fail a correct node."""
    twin = MathObject(
        id="obj.survival", name="Survival", canonical="S(t)", definition="d",
        aliases=(Alias("stats", "S(t)", "survival function"),
                 Alias("credit", "S(t)", "survival function")),
    )
    corpus = Corpus(
        nodes={"n": node("n", ["stats", "credit"],
                         [Spend("obj.survival", "stats"), Spend("obj.survival", "credit")])},
        paths={},
    )
    assert check_declared_symbols_resolve(corpus, Objects({"obj.survival": twin})).failures == []


def test_a_domain_with_one_symbol_on_two_objects_fails_globally():
    result = check_symbol_uniqueness_within_domain(
        Objects({"obj.hazard": HAZARD, "obj.other": INTENSITY_CLASH})
    )
    assert len(result.failures) == 1 and "gi" in result.failures[0]


def test_the_same_symbol_in_different_domains_is_fine():
    twin = MathObject(
        id="obj.twin", name="Twin", canonical="z", definition="d",
        aliases=(Alias("life", r"\lambda", "different domain"),),
    )
    assert check_symbol_uniqueness_within_domain(
        Objects({"obj.hazard": HAZARD, "obj.twin": twin})
    ).failures == []
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_checks_notation.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'scripts.alchemist.checks'`.

- [ ] **Step 3: Write the minimal implementation**

```python
# scripts/alchemist/checks.py
"""The seven rules. Each returns a Result, so the runner reports every failure in
one pass rather than stopping at the first.

Nothing here parses a node body. Matching an alias string against TeX is not
reliable: \\lambda occurs inside \\lambda(t), v inside \\varphi, and every short
alias inside something longer. Declaring what a node spends is exact instead, and
whether the body honours the declaration is a review responsibility.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from .model import Corpus, Objects


@dataclass
class Result:
    rule: str
    failures: list[str] = field(default_factory=list)
    skipped: str | None = None

    @property
    def ok(self) -> bool:
        return not self.failures


def check_declared_symbols_resolve(corpus: Corpus, objects: Objects) -> Result:
    result = Result("1. declared symbols resolve")
    for node in corpus.nodes.values():
        seen: dict[str, str] = {}
        for spend in node.spends:
            if spend.object not in objects.by_id:
                result.failures.append(
                    f"{node.id}: spends unknown object {spend.object!r}"
                )
                continue
            if spend.domain not in node.domains:
                result.failures.append(
                    f"{node.id}: spends {spend.object} in domain {spend.domain!r}, "
                    f"which is not among its own domains {list(node.domains)}"
                )
                continue
            try:
                symbol = objects.rendering(spend)
            except LookupError as exc:
                result.failures.append(f"{node.id}: {exc}")
                continue
            if symbol in seen and seen[symbol] != spend.object:
                result.failures.append(
                    f"{node.id}: {seen[symbol]} and {spend.object} both render "
                    f"as {symbol!r} in domain {spend.domain!r}"
                )
            seen[symbol] = spend.object
    return result


def check_symbol_uniqueness_within_domain(objects: Objects) -> Result:
    result = Result("2. one symbol per object within a domain")
    claims: dict[tuple[str, str], list[str]] = defaultdict(list)
    for obj in objects.by_id.values():
        for alias in obj.aliases:
            claims[(alias.domain, alias.symbol)].append(obj.id)
    for (domain, symbol), owners in sorted(claims.items()):
        if len(owners) > 1:
            result.failures.append(
                f"domain {domain!r}: {symbol!r} is claimed by {sorted(owners)}"
            )
    return result
```

Two points about check 1 that the naive reading gets wrong. First, a node that spends an object in a domain it does not itself declare is a failure, which stops a credit node quietly borrowing the life rendering. Second, the collision map keys on **object identity**, so one object spelled alike in two domains passes: `obj.survival` is `S(t)` in both statistics and credit, and that is one meaning rather than a collision. Keying on the symbol alone would fail `nodes/survival-function.md` in Task 11.

- [ ] **Step 4: Run the test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_checks_notation.py -v`
Expected: 8 passed.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(checks): verify declared symbols resolve and stay unique per domain"
```

---

### Task 4: Checks 3 and 4, the graph rules

**Files:**
- Modify: `scripts/alchemist/checks.py` (append)
- Test: `tests/test_checks_graph.py`

**Interfaces:**
- Consumes: `Result`, `Corpus`, `TeachingPath`.
- Produces: `check_requires_resolve_and_acyclic(corpus) -> Result`, `check_path_teachability(corpus) -> Result`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_checks_graph.py
from pathlib import Path

from scripts.alchemist.checks import (
    check_path_teachability,
    check_requires_resolve_and_acyclic,
)
from scripts.alchemist.model import Corpus, Node, TeachingPath


def node(node_id: str, requires=()) -> Node:
    return Node(
        id=node_id, title=node_id, domains=("stats",), status="stub",
        requires=tuple(requires), spends=(), anchor=(), vault_articles=(),
        vault_sources=(), taught_in=None, body="", path=Path(f"nodes/{node_id}.md"),
    )


def corpus(nodes, paths=()) -> Corpus:
    return Corpus({n.id: n for n in nodes}, {p.id: p for p in paths})


def test_a_resolvable_acyclic_graph_passes():
    c = corpus([node("a"), node("b", ["a"])])
    assert check_requires_resolve_and_acyclic(c).failures == []


def test_a_dangling_prerequisite_fails():
    result = check_requires_resolve_and_acyclic(corpus([node("b", ["ghost"])]))
    assert len(result.failures) == 1 and "ghost" in result.failures[0]


def test_a_cycle_fails_and_names_its_members():
    c = corpus([node("a", ["b"]), node("b", ["a"])])
    result = check_requires_resolve_and_acyclic(c)
    assert result.failures and "cycle" in result.failures[0]


def test_a_self_loop_fails():
    result = check_requires_resolve_and_acyclic(corpus([node("a", ["a"])]))
    assert result.failures and "cycle" in result.failures[0]


def test_a_path_with_prerequisites_in_order_passes():
    c = corpus(
        [node("a"), node("b", ["a"])],
        [TeachingPath("p", "P", (), "", ("a", "b"))],
    )
    assert check_path_teachability(c).failures == []


def test_a_path_with_a_prerequisite_later_fails():
    c = corpus(
        [node("a"), node("b", ["a"])],
        [TeachingPath("p", "P", (), "", ("b", "a"))],
    )
    result = check_path_teachability(c)
    assert len(result.failures) == 1 and "before" in result.failures[0]


def test_builds_on_supplies_the_prerequisite():
    c = corpus(
        [node("a"), node("b", ["a"])],
        [
            TeachingPath("base", "Base", (), "", ("a",)),
            TeachingPath("p", "P", ("base",), "", ("b",)),
        ],
    )
    assert check_path_teachability(c).failures == []


def test_builds_on_is_transitive():
    """`c` requires the grandparent's node as well as the parent's, so this passes
    only if the closure walks the whole chain. A one-level implementation supplies
    {"b"} alone and fails on "a"."""
    c = corpus(
        [node("a"), node("b", ["a"]), node("c", ["a", "b"])],
        [
            TeachingPath("one", "One", (), "", ("a",)),
            TeachingPath("two", "Two", ("one",), "", ("b",)),
            TeachingPath("three", "Three", ("two",), "", ("c",)),
        ],
    )
    assert check_path_teachability(c).failures == []


def test_a_builds_on_cycle_is_reported_rather_than_hanging():
    c = corpus(
        [node("a")],
        [
            TeachingPath("one", "One", ("two",), "", ("a",)),
            TeachingPath("two", "Two", ("one",), "", ()),
        ],
    )
    result = check_path_teachability(c)
    assert result.failures and "builds_on cycle" in result.failures[0]


def test_a_builds_on_cycle_between_other_paths_terminates():
    """Covers the `seen` guard, which the two-path cycle test above never reaches:
    there the cycle returns early on `nxt == path_id`. Here `x` sits outside the
    cycle, so only `seen` stops the frontier revisiting `two` forever. Dropping the
    guard makes this test hang rather than fail, which is the honest cost of
    testing termination without adding a timeout dependency."""
    c = corpus(
        [node("a")],
        [
            TeachingPath("x", "X", ("two",), "", ("a",)),
            TeachingPath("two", "Two", ("three",), "", ()),
            TeachingPath("three", "Three", ("two",), "", ()),
        ],
    )
    result = check_path_teachability(c)
    cycles = [f for f in result.failures if "builds_on cycle" in f]
    assert len(cycles) == 2
    assert not any(f.startswith("x:") for f in cycles)


def test_a_path_naming_an_unknown_node_fails():
    c = corpus([node("a")], [TeachingPath("p", "P", (), "", ("a", "ghost"))])
    result = check_path_teachability(c)
    assert any("ghost" in f for f in result.failures)
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_checks_graph.py -v`
Expected: FAIL, `ImportError: cannot import name 'check_requires_resolve_and_acyclic'`.

- [ ] **Step 3: Append the implementation**

```python
def check_requires_resolve_and_acyclic(corpus: Corpus) -> Result:
    result = Result("3. prerequisites resolve and the graph is acyclic")
    for node in corpus.nodes.values():
        for required in node.requires:
            if required not in corpus.nodes:
                result.failures.append(
                    f"{node.id}: requires unknown node {required!r}"
                )

    WHITE, GREY, BLACK = 0, 1, 2
    colour = dict.fromkeys(corpus.nodes, WHITE)

    def visit(node_id: str, trail: list[str]) -> None:
        if colour[node_id] == GREY:
            cycle = trail[trail.index(node_id):] + [node_id]
            result.failures.append("cycle: " + " -> ".join(cycle))
            return
        if colour[node_id] == BLACK:
            return
        colour[node_id] = GREY
        for required in corpus.nodes[node_id].requires:
            if required in colour:
                visit(required, trail + [node_id])
        colour[node_id] = BLACK

    for node_id in sorted(corpus.nodes):
        if colour[node_id] == WHITE:
            visit(node_id, [])
    return result


def check_path_teachability(corpus: Corpus) -> Result:
    """A node's prerequisites appear earlier in its own path, or anywhere in a
    path reachable through builds_on. Without the second clause every domain
    path would fail, since a life path does not restate the maths it assumes.
    """
    result = Result("4. every path is teachable in order")

    def inherited(path_id: str) -> set[str] | None:
        """Nodes supplied by the builds_on closure. None where that closure cycles."""
        seen: set[str] = set()
        frontier = list(corpus.paths[path_id].builds_on)
        while frontier:
            nxt = frontier.pop()
            if nxt == path_id:
                return None
            if nxt in seen or nxt not in corpus.paths:
                continue
            seen.add(nxt)
            frontier.extend(corpus.paths[nxt].builds_on)
        return {n for pid in seen for n in corpus.paths[pid].nodes}

    for path in sorted(corpus.paths.values(), key=lambda p: p.id):
        for referenced in path.builds_on:
            if referenced not in corpus.paths:
                result.failures.append(
                    f"{path.id}: builds_on unknown path {referenced!r}"
                )
        supplied = inherited(path.id)
        if supplied is None:
            result.failures.append(
                f"{path.id}: builds_on cycle reaches back to itself"
            )
            continue
        available = set(supplied)
        for node_id in path.nodes:
            node = corpus.nodes.get(node_id)
            if node is None:
                result.failures.append(f"{path.id}: unknown node {node_id!r}")
                continue
            for required in node.requires:
                if required not in available:
                    result.failures.append(
                        f"{path.id}: {node_id} needs {required!r} before it, and "
                        f"neither the path nor its builds_on closure supplies it"
                    )
            available.add(node_id)
    return result
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_checks_graph.py -v`
Expected: 11 passed.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(checks): verify graph acyclicity and path teachability"
```

---

### Task 5: Checks 5 and 6, the provenance rules

**Files:**
- Create: `sources/wanted.yaml` (with one worked entry and a header comment)
- Modify: `scripts/alchemist/checks.py` (append)
- Test: `tests/test_checks_sources.py`

**Interfaces:**
- Consumes: `Result`, `Corpus`.
- Produces: `vault_root() -> Path`, `check_publishable_citations(corpus, vault: Path) -> Result`, `check_gap_closure(corpus, root: Path) -> Result`. Both return `Result` with `skipped` set where the vault is absent.

- [ ] **Step 1: Seed the ledger**

```yaml
# Sources the corpus needs and the vault does not hold. One entry per document.
#
# The ledger drains rather than accumulates, because no node reaches
# status: reviewed while an open entry lists it in needed_by (check 6).
#
# acquisition: public-download | regulator | journal | purchased-personal
# status:      wanted | located | in-raw | ingested
#
# purchased-personal is a last resort. Where an entry uses it, it also records
# the public primary source those notes were distilled from, and that primary
# source is what the node eventually cites.
- id: ifoa-cm1-core-reading-2026
  needed_by: [compound-interest]
  claim: >
    The standard actuarial notation for annuity-certain values and the
    equation-of-value formulation.
  document: "IFoA CM1 Core Reading, 2026"
  url: null
  expected_tier: T4
  acquisition: purchased-personal
  primary_alternative: "McCutcheon and Scott, An Introduction to the Mathematics of Finance"
  status: wanted
```

- [ ] **Step 2: Write the failing test**

```python
# tests/test_checks_sources.py
from pathlib import Path

from scripts.alchemist.checks import check_gap_closure, check_publishable_citations
from scripts.alchemist.model import Corpus, Node

REGISTER = """---
id: {id}
confidentiality: {confidentiality}
publication_waiver: {waiver}
---
body
"""


def node(node_id: str, status="stub", sources=(), articles=()) -> Node:
    return Node(
        id=node_id, title=node_id, domains=("credit",), status=status,
        requires=(), spends=(), anchor=(), vault_articles=tuple(articles),
        vault_sources=tuple(sources), taught_in=None, body="",
        path=Path(f"nodes/{node_id}.md"),
    )


def fake_vault(tmp_path: Path, entries: dict[str, tuple[str, str]]) -> Path:
    registry = tmp_path / "wiki" / "_meta" / "sources"
    registry.mkdir(parents=True)
    for source_id, (confidentiality, waiver) in entries.items():
        (registry / f"{source_id}.md").write_text(
            REGISTER.format(id=source_id, confidentiality=confidentiality, waiver=waiver)
        )
    return tmp_path


def test_a_public_free_source_passes(tmp_path):
    vault = fake_vault(tmp_path, {"s1": ("public-free", "null")})
    c = Corpus({"n": node("n", sources=["s1"])}, {})
    assert check_publishable_citations(c, vault).failures == []


def test_a_public_paid_source_without_a_waiver_fails(tmp_path):
    vault = fake_vault(tmp_path, {"s1": ("public-paid", "null")})
    c = Corpus({"n": node("n", sources=["s1"])}, {})
    result = check_publishable_citations(c, vault)
    assert len(result.failures) == 1 and "public-paid" in result.failures[0]


def test_a_public_paid_source_with_a_waiver_passes(tmp_path):
    vault = fake_vault(tmp_path, {"s1": ("public-paid", "'granted 2026-09-01'")})
    c = Corpus({"n": node("n", sources=["s1"])}, {})
    assert check_publishable_citations(c, vault).failures == []


def test_a_source_missing_from_the_register_fails(tmp_path):
    vault = fake_vault(tmp_path, {})
    c = Corpus({"n": node("n", sources=["ghost"])}, {})
    result = check_publishable_citations(c, vault)
    assert len(result.failures) == 1 and "not in the vault register" in result.failures[0]


def test_an_absent_vault_skips_rather_than_fails(tmp_path):
    c = Corpus({"n": node("n", sources=["s1"])}, {})
    result = check_publishable_citations(c, tmp_path / "nowhere")
    assert result.failures == [] and result.skipped is not None


def test_a_paid_source_may_inform_through_vault_articles(tmp_path):
    """Check 5 walks `vault_sources` only. A paid source with no waiver can still
    inform a node through `vault_articles`, because the article lives in the
    private vault and the node's own prose is original. Mutating the loop to walk
    `vault_articles` as well would block purchased material from informing at all,
    which is the opposite of the intended rule. The value here is register-id
    shaped rather than slug shaped precisely so that such a mutant would resolve
    it and fail."""
    vault = fake_vault(tmp_path, {"paid": ("public-paid", "null")})
    c = Corpus({"n": node("n", articles=["paid"])}, {})
    assert check_publishable_citations(c, vault).failures == []


def test_an_absent_ledger_skips_rather_than_fails(tmp_path):
    c = Corpus({"n": node("n", status="reviewed")}, {})
    result = check_gap_closure(c, tmp_path / "nowhere")
    assert result.failures == [] and result.skipped is not None


def test_a_reviewed_node_with_an_open_gap_fails(tmp_path):
    (tmp_path / "sources").mkdir()
    (tmp_path / "sources" / "wanted.yaml").write_text(
        "- id: g1\n  needed_by: [n]\n  status: wanted\n"
    )
    c = Corpus({"n": node("n", status="reviewed")}, {})
    result = check_gap_closure(c, tmp_path)
    assert len(result.failures) == 1 and "g1" in result.failures[0]


def test_a_reviewed_node_whose_gap_is_ingested_passes(tmp_path):
    (tmp_path / "sources").mkdir()
    (tmp_path / "sources" / "wanted.yaml").write_text(
        "- id: g1\n  needed_by: [n]\n  status: ingested\n"
    )
    c = Corpus({"n": node("n", status="reviewed")}, {})
    assert check_gap_closure(c, tmp_path).failures == []


def test_a_stub_node_with_an_open_gap_passes(tmp_path):
    (tmp_path / "sources").mkdir()
    (tmp_path / "sources" / "wanted.yaml").write_text(
        "- id: g1\n  needed_by: [n]\n  status: wanted\n"
    )
    c = Corpus({"n": node("n", status="stub")}, {})
    assert check_gap_closure(c, tmp_path).failures == []
```

- [ ] **Step 3: Run the test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_checks_sources.py -v`
Expected: FAIL, `ImportError: cannot import name 'check_publishable_citations'`.

- [ ] **Step 4: Append the implementation**

Move the four import lines to the top of the file beside the existing imports, then append the
rest at the bottom. An append cannot introduce an import mid-module.

```python
# top of scripts/alchemist/checks.py, beside the existing imports
import os
from pathlib import Path

import yaml

from .model import FRONTMATTER, REPO

# bottom of the file
PUBLISHABLE = {"public-free"}


def vault_root() -> Path:
    """The vault is a separate private repo, so its location is configurable."""
    return Path(
        os.environ.get("ALCHEMIST_VAULT", Path.home() / "Documents" / "Repos" / "vault")
    ).expanduser()


def _register_entry(vault: Path, source_id: str) -> dict | None:
    path = vault / "wiki" / "_meta" / "sources" / f"{source_id}.md"
    if not path.is_file():
        return None
    match = FRONTMATTER.match(path.read_text())
    return yaml.safe_load(match.group(1)) if match else None


def check_publishable_citations(corpus: Corpus, vault: Path) -> Result:
    """This repo is public, so a quoted source has to be publishable.

    Purchased material can still inform a node through vault_articles, since
    the article lives in the private vault and the node's own prose is original.
    What it can never do is appear in vault_sources, which means the node quotes
    the primary text.
    """
    result = Result("5. quoted sources are publishable")
    if not (vault / "wiki" / "_meta" / "sources").is_dir():
        result.skipped = f"no vault register at {vault}"
        return result
    for node in corpus.nodes.values():
        for source_id in node.vault_sources:
            entry = _register_entry(vault, source_id)
            if entry is None:
                result.failures.append(
                    f"{node.id}: {source_id!r} is not in the vault register"
                )
                continue
            confidentiality = entry.get("confidentiality")
            if confidentiality in PUBLISHABLE:
                continue
            if confidentiality == "public-paid" and entry.get("publication_waiver"):
                continue
            result.failures.append(
                f"{node.id}: quotes {source_id!r}, which is {confidentiality!r} "
                f"with no publication waiver, and this repo is public"
            )
    return result


def check_gap_closure(corpus: Corpus, root: Path = REPO) -> Result:
    result = Result("6. no reviewed node carries an open source gap")
    ledger = root / "sources" / "wanted.yaml"
    if not ledger.is_file():
        result.skipped = f"no ledger at {ledger}"
        return result
    for entry in yaml.safe_load(ledger.read_text()) or []:
        if entry.get("status") == "ingested":
            continue
        for node_id in entry.get("needed_by") or []:
            node = corpus.nodes.get(node_id)
            if node is not None and node.status == "reviewed":
                result.failures.append(
                    f"{node_id}: reviewed, but gap {entry['id']!r} is still "
                    f"{entry.get('status')!r}"
                )
    return result
```

- [ ] **Step 5: Run the test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_checks_sources.py -v`
Expected: 10 passed.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(checks): gate quoted sources on publishability and gap closure"
```

---

### Task 6: The symbol table generator and check 7

**Files:**
- Create: `scripts/alchemist/site.py`
- Modify: `scripts/alchemist/checks.py` (append)
- Test: `tests/test_site.py`

**Interfaces:**
- Consumes: `Objects`, `Corpus`, `Result`.
- Produces: `render_symbols(objects: Objects) -> str`, `check_generated_current(objects, root: Path) -> Result`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_site.py
from scripts.alchemist.checks import check_generated_current
from scripts.alchemist.model import Alias, MathObject, Objects
from scripts.alchemist.site import render_symbols

HAZARD = MathObject(
    id="obj.hazard", name="Hazard rate", canonical="h(t)",
    definition="The instantaneous rate of the event.",
    aliases=(Alias("life", r"\mu_x", "force of mortality", "age-indexed"),
             Alias("gi", r"\lambda", "claim intensity")),
)
OBJECTS = Objects({"obj.hazard": HAZARD})


def test_the_table_carries_the_object_its_domains_and_its_note():
    out = render_symbols(OBJECTS)
    assert "Hazard rate" in out
    assert r"$\mu_x$" in out and "force of mortality" in out
    assert "age-indexed" in out
    assert "generated" in out.lower()


def test_objects_are_rendered_in_id_order():
    """Asserts the ordering itself rather than merely that two calls agree.
    Within one process a dict walks in insertion order deterministically, so a
    calls-agree assertion passes with `sorted()` removed, which is the mutation
    this test exists to catch."""
    later = MathObject(
        id="obj.zeta", name="Zeta", canonical="z", definition="d",
        aliases=(Alias("stats", "z", "zeta"),),
    )
    unsorted = Objects({"obj.zeta": later, "obj.hazard": HAZARD})
    out = render_symbols(unsorted)
    assert out.index("Hazard rate") < out.index("Zeta")


def test_check_7_passes_when_the_file_matches(tmp_path):
    (tmp_path / "notation").mkdir()
    (tmp_path / "notation" / "symbols.md").write_text(render_symbols(OBJECTS))
    assert check_generated_current(OBJECTS, tmp_path).failures == []


def test_check_7_fails_when_the_file_has_drifted(tmp_path):
    (tmp_path / "notation").mkdir()
    (tmp_path / "notation" / "symbols.md").write_text("# stale\n")
    result = check_generated_current(OBJECTS, tmp_path)
    assert len(result.failures) == 1
    # "drifted", not "build_site": both messages name build_site.py, so matching
    # on that would pass even if the drifted case emitted the missing message.
    assert "drifted" in result.failures[0]


def test_check_7_fails_when_the_file_is_missing(tmp_path):
    (tmp_path / "notation").mkdir()
    result = check_generated_current(OBJECTS, tmp_path)
    assert len(result.failures) == 1 and "missing" in result.failures[0]
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_site.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'scripts.alchemist.site'`.

- [ ] **Step 3: Write the implementation**

```python
# scripts/alchemist/site.py
"""Every generated artefact. Nothing here is hand-edited, and check 7 verifies
that what is committed matches what this module would produce.
"""

from __future__ import annotations

from pathlib import Path

from .model import Objects

BANNER = (
    "<!-- Generated by scripts/build_site.py from notation/objects.yaml.\n"
    "     Do not edit. Edit objects.yaml and rebuild. -->\n"
)


def render_symbols(objects: Objects) -> str:
    lines = [
        BANNER,
        "# Symbol table",
        "",
        "One meaning per object. A domain keeps its own notation, so the same object",
        "appears under several symbols and a reader crossing domains can see which",
        "spellings refer to the same thing.",
        "",
    ]
    for obj in sorted(objects.by_id.values(), key=lambda o: o.id):
        lines += [
            f"## {obj.name}",
            "",
            f"`{obj.id}`, canonically ${obj.canonical}$. {obj.definition}",
            "",
            "| Domain | Symbol | Called | Note |",
            "|---|---|---|---|",
        ]
        for alias in obj.aliases:
            lines.append(
                f"| {alias.domain} | ${alias.symbol}$ | {alias.name} "
                f"| {alias.note or ''} |"
            )
        lines.append("")
    return "\n".join(lines)
```

Append to `scripts/alchemist/checks.py`, and add `from .site import render_symbols` to the
top of that file. There is no circular import to avoid, since `site.py` imports from
`model.py` only and never from `checks.py`.

```python
def check_generated_current(objects: Objects, root: Path = REPO) -> Result:
    """A committed build artefact drifts unless something checks it."""
    result = Result("7. generated artefacts are current")
    target = root / "notation" / "symbols.md"
    if not target.is_file():
        result.failures.append(f"{target} is missing; run build_site.py")
        return result
    if target.read_text() != render_symbols(objects):
        result.failures.append(
            f"{target} has drifted from objects.yaml; run build_site.py"
        )
    return result
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_site.py -v`
Expected: 5 passed.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(site): generate the symbol table and check it has not drifted"
```

---

### Task 7: The two command-line entry points

**Files:**
- Create: `scripts/check.py`, `scripts/build_site.py`
- Modify: `scripts/alchemist/checks.py` (append the runner), `scripts/alchemist/site.py` (append the index, path pages and graph)
- Test: `tests/test_cli.py`

**Interfaces:**
- Consumes: everything above.
- Produces: `run_all(corpus, objects, root, vault) -> list[Result]`; `render_index(corpus) -> str`; `render_path_page(path, corpus) -> str`; `render_node_page(node, corpus, objects) -> str`; `render_domain_dot(corpus, domain) -> str`; `build(root: Path) -> list[Path]`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_cli.py
import subprocess
import sys
from pathlib import Path

from scripts.alchemist.model import (
    Alias, Corpus, MathObject, Node, Objects, Spend, TeachingPath,
)
from scripts.alchemist.site import (
    render_domain_dot, render_index, render_node_page, render_path_page,
)

REPO = Path(__file__).resolve().parents[1]


def node(node_id: str, requires=(), domains=("stats",), taught_in=None) -> Node:
    return Node(
        id=node_id, title=node_id.replace("-", " ").capitalize(), domains=domains,
        status="stub", requires=tuple(requires), spends=(), anchor=(),
        vault_articles=(), vault_sources=(), taught_in=taught_in, body="",
        path=Path(f"nodes/{node_id}.md"),
    )


def test_the_index_lists_every_path_and_counts_the_nodes():
    """The corpus holds three nodes while the path lists two, so the per-path count
    and the summary total are different strings. With them equal, deleting the
    per-path count entirely still passes, because the summary sentence supplies
    the same text. The third node also covers the "taught in full" figure, which
    otherwise has no test at all."""
    corpus = Corpus(
        {
            "a": node("a"),
            "b": node("b", ["a"]),
            "c": node("c", taught_in="S1_credit-survival-bridge"),
        },
        {"p": TeachingPath("p", "A path", (), "Why.", ("a", "b"))},
    )
    out = render_index(corpus)
    assert "A path" in out
    assert "2 nodes" in out                      # the path's own count
    assert "3 nodes" in out                      # the corpus summary
    assert "1 of them taught in full" in out


def test_a_path_page_lists_its_nodes_in_order_and_marks_the_taught_ones():
    corpus = Corpus(
        {"a": node("a", taught_in="S1_credit-survival-bridge"), "b": node("b", ["a"])},
        {"p": TeachingPath("p", "A path", (), "Why.", ("a", "b"))},
    )
    out = render_path_page(corpus.paths["p"], corpus)
    assert out.index("../nodes/a.html") < out.index("../nodes/b.html")
    assert "S1_credit-survival-bridge" in out


def test_a_node_page_carries_the_body_the_aliases_and_what_it_unlocks():
    hazard = MathObject(
        id="obj.hazard", name="Hazard rate", canonical="h(t)", definition="d",
        aliases=(Alias("life", r"\mu_x", "force of mortality"),
                 Alias("credit", "h(t)", "default hazard")),
    )
    root = Node(
        id="survival-function", title="Survival function", domains=("life", "credit"),
        status="drafted", requires=(), spends=(Spend("obj.hazard", "life"),
                                              Spend("obj.hazard", "credit")),
        anchor=(), vault_articles=("methods/deep-learning-credit-scoring",),
        vault_sources=(), taught_in=None, body="## Definition\n\nThe probability of no event.\n",
        path=Path("nodes/survival-function.md"),
    )
    corpus = Corpus({"survival-function": root, "hazard-rate": node("hazard-rate", ["survival-function"])}, {})
    out = render_node_page(root, corpus, Objects({"obj.hazard": hazard}))
    assert "The probability of no event." in out
    assert "force of mortality" in out and "default hazard" in out
    assert "hazard-rate" in out
    assert "methods/deep-learning-credit-scoring" in out


def test_a_node_page_omits_the_alias_table_where_one_domain_is_spent():
    hazard = MathObject(
        id="obj.hazard", name="Hazard rate", canonical="h(t)", definition="d",
        aliases=(Alias("credit", "h(t)", "default hazard"),),
    )
    only = Node(
        id="a", title="A", domains=("credit",), status="stub", requires=(),
        spends=(Spend("obj.hazard", "credit"),), anchor=(), vault_articles=(),
        vault_sources=(), taught_in=None, body="x\n", path=Path("nodes/a.md"),
    )
    out = render_node_page(only, Corpus({"a": only}, {}), Objects({"obj.hazard": hazard}))
    assert "Called in each domain" not in out


def test_the_dot_graph_carries_one_edge_per_prerequisite():
    corpus = Corpus({"a": node("a"), "b": node("b", ["a"])}, {})
    dot = render_domain_dot(corpus, "stats")
    assert '"a" -> "b"' in dot and dot.startswith("digraph")


def test_the_dot_graph_excludes_other_domains():
    corpus = Corpus(
        {"a": node("a", domains=("life",)), "b": node("b", ["a"], domains=("stats",))},
        {},
    )
    dot = render_domain_dot(corpus, "stats")
    assert '"b"' in dot and '"a" -> "b"' not in dot


def test_check_py_exits_zero_on_the_real_repo():
    done = subprocess.run(
        [sys.executable, "scripts/check.py"], cwd=REPO, capture_output=True, text=True
    )
    assert done.returncode == 0, done.stdout + done.stderr


def test_check_py_exits_non_zero_when_a_rule_fails(tmp_path):
    (tmp_path / "nodes").mkdir()
    (tmp_path / "paths").mkdir()
    (tmp_path / "notation").mkdir()
    (tmp_path / "nodes" / "b.md").write_text(
        "---\nid: b\ntitle: B\ndomains: [stats]\nstatus: stub\nrequires: [ghost]\n---\n\nx\n"
    )
    (tmp_path / "notation" / "objects.yaml").write_text("[]\n")
    (tmp_path / "notation" / "symbols.md").write_text("wrong\n")
    done = subprocess.run(
        [sys.executable, str(REPO / "scripts" / "check.py"), "--root", str(tmp_path)],
        capture_output=True, text=True, cwd=REPO,
    )
    assert done.returncode == 1 and "ghost" in done.stdout
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_cli.py -v`
Expected: FAIL, `ImportError: cannot import name 'render_index'`.

- [ ] **Step 3: Append the generators to `scripts/alchemist/site.py`**

```python
HEAD = """<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{css}">
</head><body>
"""


def render_index(corpus: Corpus) -> str:
    rows = []
    for path in sorted(corpus.paths.values(), key=lambda p: p.id):
        rows.append(
            f'<li><a href="paths/{path.id}.html">{path.title}</a> '
            f"<span>{len(path.nodes)} nodes</span></li>"
        )
    taught = sum(1 for n in corpus.nodes.values() if n.taught_in)
    return (
        HEAD.format(title="Alchemist", css="assets/lecture.css")
        + "<h1>Alchemist</h1>\n"
        + f"<p>{len(corpus.nodes)} nodes, {taught} of them taught in full, "
        + f"across {len(corpus.paths)} paths.</p>\n"
        + "<ul>\n" + "\n".join(rows) + "\n</ul>\n</body></html>\n"
    )


def render_path_page(path, corpus: Corpus) -> str:
    rows = []
    for node_id in path.nodes:
        node = corpus.nodes[node_id]
        lecture = (
            f' <a href="../lectures/{node.taught_in}.html">lecture</a>'
            if node.taught_in else ""
        )
        rows.append(
            f'<li><a href="../nodes/{node.id}.html">{node.title}</a>{lecture}</li>'
        )
    return (
        HEAD.format(title=path.title, css="../assets/lecture.css")
        + f"<h1>{path.title}</h1>\n<p>{path.preamble}</p>\n"
        + "<ol>\n" + "\n".join(rows) + "\n</ol>\n</body></html>\n"
    )


# Path pages live in site/paths/ and node pages in site/nodes/, so a path page
# reaches a node page as ../nodes/<id>.html. Keep the two directories siblings.


def render_node_page(node, corpus: Corpus, objects: Objects) -> str:
    """A tier-1 page: the author's three written sections, then three generated
    tails. Splitting it this way is what keeps a Phase 3 agent's job to three
    short pieces of prose, and it means the alias table, the unlocks list and
    the sources can never fall out of step with the graph.
    """
    from markdown_it import MarkdownIt

    parts = [
        HEAD.format(title=node.title, css="../assets/lecture.css"),
        f"<h1>{node.title}</h1>",
        MarkdownIt().render(node.body),
    ]

    if len({s.domain for s in node.spends}) > 1:
        rows = []
        for spend in node.spends:
            alias = objects.by_id[spend.object].for_domain(spend.domain)
            rows.append(
                f"<tr><td>{spend.domain}</td><td>${alias.symbol}$</td>"
                f"<td>{alias.name}</td></tr>"
            )
        parts += [
            "<h2>Called in each domain</h2>",
            "<table><thead><tr><th>Domain</th><th>Symbol</th><th>Called</th>"
            "</tr></thead><tbody>" + "".join(rows) + "</tbody></table>",
        ]

    unlocks = sorted(o.id for o in corpus.nodes.values() if node.id in o.requires)
    if unlocks:
        links = "".join(f'<li><a href="{u}.html">{u}</a></li>' for u in unlocks)
        parts += ["<h2>What this unlocks</h2>", f"<ul>{links}</ul>"]

    if node.vault_articles or node.vault_sources:
        items = "".join(
            f"<li>{ref}</li>" for ref in (*node.vault_articles, *node.vault_sources)
        )
        parts += ["<h2>Sources</h2>", f"<ul>{items}</ul>"]

    return "\n".join(parts) + "\n</body></html>\n"


def render_domain_dot(corpus: Corpus, domain: str) -> str:
    """One graph per domain. An edge is drawn only where both ends sit in the
    domain, so a domain view stays readable rather than dragging in every root.
    """
    members = {n.id for n in corpus.nodes.values() if domain in n.domains}
    lines = [
        "digraph alchemist {",
        '  rankdir=LR; node [shape=box, fontname="Helvetica", fontsize=10];',
    ]
    for node_id in sorted(members):
        lines.append(f'  "{node_id}" [label="{corpus.nodes[node_id].title}"];')
    for node_id in sorted(members):
        for required in sorted(corpus.nodes[node_id].requires):
            if required in members:
                lines.append(f'  "{required}" -> "{node_id}";')
    lines.append("}")
    return "\n".join(lines) + "\n"


def build(root: Path = REPO) -> list[Path]:
    """Write every generated artefact and return what was written."""
    corpus, objects = load_corpus(root), load_objects(root)
    written: list[Path] = []

    symbols = root / "notation" / "symbols.md"
    symbols.write_text(render_symbols(objects))
    written.append(symbols)

    index = root / "index.html"
    index.write_text(render_index(corpus))
    written.append(index)

    pages = root / "site" / "paths"
    pages.mkdir(parents=True, exist_ok=True)
    for path in corpus.paths.values():
        target = pages / f"{path.id}.html"
        target.write_text(render_path_page(path, corpus))
        written.append(target)

    node_pages = root / "site" / "nodes"
    node_pages.mkdir(parents=True, exist_ok=True)
    for node in corpus.nodes.values():
        target = node_pages / f"{node.id}.html"
        target.write_text(render_node_page(node, corpus, objects))
        written.append(target)

    graphs = root / "site" / "graphs"
    graphs.mkdir(parents=True, exist_ok=True)
    domains = {d for n in corpus.nodes.values() for d in n.domains}
    for domain in sorted(domains):
        svg = graphs / f"{domain}.svg"
        subprocess.run(
            ["dot", "-Tsvg", "-o", str(svg)],
            input=render_domain_dot(corpus, domain), text=True, check=True,
        )
        written.append(svg)
    return written
```

Extend `site.py`'s import line to `from .model import REPO, Corpus, Objects`, re-add
`from pathlib import Path` (Task 6 correctly removed it as unused, and `build()` and
`render_node_page` need it for their annotations), and move `import subprocess` and
`from .model import load_corpus, load_objects` from inside `build()` to the top of the file
beside them. Neither local import avoids a cycle, so neither is justified.

- [ ] **Step 4: Append the runner to `scripts/alchemist/checks.py`**

```python
def run_all(corpus: Corpus, objects: Objects, root: Path, vault: Path) -> list[Result]:
    return [
        check_declared_symbols_resolve(corpus, objects),
        check_symbol_uniqueness_within_domain(objects),
        check_requires_resolve_and_acyclic(corpus),
        check_path_teachability(corpus),
        check_publishable_citations(corpus, vault),
        check_gap_closure(corpus, root),
        check_generated_current(objects, root),
    ]
```

- [ ] **Step 5: Write the two entry points**

```python
# scripts/check.py
"""Run every rule over the corpus. Exit 1 on any failure."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.checks import run_all, vault_root
from scripts.alchemist.model import load_corpus, load_objects


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    corpus = load_corpus(args.root)
    objects = load_objects(args.root)
    results = run_all(corpus, objects, args.root, vault_root())

    failed = 0
    for result in results:
        if result.skipped:
            print(f"SKIP  {result.rule}: {result.skipped}")
        elif result.ok:
            print(f"ok    {result.rule}")
        else:
            failed += len(result.failures)
            print(f"FAIL  {result.rule}")
            for failure in result.failures:
                print(f"        {failure}")
    print(f"\n{len(corpus.nodes)} nodes, {len(corpus.paths)} paths, {failed} failures")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

```python
# scripts/build_site.py
"""Write every generated artefact, then verify the checks still pass."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.site import build


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    for written in build(args.root):
        print(written.relative_to(args.root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 6: Generate, then run every test**

```bash
.venv/bin/python scripts/build_site.py
.venv/bin/python -m pytest -v
```

Expected: all tests pass, including `test_check_py_exits_zero_on_the_real_repo`. The repo has no nodes yet, so an empty corpus passing is the correct result.

- [ ] **Step 7: Commit**

```bash
git add -A
git commit -m "feat(cli): add check and build entry points with path and graph pages"
```

- [ ] **Step 8: Escape author-supplied text and fix the relative paths**

Every generator above interpolates author-supplied strings straight into markup, and three
relative paths are wrong. Both were defects in this plan's own code, found at review.

Escaping matters here specifically because the corpus is mathematical and the repo is public:
"PD < 1%" is ordinary prose in credit risk, and it corrupts a page the first time real content
lands. A double quote in a node title is worse, because a DOT label is a quoted string, so `dot`
fails on the rest of the line.

Add `import html` at the top of `site.py` and these two helpers after `BANNER`:

```python
def _esc(text: str) -> str:
    """Escape author-supplied text for HTML. Titles and preambles are prose from a
    mathematical corpus, so "PD < 1%" is ordinary rather than exotic, and this
    repo is public.
    """
    return html.escape(str(text), quote=True)


def _dot_label(text: str) -> str:
    """A DOT label is a quoted string, so a double quote in a title would end it
    early. Backslash first, or the escapes escape each other.
    """
    return text.replace("\\", "\\\\").replace('"', '\\"')
```

Then apply them, and correct the paths:

1. `render_index`: wrap `path.title` in `_esc(...)`, and `path.id` too, since `parse_path` does
   not slug-validate an id the way `parse_node` does.
2. `render_path_page`: wrap `path.title`, `path.preamble`, `node.title`, `node.id` and
   `node.taught_in` in `_esc(...)`. Change the stylesheet from `../assets/lecture.css` to
   `../../assets/lecture.css`, and the lecture link from `../lectures/` to `../../lectures/`.
   A page in `site/paths/` is two levels below the root, so `../assets/` resolves to
   `site/assets/`, which nothing ever creates, and `../lectures/` to `site/lectures/`, likewise.
3. `render_node_page`: wrap `node.title`, `alias.symbol`, `alias.name`, `spend.domain`, each
   unlock id and each vault reference in `_esc(...)`. Change the stylesheet to
   `../../assets/lecture.css`. The unlock links stay `{u}.html`, since node pages are siblings.
4. `render_domain_dot`: wrap the label in `_dot_label(...)`.
5. `build()`: wrap the `subprocess.run(["dot", ...])` call so a missing binary is actionable.
   `check=True` converts a non-zero exit into `CalledProcessError` and does nothing for the
   `FileNotFoundError` a missing executable raises:

```python
        try:
            subprocess.run(
                ["dot", "-Tsvg", "-o", str(svg)],
                input=render_domain_dot(corpus, domain), text=True, check=True,
            )
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                "graphviz is not on PATH, so the domain graphs cannot be drawn. "
                "Install it, for example with `brew install graphviz`."
            ) from exc
```

6. `scripts/build_site.py`: its docstring claims "then verify the checks still pass", which
   `main()` never does. Change it to `"""Write every generated artefact."""` so a reader does
   not skip running `check.py`.

Then add three tests to `tests/test_cli.py`:

```python
def test_author_supplied_text_is_escaped():
    """"PD < 1%" is ordinary prose in this corpus and the repo is public, so an
    unescaped title corrupts the page the first time real content lands."""
    corpus = Corpus(
        {"a": node("a")},
        {"p": TeachingPath("p", "PD < 1% & rising", (), "See <b>this</b>.", ("a",))},
    )
    index = render_index(corpus)
    page = render_path_page(corpus.paths["p"], corpus)
    assert "PD &lt; 1% &amp; rising" in index
    assert "PD < 1% & rising" not in index
    assert "&lt;b&gt;this&lt;/b&gt;" in page
    assert "<b>this</b>" not in page


def test_a_quote_in_a_title_does_not_break_the_dot_label():
    """A DOT label is a quoted string, so an unescaped double quote ends the
    label early and `dot` fails on the rest of the line."""
    quoted = Node(
        id="a", title='The "ultimate" claim', domains=("stats",), status="stub",
        requires=(), spends=(), anchor=(), vault_articles=(), vault_sources=(),
        taught_in=None, body="", path=Path("nodes/a.md"),
    )
    dot = render_domain_dot(Corpus({"a": quoted}, {}), "stats")
    assert '\\"ultimate\\"' in dot


def test_pages_below_site_reach_the_repo_root():
    """A page in site/paths/ is two levels below the root, so ../assets/ would
    resolve to site/assets/, which nothing ever creates."""
    corpus = Corpus(
        {"a": node("a", taught_in="S1_credit-survival-bridge")},
        {"p": TeachingPath("p", "P", (), "", ("a",))},
    )
    page = render_path_page(corpus.paths["p"], corpus)
    assert "../../assets/lecture.css" in page
    assert "../../lectures/S1_credit-survival-bridge.html" in page
```

Run: `.venv/bin/python scripts/build_site.py && .venv/bin/python -m pytest -v`
Expected: 11 in `test_cli.py`, 55 in the suite. Regenerate the site before the suite, because
`index.html` is committed and escaping changes its bytes once the corpus carries author-supplied
text. With the corpus still empty in Phase 0 the bytes will not change, which is expected
rather than a sign the escaping did nothing.

- [ ] **Step 9: Commit**

```bash
git add -A
git commit -m "fix(site): escape author-supplied text and correct the relative paths"
```

---

### Task 8: Vendor KaTeX and inline the assets

**Files:**
- Create: `vendor/katex/katex.min.js`, `vendor/katex/katex.min.css`, `vendor/katex/fonts/`
- Create: `scripts/katex_embed_fonts.py`, `scripts/inline_assets.py`
- Create: `assets/lecture.css` (copied from the trunk repo)
- Test: `tests/test_inline_assets.py`

**Interfaces:**
- Consumes: nothing from earlier tasks.
- Produces: `inline(html_path: Path, root: Path) -> int` returning the number of assets inlined.

- [ ] **Step 1: Vendor KaTeX at a pinned version and copy the stylesheet**

```bash
cd ~/Documents/Repos/alchemist
KATEX=0.16.11
curl -fsSL "https://github.com/KaTeX/KaTeX/releases/download/v${KATEX}/katex.tar.gz" -o /tmp/katex.tar.gz
tar -xzf /tmp/katex.tar.gz -C /tmp
mkdir -p vendor/katex
cp /tmp/katex/katex.min.js /tmp/katex/katex.min.css vendor/katex/
cp -R /tmp/katex/fonts vendor/katex/fonts
echo "${KATEX}" > vendor/katex/VERSION
cp ../actuarial_deep_learning/lectures/lecture.css assets/lecture.css
du -sh vendor/katex
```

0.16.11 matches the version the `guides` lectures already used, so nothing regresses against a corpus you have read.

- [ ] **Step 2: Embed the fonts into the stylesheet, once**

```python
# scripts/katex_embed_fonts.py
"""Rewrite vendor/katex/katex.min.css so its font URLs are base64 data URIs.

Run once after vendoring a new KaTeX. A single-file lecture needs the fonts
inside the CSS, because inlining a stylesheet that points at fonts/ by relative
URL yields a page whose mathematics renders in a fallback face.

Only the woff2 faces are embedded. KaTeX also ships woff and ttf for older
browsers, and carrying all three would treble the payload for no reader we have.
"""

import base64
import re
from pathlib import Path

VENDOR = Path(__file__).resolve().parents[1] / "vendor" / "katex"
URL = re.compile(r"url\((fonts/[^)]+\.woff2)\)")


def main() -> int:
    css = VENDOR / "katex.min.css"
    text = css.read_text()

    def embed(match: re.Match[str]) -> str:
        data = (VENDOR / match.group(1)).read_bytes()
        encoded = base64.b64encode(data).decode("ascii")
        return f"url(data:font/woff2;base64,{encoded})"

    rewritten, count = URL.subn(embed, text)
    # Drop the woff and ttf sources, which now sit after a data URI that always wins.
    rewritten = re.sub(r",\s*url\(fonts/[^)]+\.(?:woff|ttf)\)\s*format\([^)]+\)", "", rewritten)
    css.write_text(rewritten)
    print(f"embedded {count} woff2 faces into {css.name}, now {len(rewritten):,} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

Run it, then verify:

```bash
.venv/bin/python scripts/katex_embed_fonts.py
grep -c "url(fonts/" vendor/katex/katex.min.css   # expect 0
```

- [ ] **Step 3: Write the failing test**

```python
# tests/test_inline_assets.py
from pathlib import Path

import pytest

from scripts.inline_assets import inline

PAGE = """<!doctype html>
<html><head>
<link rel="stylesheet" href="../vendor/katex/katex.min.css">
<link rel="stylesheet" href="../assets/lecture.css">
<script defer src="../vendor/katex/katex.min.js"></script>
</head><body><p>$x$</p></body></html>
"""


def fake_repo(tmp_path: Path) -> Path:
    (tmp_path / "vendor" / "katex").mkdir(parents=True)
    (tmp_path / "assets").mkdir()
    (tmp_path / "lectures").mkdir()
    (tmp_path / "vendor" / "katex" / "katex.min.css").write_text(".katex{}")
    (tmp_path / "vendor" / "katex" / "katex.min.js").write_text("var katex={};")
    (tmp_path / "assets" / "lecture.css").write_text("body{}")
    (tmp_path / "lectures" / "L.html").write_text(PAGE)
    return tmp_path


def test_all_three_assets_are_inlined(tmp_path):
    root = fake_repo(tmp_path)
    assert inline(root / "lectures" / "L.html", root) == 3


def test_no_external_reference_survives(tmp_path):
    root = fake_repo(tmp_path)
    inline(root / "lectures" / "L.html", root)
    out = (root / "lectures" / "L.html").read_text()
    assert "href=" not in out and "src=" not in out
    assert ".katex{}" in out and "body{}" in out and "var katex={}" in out


def test_it_is_idempotent(tmp_path):
    root = fake_repo(tmp_path)
    target = root / "lectures" / "L.html"
    inline(target, root)
    once = target.read_text()
    assert inline(target, root) == 0
    assert target.read_text() == once


def test_a_missing_asset_raises_rather_than_silently_skipping(tmp_path):
    """Raising is half the property. The other half is that nothing was written:
    a half-inlined lecture that also raised would leave a corrupt file for the
    next step in the chain to print."""
    root = fake_repo(tmp_path)
    target = root / "lectures" / "L.html"
    before = target.read_text()
    (root / "assets" / "lecture.css").unlink()
    with pytest.raises(FileNotFoundError, match="lecture.css"):
        inline(target, root)
    assert target.read_text() == before
```

- [ ] **Step 4: Run the test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_inline_assets.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'scripts.inline_assets'`.

- [ ] **Step 5: Write the implementation**

```python
# scripts/inline_assets.py
"""Inline our own three assets into a rendered lecture, so the file is
self-contained and opens from a bare disk with no network.

Quarto's own embed-resources: true is not used, because it inlines Quarto's
theme assets too, and render_lecture.sh removes those by matching link and
script tags that point into _files/libs/. Inlining defeats that strip. Doing it
ourselves afterwards reaches the same single file and leaves the strip working.

Raises rather than skips on a missing asset: a lecture that quietly lost its
stylesheet still renders, just wrongly, which is the failure mode this whole
pipeline exists to avoid.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LINK = re.compile(r'[ \t]*<link[^>]*href="([^"]+\.css)"[^>]*>\n?')
SCRIPT = re.compile(r'[ \t]*<script[^>]*src="([^"]+\.js)"[^>]*>\s*</script>\n?')


def _resolve(reference: str, html_path: Path, root: Path) -> Path:
    candidate = (html_path.parent / reference).resolve()
    if not candidate.is_file():
        raise FileNotFoundError(f"{html_path}: cannot find {reference}")
    if root.resolve() not in candidate.parents:
        raise ValueError(f"{html_path}: {reference} escapes the repo")
    return candidate


def inline(html_path: Path, root: Path) -> int:
    text = html_path.read_text()
    count = 0

    def css(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        body = _resolve(match.group(1), html_path, root).read_text()
        return f"<style>\n{body}\n</style>\n"

    def js(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        body = _resolve(match.group(1), html_path, root).read_text()
        return f"<script>\n{body}\n</script>\n"

    text = LINK.sub(css, text)
    text = SCRIPT.sub(js, text)
    if count:
        html_path.write_text(text)
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, nargs="+")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    for html in args.html:
        print(f"inlined {inline(html, args.root)} assets into {html}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 6: Run the test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_inline_assets.py -v`
Expected: 4 passed.

- [ ] **Step 7: Commit**

```bash
git add -A
git commit -m "feat(render): vendor katex with embedded fonts and inline lecture assets"
```

---

### Task 9: The render and print chain

**Files:**
- Create: `scripts/render_lecture.sh`, `scripts/html_to_pdf.sh`
- Test: `tests/test_render_chain.py`

**Interfaces:**
- Consumes: `scripts/inline_assets.py` from Task 8.
- Produces: two shell entry points. `render_lecture.sh <file.qmd>...` writes `<file>.html`; `html_to_pdf.sh <file.html>...` writes `<file>.pdf`.

- [ ] **Step 1: Copy both scripts and apply the four changes**

```bash
cd ~/Documents/Repos/alchemist
cp ../actuarial_deep_learning/scripts/render_lecture.sh scripts/
cp ../actuarial_deep_learning/scripts/html_to_pdf.sh scripts/
chmod +x scripts/render_lecture.sh scripts/html_to_pdf.sh
```

Then edit them. The four changes, and nothing else, because the rest of both scripts encodes traps that were paid for once already:

1. In `render_lecture.sh`, after the figure relocation block and inside the `for` loop, add the inline step:

```bash
  .venv/bin/python scripts/inline_assets.py "$html"
```

2. In `render_lecture.sh`, replace the header comment sentence "MathJax loads from its CDN and is untouched." with "KaTeX loads from `vendor/katex/` and is inlined afterwards by `scripts/inline_assets.py`, so the output carries no network dependency."

3. In `render_lecture.sh`, replace the two-directory discussion in the header comment with: "One directory goes through here, `lectures/`. Paths are required rather than defaulted, because the lectures execute Python against the gitignored credit parquets, so a sweep on a fresh clone would fail partway through on missing data rather than on the lecture asked for."

4. In `html_to_pdf.sh`, change `BUDGET="${BUDGET:-30000}"` to `BUDGET="${BUDGET:-5000}"` and replace the `--virtual-time-budget` paragraph in the header comment with: "`--virtual-time-budget` waits for KaTeX, which is now inlined and typesets synchronously at load, so the budget no longer covers a network fetch and 5 seconds is generous. Each run still gets its own throwaway profile directory: concurrent Chrome instances sharing one profile fight over its lock and one of them silently produces nothing."

Keep the watchdog loop and the `%%EOF` trailer check exactly as they are. Chrome 152 still declines to exit and macOS still ships no `timeout(1)`.

- [ ] **Step 2: Write the integration test**

```python
# tests/test_render_chain.py
"""End-to-end over the real toolchain. Skipped where Quarto or Chrome is absent,
so the unit suite still runs on a machine that has neither.
"""

import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
QUARTO = Path(os.environ.get("QUARTO", Path.home() / ".local" / "bin" / "quarto"))
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

PROBE = """---
title: "Render probe"
format:
  html:
    css: ../assets/lecture.css
    embed-resources: false
    html-math-method:
      method: katex
      url: "../vendor/katex/"
---

Inline $\\lambda(t)$ and a display:

$$
{}_tp_x = \\exp\\left(-\\int_0^t \\mu_{x+s}\\,ds\\right)
$$
"""


@pytest.fixture
def probe():
    target = REPO / "lectures" / "_probe.qmd"
    target.write_text(PROBE)
    yield target
    for suffix in (".qmd", ".html", ".pdf"):
        target.with_suffix(suffix).unlink(missing_ok=True)
    shutil.rmtree(REPO / "lectures" / "_probe_files", ignore_errors=True)


@pytest.mark.skipif(not QUARTO.is_file(), reason="quarto not installed")
def test_a_rendered_lecture_carries_no_external_reference(probe):
    subprocess.run(
        ["bash", "scripts/render_lecture.sh", str(probe.relative_to(REPO))],
        cwd=REPO, check=True, capture_output=True, text=True,
    )
    html = probe.with_suffix(".html").read_text()
    # Assert the specific paths are no longer referenced, rather than the bare
    # substrings `href=` and `src=`. The real inlined katex.min.js contains `src=`
    # in its own image-rendering code, so a substring assertion fails spuriously
    # the moment a genuine asset is inlined, which is what Task 8 found.
    assert "vendor/katex/katex.min.css" not in html
    assert "vendor/katex/katex.min.js" not in html
    assert "assets/lecture.css" not in html
    assert "katex.render" in html   # Quarto's own render loop survived
    assert ".katex" in html         # the stylesheet's rules were inlined


@pytest.mark.skipif(not QUARTO.is_file(), reason="quarto not installed")
def test_the_katex_path_is_not_concatenated_without_a_separator(probe):
    """Quarto joins its katex url to the filename with no separator, so a url
    missing its trailing slash yields vendor/katexkatex.min.js and silently
    fails to typeset. Verified against Quarto 1.10.18 on 3 September 2026."""
    subprocess.run(
        ["bash", "scripts/render_lecture.sh", str(probe.relative_to(REPO))],
        cwd=REPO, check=True, capture_output=True, text=True,
    )
    assert "katexkatex" not in probe.with_suffix(".html").read_text()


@pytest.mark.skipif(
    not (QUARTO.is_file() and CHROME.is_file()), reason="quarto or chrome absent"
)
def test_the_pdf_is_complete(probe):
    subprocess.run(
        ["bash", "scripts/render_lecture.sh", str(probe.relative_to(REPO))],
        cwd=REPO, check=True, capture_output=True, text=True,
    )
    subprocess.run(
        ["bash", "scripts/html_to_pdf.sh", str(probe.with_suffix(".html").relative_to(REPO))],
        cwd=REPO, check=True, capture_output=True, text=True,
    )
    pdf = probe.with_suffix(".pdf")
    assert pdf.stat().st_size > 10_000
    assert b"%%EOF" in pdf.read_bytes()[-64:]
```

- [ ] **Step 3: Run the test**

Run: `.venv/bin/python -m pytest tests/test_render_chain.py -v`
Expected: 3 passed. Where either test 1 or test 2 fails on the KaTeX path, check the trailing slash in the probe's `url` before anything else.

- [ ] **Step 4: Give the stylesheet KaTeX's display wrapper, and fix its header**

The sheet was copied byte-for-byte from a repo that renders with MathJax, so its only
maths rules target `.math.display` and `mjx-container[display="true"]` (lines 670, 677 and 791).
KaTeX wraps a display equation in `.katex-display`, which no rule mentions, so a wide equation
may overflow the column unboxed instead of getting the horizontal scroll the sheet intends.
Byte-identity was the means of carrying the sheet across rather than the goal, so this is a
deliberate, documented deviation from it.

First confirm the symptom. Render the probe from Step 2, open the HTML, and check whether the
display equation is wrapped in an element carrying `.katex-display` and whether it scrolls or
overflows. Report what you see either way.

Where it does overflow, add `.katex-display` alongside the existing selectors in all three
places, keeping `mjx-container` so the rules stay correct for anything rendered with MathJax:

```css
.math.display, .katex-display, mjx-container[display="true"] {
```

and in the print block at line 791:

```css
  .math.display, .katex-display, mjx-container[display="true"] { overflow: visible; }
```

Then replace the file's header comment. As copied it reads "Deep Learning for Actuarial
Modeling, Milano 2026 / Shared presentation layer for the seven Quarto lecture documents",
which describes the other repo's seven lectures rather than this corpus, and carries an American
spelling this repo's rules forbid. Say instead what the sheet is here, that it came from
`actuarial_deep_learning/lectures/lecture.css`, and that it deliberately departs from
`~/.claude/rules/html-design.md` in favour of a warm-paper reading register for long-form study.
Leave the rest of the sheet alone.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(render): carry the quarto and chrome chain across, network-free"
```

---

### Task 10: The KaTeX compatibility sweep

**Files:**
- Create: `scripts/katex_sweep.py`, `scripts/katex_check.mjs`
- Create: `notes/katex-compatibility-2026-09-03.md` (the report)
- Test: `tests/test_katex_sweep.py`

**Interfaces:**
- Consumes: `vendor/katex/katex.min.js` from Task 8.
- Produces: `extract_spans(text: str) -> list[tuple[int, bool, str]]` returning `(line, display, tex)`, and `sweep(paths: list[Path]) -> list[str]` returning failure lines.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_katex_sweep.py
from scripts.katex_sweep import extract_spans

QMD = """---
title: "T"
math: "$not maths, this is frontmatter$"
---

Inline $\\lambda(t)$ here.

$$
{}_tp_x = 1
$$

```python
cost = 5  # $ in a code fence is not maths
print("$x$")
```

And $\\mu_x$ after the fence.
"""


def test_frontmatter_is_not_scanned():
    assert all("frontmatter" not in tex for _, _, tex in extract_spans(QMD))


def test_fenced_code_is_not_scanned():
    assert all("code fence" not in tex for _, _, tex in extract_spans(QMD))
    assert all(tex.strip() != "x" for _, _, tex in extract_spans(QMD))


def test_display_and_inline_are_both_found_and_flagged():
    spans = extract_spans(QMD)
    assert (True, "{}_tp_x = 1") in [(d, t.strip()) for _, d, t in spans]
    assert r"\lambda(t)" in [t.strip() for _, d, t in spans if not d]
    assert r"\mu_x" in [t.strip() for _, d, t in spans if not d]


def test_line_numbers_are_reported_for_the_report():
    spans = extract_spans(QMD)
    assert all(line >= 1 for line, _, _ in spans)
    inline_lines = [line for line, d, t in spans if not d and "lambda" in t]
    assert inline_lines and inline_lines[0] == 6
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_katex_sweep.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'scripts.katex_sweep'`.

- [ ] **Step 3: Write the implementation**

```python
# scripts/katex_sweep.py
"""Test every mathematics span in a .qmd against KaTeX itself.

KaTeX supports a strict subset of MathJax, and the seventeen credit lectures
carried across from actuarial_deep_learning were authored against MathJax. A
construct KaTeX cannot parse renders as red error text rather than failing the
build, so it has to be found deliberately.

This runs the real parser rather than grepping for a list of suspects, so it
stays correct as lectures are added in Phase 4.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
FENCE = re.compile(r"^[ \t]*```.*?^[ \t]*```[ \t]*$", re.S | re.M)
DISPLAY = re.compile(r"\$\$(.+?)\$\$", re.S)
INLINE = re.compile(r"(?<![\$\w])\$([^\$\n]+?)\$(?![\$\w])")


def _blank(match: re.Match[str]) -> str:
    """Replace a span with the same number of newlines, so line numbers hold."""
    return "\n" * match.group(0).count("\n")


def extract_spans(text: str) -> list[tuple[int, bool, str]]:
    text = FRONTMATTER.sub(_blank, text)
    text = FENCE.sub(_blank, text)

    spans: list[tuple[int, bool, str]] = []
    for match in DISPLAY.finditer(text):
        spans.append((text[: match.start()].count("\n") + 1, True, match.group(1)))
    text = DISPLAY.sub(_blank, text)
    for match in INLINE.finditer(text):
        spans.append((text[: match.start()].count("\n") + 1, False, match.group(1)))
    return sorted(spans)


def sweep(paths: list[Path]) -> list[str]:
    payload = []
    for path in paths:
        for line, display, tex in extract_spans(path.read_text()):
            payload.append(
                {"file": str(path), "line": line, "display": display, "tex": tex}
            )
    if not payload:
        return []
    done = subprocess.run(
        ["node", str(REPO / "scripts" / "katex_check.mjs")],
        input=json.dumps(payload), text=True, capture_output=True, check=True,
    )
    return [f for f in json.loads(done.stdout) if f]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("qmd", type=Path, nargs="+")
    args = parser.parse_args()
    failures = sweep(args.qmd)
    for failure in failures:
        print(failure)
    total = sum(len(extract_spans(p.read_text())) for p in args.qmd)
    print(f"\n{total} spans across {len(args.qmd)} files, {len(failures)} unsupported")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
```

```javascript
// scripts/katex_check.mjs
// Read spans as JSON on stdin, render each with KaTeX throwing on error, and
// write the failures back as JSON. Node is used rather than a Python TeX parser
// because KaTeX itself is the only authority on what KaTeX accepts.
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const katex = require("../vendor/katex/katex.min.js");

const spans = JSON.parse(readFileSync(0, "utf8"));
const failures = spans.map((span) => {
  try {
    katex.renderToString(span.tex, {
      displayMode: span.display,
      throwOnError: true,
      strict: "warn",
    });
    return null;
  } catch (error) {
    const kind = span.display ? "display" : "inline";
    return `${span.file}:${span.line} (${kind}): ${error.message}`;
  }
});
process.stdout.write(JSON.stringify(failures));
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `.venv/bin/python -m pytest tests/test_katex_sweep.py -v`
Expected: 4 passed.

- [ ] **Step 5: Sweep the seventeen trunk lectures and write the report**

```bash
.venv/bin/python scripts/katex_sweep.py ../actuarial_deep_learning/credit_lectures/*.qmd \
  | tee notes/katex-compatibility-2026-09-03.md
```

Then open the report and add a paragraph at its head naming the date, the KaTeX version from `vendor/katex/VERSION`, and what was found. A preliminary grep on 3 September 2026 found only `\begin{gathered}`, `\begin{cases}` and `\begin{aligned}` across all seventeen, with no `\label`, `\eqref`, `\require`, `\tag`, `\newcommand`, `\mathrlap` or `\bm`, and KaTeX supports all three environments, so the expected result is zero unsupported spans. Where the sweep does find something, record each construct and its replacement in the report, since Phase 4 will need the same substitutions.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "feat(render): sweep lecture mathematics against katex itself"
```

---

### Task 11: The two exemplars

**Files:**
- Create: `scripts/fetch_credit_data.py`
- Create: `nodes/conditional-probability.md`, `nodes/survival-function.md`, `nodes/hazard-rate.md`
- Create: `paths/maths-stats-prerequisites.yaml`, `paths/survival-braid.yaml`
- Create: `lectures/S1_credit-survival-bridge.qmd` (copied and repathed)

**Interfaces:**
- Consumes: the whole pipeline.
- Produces: a corpus that passes all seven checks, and one rendered lecture with its PDF.

- [ ] **Step 1: Bring the data across**

```bash
cd ~/Documents/Repos/alchemist
cp ../actuarial_deep_learning/scripts/convert_credit_data.py scripts/fetch_credit_data.py
# The Bondora survival table is 8.5 MB and already built next door. Copying it
# beats re-downloading the 150 MB public CSV to rebuild the same file.
cp ../actuarial_deep_learning/data/bondora_survival.parquet data/
ls -lh data/bondora_survival.parquet
```

Then edit `scripts/fetch_credit_data.py`: keep the Bondora functions and the Eurostat fetcher, delete the Amex, Home Credit and credit-card branches with their `--datasets` choices, and update the module docstring to name only what remains. Phase 0's exemplar reads `bondora_survival.parquet` and nothing else, and a script offering to stream 15 GB it never needs is a trap for whoever runs it next. The public source URL stays in the docstring, so the file is rebuildable as the spec promises.

- [ ] **Step 2: Write the three exemplar nodes**

**The tier-1 page template.** A node body carries exactly three written sections, in this
order and under these headings. Everything else on a rendered node page is generated by
`render_node_page`, which is what keeps a Phase 3 agent's job to three short pieces of prose
and stops the graph and the page disagreeing.

1. `## Definition`, one or two sentences a reader could quote, naming the object and stating
   the condition under which it is undefined or degenerate.
2. `## The expression`, carrying the defining formula in a display block, in the rendering the node's
   `spends` declares, with every symbol in it named in the sentence beneath.
3. `## Why this node exists`, two or three sentences on what breaks without it, ending on
   the node that needs it next. This is the section that makes the graph readable as a
   syllabus rather than an index.

`nodes/conditional-probability.md`, written to that template in full, so the exemplar is a
thing to copy rather than a thing to interpret:

```markdown
---
id: conditional-probability
title: Conditional probability
domains: [maths, stats]
status: drafted
requires: []
spends: []
anchor: [ifoa.cs1.1.1]
vault_articles: []
vault_sources: []
taught_in: null
---

## Definition

The conditional probability of an event given a second event is the probability that
both occur, divided by the probability of the second. It is undefined where the
second event has probability zero, which is why a continuous conditioning variable
needs a density rather than this definition.

## The expression

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0
$$

Here $A$ is the event whose probability is wanted, $B$ is the event taken as given,
and $A \cap B$ is their joint occurrence. Rearranging gives the multiplication rule,
$P(A \cap B) = P(A \mid B)\,P(B)$, which is the form every likelihood in the corpus
is assembled from.

## Why this node exists

Every model downstream is a conditional statement. A probability of default is the
probability of an event given what was known at origination, a hazard is a
probability given survival so far, and a generalised linear model's response is a
distribution given a covariate vector. Without conditioning, none of those three
sentences can be written down, so this node is the root the survival branch grows
from and the survival function needs it next.
```

`nodes/survival-function.md`: `requires: [conditional-probability]`, `domains: [stats, life, credit]`, `spends` the survival object in `stats`, `life` and `credit`, `anchor: [ifoa.cs2.1.1]`.

`nodes/hazard-rate.md`: `requires: [survival-function]`, `domains: [stats, life, gi, credit]`, `spends` the hazard object in all four domains and the survival object in `credit`, `anchor: [ifoa.cs2.2.1]`, and `taught_in: S1_credit-survival-bridge`.

`hazard-rate` is the right exemplar because it spends one object under four different symbols, so it exercises the alias machinery harder than anything else in the corpus, and its `taught_in` proves the node-to-lecture link.

- [ ] **Step 3: Write the two paths**

```yaml
# paths/maths-stats-prerequisites.yaml
id: maths-stats-prerequisites
title: The mathematics and statistics the corpus assumes
builds_on: []
preamble: >
  Everything the domain paths take as given. Nothing here is specific to
  banking or to insurance.
nodes: [conditional-probability]
```

```yaml
# paths/survival-braid.yaml
id: survival-braid
title: Survival analysis across life, general insurance and credit
builds_on: [maths-stats-prerequisites]
preamble: >
  One object under four names. The braid runs from the survival function through
  the hazard rate and into the discrete-time hazard a lender can fit with the
  scorecard machinery it already has.
nodes: [survival-function, hazard-rate]
```

This pair proves `builds_on` in the real corpus: `survival-function` requires `conditional-probability`, which `survival-braid` never lists, so check 4 passes only through the closure.

- [ ] **Step 4: Copy the lecture and repath it**

```bash
cp ../actuarial_deep_learning/credit_lectures/S1_credit-survival-bridge.qmd lectures/
```

Then make three edits to `lectures/S1_credit-survival-bridge.qmd`:

1. Change `css: ../lectures/lecture.css` to `css: ../assets/lecture.css`.
2. Add the maths method under `format.html`, with the trailing slash:

```yaml
    html-math-method:
      method: katex
      url: "../vendor/katex/"
```

3. Change every `../data/` read to `../data/`, which is already correct because the lecture now sits one directory below the root exactly as it did before. Verify with `grep -n '\.\./data/' lectures/S1_credit-survival-bridge.qmd` and confirm each path resolves.

Add a comment under the YAML header recording that this is a copy of the trunk repo's lecture, re-rendered against vendored KaTeX, so the provenance travels with the file.

- [ ] **Step 5: Cover `parse_path`, which no earlier task exercises**

Append to `tests/test_model.py`. Task 1 tested `parse_node` and Task 4 constructs
`TeachingPath` records directly, so `parse_path` reaches Phase 0's end without a single test
despite both path files below depending on it.

```python
from scripts.alchemist.model import parse_path

VALID_PATH = """id: survival-braid
title: Survival analysis across life, general insurance and credit
builds_on: [maths-stats-prerequisites]
preamble: One object under four names.
nodes: [survival-function, hazard-rate]
"""


def test_parses_a_valid_path(tmp_path):
    target = tmp_path / "survival-braid.yaml"
    target.write_text(VALID_PATH)
    path = parse_path(target)
    assert path.id == "survival-braid"
    assert path.builds_on == ("maths-stats-prerequisites",)
    assert path.nodes == ("survival-function", "hazard-rate")


def test_a_path_defaults_builds_on_and_preamble_when_absent(tmp_path):
    target = tmp_path / "bare.yaml"
    target.write_text("id: bare\ntitle: Bare\nnodes: []\n")
    path = parse_path(target)
    assert path.builds_on == () and path.preamble == "" and path.nodes == ()


def test_a_path_filename_that_disagrees_with_the_id_is_rejected(tmp_path):
    target = tmp_path / "wrong.yaml"
    target.write_text(VALID_PATH)
    with pytest.raises(ValueError, match="does not match id"):
        parse_path(target)
```

Run: `.venv/bin/python -m pytest tests/test_model.py -v`
Expected: 8 passed, the five from Task 1 plus these three.

- [ ] **Step 6: Build, check, render and print**

```bash
.venv/bin/python scripts/build_site.py
.venv/bin/python scripts/check.py
bash scripts/render_lecture.sh lectures/S1_credit-survival-bridge.qmd
bash scripts/html_to_pdf.sh lectures/S1_credit-survival-bridge.html
.venv/bin/python -m pytest -v
```

Expected: `check.py` reports ok on all seven rules and exits zero; the render emits the lecture with figures under `lectures/figures/S1_credit-survival-bridge/`; the PDF is more than 200 kB and ends in `%%EOF`.

- [ ] **Step 7: Test that the PDF carries typeset mathematics, not TeX source**

This is the failure the whole render chain exists to remove, and Task 9's tests cannot see it.
Chrome can snapshot the page before KaTeX has finished typesetting, and the resulting PDF is
complete, correctly trailed and A4 while carrying raw `\frac{}{}` where the mathematics should
be. File size and the `%%EOF` check both pass. Task 9's probe was equation-only and was verified
by a human read; this lecture has figures that take longer to compose, which is precisely when a
5-second `BUDGET` could fire early.

Add `pypdf==5.1.0` to `requirements-dev.txt` and install it, then add to
`tests/test_render_chain.py`:

```python
TEX_SOURCE = re.compile(r"\\(?:frac|int|exp|sum|prod|mathbf|mathrm|left|right)\b")


@pytest.mark.skipif(not (QUARTO.is_file() and CHROME.is_file()), reason="quarto or chrome absent")
def test_the_exemplar_pdf_carries_typeset_mathematics():
    """A PDF whose maths snapshot fired early is complete, correctly trailed and
    A4 while showing raw TeX, so neither the size check nor the %%EOF check can
    see it. Extract the text and look instead.
    """
    from pypdf import PdfReader

    pdf = REPO / "lectures" / "S1_credit-survival-bridge.pdf"
    if not pdf.is_file():
        pytest.skip("the exemplar lecture has not been printed yet")
    text = "\n".join(page.extract_text() for page in PdfReader(pdf).pages)
    assert "hazard" in text.lower()          # extraction worked at all
    assert TEX_SOURCE.search(text) is None   # and no command survived untypeset
```

Add `import re` to that file's imports if it is not already there.

Run: `.venv/bin/python -m pytest tests/test_render_chain.py -v`
Expected: 4 passed.

Then open the HTML and read one page of mathematics with your own eyes as well. The test catches
untypeset TeX; it cannot tell you the typesetting is *good*.

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "feat(corpus): add three exemplar nodes, two paths and the S1 lecture"
```

---

### Task 12: CLAUDE.md, the commit hook and the Pages workflow

**Files:**
- Create: `CLAUDE.md`, `.githooks/pre-commit`, `.github/workflows/pages.yml`, `README.md`
- Test: `tests/test_hook.py`

**Interfaces:**
- Consumes: `scripts/check.py`.
- Produces: the repo's own conventions, enforced.

- [ ] **Step 1: Write `CLAUDE.md`**

Cover, in this order: what the repo is and the one job in spec section 1; the two tiers; the node, notation, path and ledger schemas by pointing at the spec rather than restating them; the closed domain vocabulary and the anchor grammar; the seven checks and the fact that `check.py` runs on every commit; the build commands; the public-repo rules including the CC BY-NC 4.0 constraint; and the pointer to `~/.claude/rules/` for the shared standards. State plainly which Gini conventions are suspended here and why, following the pattern in `actuarial_deep_learning/CLAUDE.md`, and record that `assets/lecture.css` deliberately departs from `~/.claude/rules/html-design.md` with the deviation stated at the sheet's own head.

- [ ] **Step 2: Wire the hook**

```bash
mkdir -p .githooks
cat > .githooks/pre-commit <<'HOOK'
#!/usr/bin/env bash
# Run the corpus checks before every commit. A broken graph is cheap to fix now
# and expensive once hundreds of pages hang off it.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
.venv/bin/python scripts/check.py
HOOK
chmod +x .githooks/pre-commit
git config core.hooksPath .githooks
```

- [ ] **Step 3: Write the failing test**

```python
# tests/test_hook.py
import os
import stat
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def test_the_hook_is_executable():
    hook = REPO / ".githooks" / "pre-commit"
    assert hook.is_file()
    assert hook.stat().st_mode & stat.S_IXUSR


def test_git_is_configured_to_use_it():
    done = subprocess.run(
        ["git", "config", "core.hooksPath"], cwd=REPO, capture_output=True, text=True
    )
    assert done.stdout.strip() == ".githooks"


def test_the_hook_passes_on_the_current_tree():
    done = subprocess.run(
        ["bash", ".githooks/pre-commit"], cwd=REPO, capture_output=True, text=True,
        env={**os.environ},
    )
    assert done.returncode == 0, done.stdout + done.stderr
```

- [ ] **Step 4: Run the test**

Run: `.venv/bin/python -m pytest tests/test_hook.py -v`
Expected: 3 passed.

- [ ] **Step 5: Write the Pages workflow**

Copy the shape of `actuarial_deep_learning/.github/workflows/pages.yml` and change the assemble step's allow-list to: `index.html`, `site/` (the path pages and graph SVGs), `nodes/` rendered pages, `notation/symbols.md`, `lectures/*.html`, `lectures/*.pdf`, `lectures/figures/`, and `assets/`. Everything not named stays off the site, so `notes/`, the grading reports, the `.qmd` sources, `sources/wanted.yaml` and `scripts/` do not publish.

Two operational notes carried over: re-running only the failed job of a run that both uploads and deploys produces a second artefact named `github-pages` and `deploy-pages` then refuses to choose between them, so dispatch a fresh run instead; and `upload-pages-artifact@v5` excludes hidden files by default, which would silently drop `site/.nojekyll` unless `include-hidden-files: true` is set.

Add a job that runs, in this order, `.venv/bin/python scripts/build_site.py`, then
`.venv/bin/python scripts/check.py`, then `.venv/bin/python -m pytest`, before the deploy.
The build comes first because `index.html` is generated and committed while only
`notation/symbols.md` is guarded by check 7, so a stale index would otherwise publish.

- [ ] **Step 6: Point Pyright at the virtual environment**

Append to `pyproject.toml`:

```toml
[tool.pyright]
venvPath = "."
venv = ".venv"
```

Without it, Pyright reports `Import "pytest" could not be resolved` and
`Import "scripts.alchemist.model" could not be resolved` on every test file, because nothing
tells it where the packages live. The tests themselves resolve fine, since
`[tool.pytest.ini_options] pythonpath = ["."]` handles the import path at runtime. This is
editor configuration rather than a code fix, which is why it sits here rather than in Task 1.

- [ ] **Step 7: Write `README.md`**

One page: what Alchemist is, the two tiers, how to clone and run the checks (including that checks 5 and 6 skip without a vault, so a stranger gets five of seven), how to render a lecture, and the CC BY-NC 4.0 notice on ETH-derived material.

- [ ] **Step 8: Run everything and commit**

```bash
.venv/bin/python -m pytest -v
.venv/bin/python scripts/check.py
git add -A
git commit -m "chore: add repo conventions, the pre-commit hook and the pages workflow"
```

---

## Definition of done for Phase 0

Gate 1 opens when all of the following hold.

1. `.venv/bin/python -m pytest` passes, with no test skipped other than by an absent Quarto or Chrome.
2. `.venv/bin/python scripts/check.py` exits zero and reports ok on all seven rules, with none skipped on your machine.
3. `nodes/hazard-rate.md` reads as a page you would put in front of somebody, and it spends one object under four symbols.
4. `lectures/S1_credit-survival-bridge.html` opens with the network off and typesets its mathematics, and its PDF ends in `%%EOF`.
5. `notes/katex-compatibility-2026-09-03.md` records the sweep result across all seventeen trunk lectures.
6. `notation/symbols.md` is committed, generated, and check 7 agrees it is current.

Then you read the schema, the object table, and both exemplars, and Phase 1 gets its own plan.

---

## Spec coverage

Every section of the spec maps to a task, or is deliberately deferred.

| Spec section | Covered by |
|---|---|
| 4.1 node record | Task 1 |
| 4.1a node granularity | **Deferred to Phase 1.** It governs transcription, and Phase 0 writes three nodes by hand. |
| 4.2 notation contract | Task 2, seeded with all twelve collisions |
| 4.3 paths | Task 1 parses them, Task 11 writes the first two |
| 4.4 gap ledger | Task 5, seeded with one worked entry |
| 5 checks 1 to 7 | Tasks 3, 4, 5 and 6, with the runner in Task 7 |
| 6 repo layout | Tasks 1 and 12 |
| 7 build pipeline | Tasks 7, 8 and 9. The typeface needs no work: the stylesheet resolves to system stacks. |
| 8 licence and confidentiality | Check 5 in Task 5, and `CLAUDE.md` plus `README.md` in Task 12 |
| 9 phases and gates | This plan is Phase 0; its gate is the definition of done above |
| 10 model routing | **Not software.** Switch to Sonnet before Task 1. Phase 3 decides Fable on grader output. |
| 11 out of scope | Nothing in this plan touches the excluded items |
