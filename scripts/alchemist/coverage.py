"""Attachment coverage over the corpus, and the markdown report built from it.

Every node starts Phase 2 with ``vault_articles: []``. The wave agents attach
what the vault actually holds, and the vault is a credit risk research base
sitting under a corpus that is heaviest in actuarial and statistical material
it barely touches, so most nodes stay uncovered however many waves run.
Reporting that fact alone would tell Mario nothing he does not already know.
The question the gate exists to put is which document, once acquired, would
close the largest block of uncovered nodes, and that is what
``by_anchor_document`` and the report's closing section answer.

Nothing here touches the filesystem beyond what ``load_corpus`` has already
read: every function takes a ``Corpus`` and returns rows or text. Reading
``data/vault-index.yaml`` and writing the report to disk are
``build_coverage_report.py``'s job, matching how ``check.py`` sits over
``checks.py``.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable, Iterable

from .model import Corpus, Node

#: Passed as `index_built` when no vault index was present at generation
#: time, so `render_report` can say so plainly rather than the report
#: claiming a build date that does not exist.
NO_INDEX = "no index was present"


def _attached(node: Node) -> bool:
    """A node counts as attached once it carries at least one vault article.

    `vault_sources` is a separate declaration, that a node quotes a source
    rather than draws on it through prose, and check 11 already gates its
    resolution on its own terms. Coverage, the question this module answers,
    is about `vault_articles` alone.
    """
    return bool(node.vault_articles)


def _anchor_documents(node: Node) -> set[str]:
    """The distinct `<body>.<subject>` prefixes a node's anchors point at.

    Two anchors under the same document, two syllabus paragraphs from the
    same course, still make the node one member of that document rather
    than two, so this de-duplicates before any caller counts. The literal
    `chosen` anchors no document and is dropped.
    """
    return {
        ".".join(anchor.split(".")[:2])
        for anchor in node.anchor
        if anchor != "chosen"
    }


def _coverage_by(
    corpus: Corpus, keys_of: Callable[[Node], Iterable[str]]
) -> list[tuple[str, int, int]]:
    """The shared body of `by_domain` and `by_anchor_document`: count members
    and attachments per key, then sort by member count descending and key
    ascending. `keys_of` extracts the one or more keys a node belongs under,
    domains for one caller and anchor documents for the other, and a node
    naming more than one key is a member of each rather than of one instead
    of the others.
    """
    members: dict[str, int] = defaultdict(int)
    attached: dict[str, int] = defaultdict(int)
    for node in corpus.nodes.values():
        covered = _attached(node)
        for key in keys_of(node):
            members[key] += 1
            if covered:
                attached[key] += 1
    rows = [(key, count, attached[key]) for key, count in members.items()]
    rows.sort(key=lambda row: (-row[1], row[0]))
    return rows


def by_domain(corpus: Corpus) -> list[tuple[str, int, int]]:
    """Coverage split by domain, as (domain, members, attached).

    A node declaring more than one domain is a member of each; there is no
    single domain a multi-domain node belongs to instead of the others.
    Rows are sorted by member count descending, then by domain name, so the
    domains carrying the most nodes lead the table.
    """
    return _coverage_by(corpus, lambda node: node.domains)


def by_anchor_document(corpus: Corpus) -> list[tuple[str, int, int]]:
    """Coverage split by anchor document, as (document, members, attached).

    A node anchored at `ifoa.cs2.1.1-5` belongs to document `ifoa.cs2`. Rows
    are sorted by member count descending, then by document name, matching
    `by_domain`, so the documents whose acquisition would close the most
    nodes lead the table.
    """
    return _coverage_by(corpus, _anchor_documents)


def attachment_histogram(corpus: Corpus) -> dict[int, int]:
    """Node count keyed by how many vault articles that node has attached.

    Zero dominates this histogram for most of Phase 2, and a node sitting at
    zero is not on its own a defect: the vault may simply hold nothing on
    that node's subject.
    """
    histogram: dict[int, int] = defaultdict(int)
    for node in corpus.nodes.values():
        histogram[len(node.vault_articles)] += 1
    return dict(histogram)


def _plural(count: int, word: str) -> str:
    return f"{count} {word}" if count == 1 else f"{count} {word}s"


def _agree(count: int, singular: str, plural: str) -> str:
    """The verb or pronoun matching `count`, so a sentence built around a
    count computed at run time still reads correctly should that count ever
    settle on exactly one.
    """
    return singular if count == 1 else plural


def _table(headers: list[str], aligns: list[str], rows: list[tuple]) -> list[str]:
    """A markdown table. `aligns` takes `"l"` or `"r"` per column, matching
    the numeric-right-alignment convention `site.py`'s tables already use.
    """
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---:" if a == "r" else "---" for a in aligns) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return lines


def render_report(corpus: Corpus, index_built: str) -> str:
    """The Phase 2 coverage report, as markdown.

    The anchor document view leads the report, ahead of the domain view,
    because it is the one the acquisition decision is actually made from: it
    turns an uncovered node count into a named list of documents that would
    close it. The domain view, the attachment histogram, and the closing
    list of anchor documents with nothing attached follow it in turn.
    """
    total = len(corpus.nodes)
    attached_total = sum(1 for node in corpus.nodes.values() if _attached(node))
    uncovered_total = total - attached_total

    anchor_rows = by_anchor_document(corpus)
    domain_rows = by_domain(corpus)
    histogram = attachment_histogram(corpus)

    pretoria_count = sum(1 for document, _, _ in anchor_rows if document.startswith("up."))
    uncovered_anchors = [row for row in anchor_rows if row[2] == 0]

    if index_built == NO_INDEX:
        index_line = (
            "No vault index was present when this report was generated. "
            "The figures below come from the corpus itself rather than "
            "from the index, so they still stand, but rebuild the index "
            "and re-run the affected batches before trusting any "
            "attachment made since the last successful build."
        )
    else:
        index_line = (
            f"The vault index behind these figures was built on {index_built}. "
            "Treat any attachment written against an older index as stale "
            "once the vault has moved on from that build."
        )

    anchor_intro = (
        f"The corpus points at {_plural(len(anchor_rows), 'distinct anchor document')}. "
        "Each one is identified by a node's anchor, taken as its "
        "`<body>.<subject>` prefix, and a node anchored `chosen` names no "
        "document, so it is set aside from every row below. This is the "
        "view the acquisition decision rests on: it turns an uncovered "
        "node count into the specific document that would close it. "
        f"Of those documents, {pretoria_count} "
        f"{_agree(pretoria_count, 'carries', 'carry')} an `up.*` prefix, a "
        "University of Pretoria course code. `sources/syllabi.yaml` "
        "records the 20 syllabus documents the corpus's anchors are drawn "
        "from, one row per document acquired. Eighteen of them already "
        "carry a full `<body>.<subject>` prefix, such as `ifoa.cs2`, so "
        "each lines up with exactly one row in the table below. The two "
        "University of Pretoria yearbook extracts carry only the body "
        "segment, `up`. Each extract covers many modules, and a node "
        "anchored into one of those supplies the missing subject segment "
        "itself, which is why the two extracts expand into the `up.*` "
        "rows just counted. A reader checking whether a document below is "
        "already held should look up its issuing body in "
        "`sources/syllabi.yaml`, and should expect that file's row count "
        "to differ from the table's rather than match it."
    )

    domain_intro = (
        "This splits the same corpus by the domain each node declares, "
        "instead of by the document it is anchored to. A node declaring "
        "more than one domain is counted once under each."
    )

    histogram_intro = (
        "The table below counts nodes by how many vault articles each one "
        f"carries. The node counts sum to {_plural(total, 'node')} across "
        "the corpus."
    )

    out = [
        "# Phase 2 coverage report",
        "",
        "This report measures how much of the node corpus carries an "
        "attached vault article, read directly from the corpus so the "
        "figures hold however far the waves have progressed.",
        "",
        index_line,
        "",
        f"The corpus holds {_plural(total, 'node')}. Of these, "
        f"{_plural(attached_total, 'node')} "
        f"{_agree(attached_total, 'carries', 'carry')} at least one "
        f"attached vault article and {_plural(uncovered_total, 'node')} "
        f"{_agree(uncovered_total, 'carries', 'carry')} none.",
        "",
        "## Coverage by anchor document",
        "",
        anchor_intro,
        "",
        *_table(
            ["Anchor document", "Nodes", "Attached", "Uncovered"],
            ["l", "r", "r", "r"],
            [(doc, n, a, n - a) for doc, n, a in anchor_rows],
        ),
        "",
        "## Coverage by domain",
        "",
        domain_intro,
        "",
        *_table(
            ["Domain", "Nodes", "Attached", "Uncovered"],
            ["l", "r", "r", "r"],
            [(domain, n, a, n - a) for domain, n, a in domain_rows],
        ),
        "",
        "## Attachments per node",
        "",
        histogram_intro,
        "",
        *_table(
            ["Attachments", "Nodes"],
            ["r", "r"],
            [(count, histogram[count]) for count in sorted(histogram)],
        ),
        "",
        "## Anchor documents with no attachment at all",
        "",
    ]

    if uncovered_anchors:
        uncovered_count = len(uncovered_anchors)
        out += [
            f"{_plural(uncovered_count, 'anchor document')} "
            f"{_agree(uncovered_count, 'carries', 'carry')} no attachment "
            f"at all, so none of {_agree(uncovered_count, 'its', 'their')} "
            "nodes has a vault article. This is the acquisition list in "
            "its rawest form. Each row names a document, how many nodes "
            "depend on it, and whether it is one of the Pretoria course "
            "codes.",
            "",
            *_table(
                ["Anchor document", "Nodes", "Pretoria course code"],
                ["l", "r", "l"],
                [
                    (doc, n, "yes" if doc.startswith("up.") else "no")
                    for doc, n, _ in uncovered_anchors
                ],
            ),
        ]
    else:
        out.append(
            "Every anchor document carries at least one attachment. "
            "Nothing belongs on the acquisition list on this measure alone."
        )

    return "\n".join(out) + "\n"
