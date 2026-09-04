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


ALIAS_KEYS = frozenset({"domain", "symbol", "name", "note"})


def load_objects(root: Path = REPO) -> Objects:
    raw = yaml.safe_load((root / "notation" / "objects.yaml").read_text()) or []
    by_id: dict[str, MathObject] = {}
    for entry in raw:
        # An alias is a YAML flow mapping, so an unquoted note ends at its first
        # comma and the remainder parses as a bare key carrying null. Reading
        # `note` alone would then publish the truncated half and complain about
        # nothing, which is what happened to three of these notes. Rejecting any
        # key outside the four turns that silence into a parse error naming the
        # object, the domain and the fragment that was lost.
        for alias in entry["aliases"]:
            extra = set(alias) - ALIAS_KEYS
            if extra:
                raise ValueError(
                    f"{entry['id']}, alias for domain {alias.get('domain')!r}: "
                    f"unknown alias keys {sorted(extra)}. An unquoted note "
                    f"containing a comma splits into a bare key like this, so "
                    f"quote the note."
                )
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
