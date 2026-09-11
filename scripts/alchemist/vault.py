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
from typing import Literal

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


def _frontmatter(path: Path) -> tuple[dict | None, str | None]:
    """A wiki file's frontmatter as a mapping, plus a reason where there is none.

    `read_wiki` and `attachment_complaint` both match the `FRONTMATTER` pattern,
    parse its first group as YAML, and check the result is a mapping. `read_wiki`
    reports which of those three ways parsing can fail, in its skip list;
    `attachment_complaint` only needs to know that it did, so the reason is
    there for a caller to use or ignore.
    """
    match = FRONTMATTER.match(path.read_text())
    if match is None:
        return None, "no frontmatter"
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return None, f"frontmatter does not parse ({exc.__class__.__name__})"
    if not isinstance(meta, dict):
        return None, "frontmatter is not a mapping"
    return meta, None


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
        meta, reason = _frontmatter(path)
        if meta is None:
            skipped.append(f"{slug}: {reason}")
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


@dataclass(frozen=True)
class AttachmentProblem:
    """Why a slug cannot be attached, in a shape each caller can phrase itself.

    A returned string would force check 11, which reports against a node, to
    strip a slug prefix the attach tool wants, and the two are specified to
    word their three cases differently. `kind` lets each caller branch and
    write its own message, so neither ever matches on text.
    """
    kind: Literal["missing", "unclassified", "not-publishable"]
    path: Path
    confidentiality: str | None = None


def attachment_complaint(vault: Path, slug: str) -> AttachmentProblem | None:
    """None where the slug is attachable, otherwise structured detail on why.

    Check 11 and the attach tool both ask this question, and a second copy of
    the answer would drift from the first. Each still writes its own failure
    message from the `AttachmentProblem` returned here, because a check reports
    against a node and a CLI reports against its argument.
    """
    path = article_path(vault, slug)
    if not path.is_file():
        return AttachmentProblem("missing", path)
    meta, _ = _frontmatter(path)
    confidentiality = meta.get("confidentiality") if meta else None
    if confidentiality is None:
        return AttachmentProblem("unclassified", path)
    if str(confidentiality) not in PUBLISHABLE_ARTICLE:
        return AttachmentProblem("not-publishable", path, str(confidentiality))
    return None
