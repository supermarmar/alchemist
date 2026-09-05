"""Merge the per-body staging directories into one corpus.

Twenty agents transcribe in parallel and several of them produce the same
node: survival-function comes out of CS2, F107 and the ETH lectures alike. Each
writes into its own directory, and this is where a shared node becomes shared
rather than duplicated.

The union is the point. A merged record carries every body's anchor, the union
of their domain sets and the union of their prerequisites, because a dropped
anchor is silent: the corpus still checks green without it and the loss surfaces
only in Phase 3, when a page cannot say why its node exists.

A title disagreement is not a union and is never guessed. The first title in
body order wins and the alternative is reported, because which of "Chain ladder"
and "The chain ladder method" the corpus uses is a decision rather than a merge.
"""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

import yaml

from .model import Node, parse_node


def collect(staging: Path) -> dict[str, list[Node]]:
    """Every staged record, grouped by id, in body-directory order.

    The order is sorted rather than filesystem order, so a merge run twice over
    the same staging produces byte-identical output. A thousand records that
    re-order on every run make every diff unreadable.
    """
    grouped: dict[str, list[Node]] = {}
    for body in sorted(p for p in staging.iterdir() if p.is_dir()):
        for record in sorted((body / "nodes").glob("*.md")):
            node = parse_node(record)
            grouped.setdefault(node.id, []).append(node)
    return grouped


def merge(records: list[Node], existing: Node | None = None) -> tuple[Node, list[str]]:
    """One merged record and the notes a reader has to adjudicate.

    `existing` is the record already in nodes/ under this id, where there is one.
    Three drafted exemplars sit there from Phase 0, one with a lecture attached,
    and CS1 and CS2 stage the same ids because they teach the same concepts. A
    corpus record wins on everything a stub cannot supply, meaning title, status,
    body, spends, the vault fields and taught_in, and gains the staged anchors,
    domains and prerequisites by union. Without this the merge replaces a written
    page with two sentences and orphans its lecture.
    """
    first = existing or records[0]
    everyone = ([existing] if existing is not None else []) + records
    notes: list[str] = []

    def body_of(node: Node) -> str:
        return "nodes" if node is existing else node.path.parts[-3]

    for other in records:
        if other is first:
            continue
        if other.title != first.title:
            notes.append(
                f"{first.id}: titled {first.title!r} in {body_of(first)} and "
                f"{other.title!r} in {body_of(other)}, keeping the first"
            )

    def union(field: str) -> tuple[str, ...]:
        return tuple(sorted({value for r in everyone for value in getattr(r, field)}))

    bodies = sorted({body_of(r) for r in records})
    if len(bodies) > 1:
        notes.append(f"{first.id}: merged from {len(bodies)} bodies, {', '.join(bodies)}")
    if existing is not None:
        notes.append(
            f"{first.id}: protected {existing.status} record already in nodes/, "
            f"gained anchors from {', '.join(bodies)}"
        )

    protected = existing is not None
    merged = Node(
        id=first.id,
        title=first.title,
        domains=union("domains"),
        status=first.status if protected else "stub",
        requires=union("requires"),
        spends=first.spends if protected else (),
        anchor=union("anchor"),
        vault_articles=first.vault_articles if protected else (),
        vault_sources=first.vault_sources if protected else (),
        taught_in=first.taught_in if protected else None,
        body=first.body,
        path=first.path,
    )
    return merged, notes


def _tokens_close(x: str, y: str) -> bool:
    """Two hyphen-separated tokens that read as one word spelled two ways."""
    return x != y and len(x) >= 4 and len(y) >= 4 and x[:4] == y[:4]


def near_misses(ids: Iterable[str]) -> list[tuple[str, str]]:
    """Pairs of distinct ids the exact-match reuse check is blind to by construction.

    Batch A and B agents reused an id only on a character-for-character match, so
    CM2 staged efficient-markets-hypothesis beside the undergraduate's
    efficient-market-hypothesis, and SP9 staged reputational-risk beside SP1's
    reputation-risk, with no collision and no warning. Two ids are near misses
    where they have the same token count and exactly one token differs while
    sharing its first four letters, or where one is the other with a single
    token inserted. Roughly 120 pairs over 1,600 ids; a list a human reads once
    in Task 11 rather than a rule the merge acts on.
    """
    ordered = sorted(set(ids))
    split = {i: i.split("-") for i in ordered}
    out: list[tuple[str, str]] = []
    for a_i, a in enumerate(ordered):
        ta = split[a]
        for b in ordered[a_i + 1:]:
            tb = split[b]
            if abs(len(ta) - len(tb)) > 1:
                continue
            if len(ta) == len(tb):
                diff = [(x, y) for x, y in zip(ta, tb) if x != y]
                if len(diff) == 1 and _tokens_close(*diff[0]):
                    out.append((a, b))
            else:
                longer, shorter = (ta, tb) if len(ta) > len(tb) else (tb, ta)
                if any(longer[:k] + longer[k + 1:] == shorter for k in range(len(longer))):
                    out.append((a, b))
    return out


def _scalar(value: str) -> str:
    """A YAML-safe rendering of one string, quoted only where quoting is required.

    `title` is the one free-text field this renderer carries: a staged title such
    as "Pillar 1: minimum capital requirements" contains a colon, and writing it
    bare after `title: ` breaks the line into two mapping keys. Deferring the
    quoting decision to `yaml.safe_dump` rather than hand-rolling one avoids
    reproducing that bug for the next character class a title happens to carry.
    `safe_dump` appends a `\\n...` document-end marker for a plain scalar with no
    explicit style, which this strips before the value goes back onto one line.
    """
    dumped = yaml.safe_dump(value, allow_unicode=True).strip()
    if dumped.endswith("\n..."):
        dumped = dumped[: -len("\n...")]
    return dumped


def render(node: Node) -> str:
    """Frontmatter written by hand rather than by yaml.safe_dump, so the file
    reads the way the exemplar nodes do: flow sequences on one line, and the
    field order the spec's example uses rather than alphabetical. Every field
    renders from the record, because a protected drafted node carries spends, a
    lecture and vault entries that a stub-only renderer would drop in silence."""
    if node.spends:
        spends = "spends:\n" + "\n".join(
            f"  - {{object: {s.object}, domain: {s.domain}}}" for s in node.spends
        )
    else:
        spends = "spends: []"
    meta = [
        f"id: {node.id}",
        f"title: {_scalar(node.title)}",
        f"domains: [{', '.join(node.domains)}]",
        f"status: {node.status}",
        f"requires: [{', '.join(node.requires)}]",
        spends,
        f"anchor: [{', '.join(node.anchor)}]",
        f"vault_articles: [{', '.join(node.vault_articles)}]",
        f"vault_sources: [{', '.join(node.vault_sources)}]",
        f"taught_in: {node.taught_in or 'null'}",
    ]
    return "---\n" + "\n".join(meta) + "\n---\n\n" + node.body.strip() + "\n"


def write_merged(merged: dict[str, Node], target: Path) -> list[Path]:
    target.mkdir(parents=True, exist_ok=True)
    written = []
    for node_id in sorted(merged):
        destination = target / f"{node_id}.md"
        destination.write_text(render(merged[node_id]))
        written.append(destination)
    return written
