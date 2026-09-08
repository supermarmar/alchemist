"""Merge one node id into another.

The survivor keeps its identity and gains the absorbed record's anchors, domains,
and prerequisites; every reference to the absorbed id is repointed; the absorbed
file is deleted. Ids are never renamed, and a merge is the one edit that removes
one, so it does every part of the job or none: a survivor written without the
repointing leaves dangling `requires` entries that check 3 catches and dangling
path lines that check 4 catches, and a repointing without the deletion leaves a
duplicate. Task 11 did six of these by hand in Phase 1; gate 2 ruled twenty-two
more (D7), which is what made a tool worth its tests.

Only the `requires:` line of a referring node is rewritten, as a flow sequence,
which is how every record written by `staging.render` carries it. A record whose
requires is a block sequence is left alone and check 3 reports the dangling id.
"""

from __future__ import annotations

import re
from dataclasses import replace
from pathlib import Path

import yaml

from .model import Node, parse_node, parse_path
from .staging import render

REQUIRES_LINE = re.compile(r"^requires: \[(.*)\]$", re.M)


def merged_record(survivor: Node, absorbed: Node) -> Node:
    both = {survivor.id, absorbed.id}

    def union(field: str) -> tuple[str, ...]:
        return tuple(sorted(set(getattr(survivor, field)) | set(getattr(absorbed, field))))

    return replace(
        survivor,
        domains=union("domains"),
        requires=tuple(r for r in union("requires") if r not in both),
        anchor=union("anchor"),
        vault_articles=union("vault_articles"),
        vault_sources=union("vault_sources"),
    )


def repoint_requires(text: str, absorbed: str, survivor: str, node_id: str) -> str:
    """Rewrite one node's requires line: absorbed becomes survivor, deduplicated, no self-edge."""
    match = REQUIRES_LINE.search(text)
    if match is None:
        return text
    items = [i.strip() for i in match.group(1).split(",") if i.strip()]
    if absorbed not in items:
        return text
    kept: list[str] = []
    for item in items:
        target = survivor if item == absorbed else item
        if target != node_id and target not in kept:
            kept.append(target)
    return text[: match.start()] + f"requires: [{', '.join(kept)}]" + text[match.end():]


def repoint_path(text: str, absorbed: str, survivor: str) -> str:
    lines = text.split("\n")
    if f"- {absorbed}" not in lines:
        return text
    if f"- {survivor}" in lines:
        lines = [line for line in lines if line != f"- {absorbed}"]
    else:
        lines = [f"- {survivor}" if line == f"- {absorbed}" else line for line in lines]
    return "\n".join(lines)


def ledger_names(ledger: Path, node_id: str) -> bool:
    entries = yaml.safe_load(ledger.read_text()) or []
    return any(node_id in (entry.get("needed_by") or []) for entry in entries)


def merge_pair(root: Path, absorbed_id: str, survivor_id: str) -> list[Path]:
    nodes_dir = root / "nodes"
    ledger = root / "sources" / "wanted.yaml"
    if ledger.exists() and ledger_names(ledger, absorbed_id):
        raise ValueError(f"{absorbed_id} is named in {ledger}; repoint the ledger first")
    absorbed = parse_node(nodes_dir / f"{absorbed_id}.md")
    survivor = parse_node(nodes_dir / f"{survivor_id}.md")

    touched: list[Path] = []
    survivor_file = nodes_dir / f"{survivor_id}.md"
    survivor_file.write_text(render(merged_record(survivor, absorbed)))
    touched.append(survivor_file)
    absorbed.path.unlink()
    touched.append(absorbed.path)

    for path in sorted(nodes_dir.glob("*.md")):
        text = path.read_text()
        rewritten = repoint_requires(text, absorbed_id, survivor_id, path.stem)
        if rewritten != text:
            path.write_text(rewritten)
            parse_node(path)
            touched.append(path)
    for path in sorted((root / "paths").glob("*.yaml")):
        text = path.read_text()
        rewritten = repoint_path(text, absorbed_id, survivor_id)
        if rewritten != text:
            path.write_text(rewritten)
            parse_path(path)
            touched.append(path)
    return touched
