"""Rank every verifiable anchor by how much of its node's subject appears where
the anchor points.

No check can do this job. Rule 12 was considered and rejected on 17 September
2026: d424's paragraph numbers restart at every section, so "37." occurs four
times in the extraction, and all three anchors the Phase 2 waves reported as
wrong cite numbers that exist. An existence rule would therefore have caught
none of them. What did catch them is a human reading a topic-overlap ranking,
which is what this script prints. It reports and never gates, so it carries no
false-positive cost and the corpus keeps its eleven checks.

Only two of the six anchor bodies can be audited at all. bcbs points at d424,
which the vault holds as a full extraction, and ucsc at the twelve lectures,
which the vault holds as the summer-school originals and
`actuarial_deep_learning/credit_lectures/` as the credit recast. ifoa, assa, up
and iasb name material nobody holds, so they are counted and named as
unverifiable rather than passed over in silence: roughly nine anchor references
in ten cannot be checked today, and every defect found so far sits in the tenth
that can, which is selection bias rather than a clean bill of health.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.alchemist.model import Node, load_corpus  # noqa: E402

REPO = Path(__file__).resolve().parents[1]

# The major sections of d424, in document order, each named by the line that
# titles it. Matching the title rather than a line number keeps the map valid
# across a re-extraction. "Output floor" also appears in the table of contents,
# which is why each title is sought after the previous section's start rather
# than from the top of the file.
D424_SECTIONS: tuple[tuple[str, str], ...] = (
    ("intro", "Introduction"),
    ("sa", "Standardised approach for credit risk"),
    ("irb", "Internal ratings-based approach for credit risk"),
    ("cva", "Minimum capital requirements for CVA risk"),
    ("oprisk", "Minimum capital requirements for operational risk"),
    ("floor", "Output floor"),
    ("lr", "Leverage ratio"),
)

# Words that carry no subject, so scoring on them would mark every anchor
# covered. Deliberately short: a stop list long enough to argue about is a stop
# list that hides what the score is really measuring.
STOPWORDS = frozenset(
    """a an and are as at by for from in into its of on or per the their to under with
    other others general specific standards standard requirements requirement approach
    approaches method methods model models""".split()
)

STEM_SUFFIX = r"(?:s|es|ed|ing|al|ally)?"


def vault_root() -> Path:
    """The same resolution checks 5 and 11 use, repeated rather than imported so
    a reader of this script does not have to open `checks.py` to learn where it
    reads from."""
    return Path(os.environ.get("ALCHEMIST_VAULT", Path.home() / "Documents" / "Repos" / "vault"))


def recast_root() -> Path:
    """The credit recast the corpus derives its trunk from, which is a different
    series to the summer-school originals the vault holds under the same lecture
    numbers. `notes/l01-anchor-finding-2026-09-14.md` records what that split
    cost three Phase 2 batches."""
    default = Path.home() / "Documents" / "Repos" / "actuarial_deep_learning" / "credit_lectures"
    return Path(os.environ.get("ALCHEMIST_RECAST", default))


def normalise(text: str) -> str:
    """British and American spellings of the same word must score the same. The
    vault's course extractions write "regularization" while the corpus writes
    "regularisation", and a term that misses on the z is a false positive at the
    top of the ranking."""
    return text.lower().replace("ization", "isation").replace("izing", "ising").replace("ize", "ise")


def subject_terms(node: Node) -> list[str]:
    """The node's own id and title carry its subject, and nothing else here
    does: the body is a stub of two or three sentences whose vocabulary was
    written from the anchor and would therefore score itself."""
    words = re.split(r"[^a-z]+", normalise(f"{node.id} {node.title}"))
    seen: dict[str, None] = {}
    for word in words:
        # Three letters, not four. The corpus names the quantities it cares
        # most about in three: ead, lgd, pd and irb were all being dropped from
        # their own nodes' subject before 17 September 2026.
        if len(word) >= 3 and word not in STOPWORDS:
            seen[word] = None
    return list(seen)


def acronym(node: Node) -> str | None:
    """The id's initials, where they could plausibly be how a source writes the
    term. It counts only when it is found: an id whose initials nobody uses,
    such as multiple-external-ratings-treatment, would otherwise carry a term
    that can never match and depress every such node's coverage equally."""
    initials = "".join(word[0] for word in node.id.split("-") if word)
    return initials if 2 <= len(initials) <= 4 else None


def count_term(term: str, text: str) -> int:
    """Occurrences of a term, allowing the ordinary inflections. Anchored at the
    front of a word only, so "rate" does not match "corporate".

    Counted twice, once against the text as written and once with the hyphens
    closed up, taking whichever is larger. A node id splits into whole words, so
    `backpropagation` can never match a source writing "back-propagation",
    while closing every hyphen would break "risk-weighted" for the term "risk".
    Trying both costs one pass and loses neither."""
    # A term of eight letters or more matches on its first eight, so that
    # `discriminatory` finds "discrimination". Shorter terms match whole, since
    # eight characters of a short word is the word itself and anything looser
    # matches by accident.
    stem = re.escape(term[:8]) + r"[a-z]*" if len(term) >= 8 else re.escape(term) + STEM_SUFFIX
    pattern = rf"\b{stem}\b"
    return max(
        len(re.findall(pattern, text)),
        len(re.findall(pattern, re.sub(r"(?<=[a-z])-(?=[a-z])", "", text))),
    )


@dataclass(frozen=True)
class Row:
    node_id: str
    anchor: str
    coverage: float
    depth: int
    missing: tuple[str, ...]
    note: str

    def sort_key(self) -> tuple[float, int, str]:
        return (self.coverage, self.depth, self.node_id)


def strip_bibliography(text: str) -> str:
    """Everything from a References heading onwards, dropped. A reference list
    names its subject once per cited title, which is exactly how `dropout` kept
    an anchor at a lecture that never taught it: lecture 10 cites Srivastava and
    nothing more. Citations inside running prose are left alone, because a
    sentence defining a term and citing its paper in the same breath is a real
    treatment."""
    return re.split(r"(?mi)^#+\s*References\b", text)[0]


def d424_line_ranges(lines: list[str]) -> dict[str, tuple[int, int]]:
    """Section name to a half-open line range. Sections are consecutive, so each
    ends where the next begins and the last runs to the end of the file."""
    stripped = [line.strip() for line in lines]
    starts: list[tuple[str, int]] = []
    cursor = 0
    for name, title in D424_SECTIONS:
        found = next((i for i in range(cursor, len(stripped)) if stripped[i] == title), None)
        if found is None:
            raise SystemExit(f"d424 section {name!r} not found by its title {title!r}")
        starts.append((name, found))
        cursor = found + 1
    ranges: dict[str, tuple[int, int]] = {}
    for index, (name, start) in enumerate(starts):
        end = starts[index + 1][1] if index + 1 < len(starts) else len(lines)
        ranges[name] = (start, end)
    return ranges


def paragraph_text(lines: list[str], span: tuple[int, int], number: int) -> str | None:
    """The numbered paragraph and everything up to the next number. Returns None
    where the number is absent from the section, which ranks that anchor at the
    top of the report as a plain citation error rather than a topic drift."""
    start, end = span
    opener = re.compile(rf"^{number}\.\s")
    closer = re.compile(r"^\d{1,3}\.\s")
    hits = [i for i in range(start, end) if opener.match(lines[i])]
    if not hits:
        return None
    # A numbered heading and a numbered paragraph are the same shape in this
    # extraction, so the operational risk section opens with "1. Introduction"
    # one line above "1. Operational risk is defined as...". Take the first hit
    # that reads as prose, and fall back to the first hit of any length.
    #
    # First rather than longest, which was the earlier rule and was wrong: the
    # leverage ratio section carries an annex whose paragraphs restart at one,
    # so the longest "13." in that range sat in the annex and the audit
    # reported a sound anchor as its strongest finding.
    first = next((i for i in hits if len(lines[i]) >= 60), hits[0])
    last = next((i for i in range(first + 1, end) if closer.match(lines[i])), end)
    return "\n".join(lines[first:last])


def load_d424() -> tuple[list[str], dict[str, tuple[int, int]]] | None:
    path = vault_root() / "markdown" / "bcbs" / "bcbs_d424.md"
    if not path.exists():
        return None
    lines = path.read_text(encoding="utf-8").splitlines()
    return lines, d424_line_ranges(lines)


def load_lectures() -> dict[str, dict[str, str]]:
    """Lecture number to the text of each series that holds it. Both are read,
    because a low score against one and a high score against the other is the
    l01 split showing itself rather than a bad anchor."""
    vault_dir = vault_root() / "markdown" / "courses"
    recast_dir = recast_root()
    out: dict[str, dict[str, str]] = {}
    for number, vault_name in (
        ("l01", "01-use-case"), ("l02", "02-edf-glm"), ("l03", "03-deep-learning-overview"),
        ("l04", "04-05-feed-forward-networks"), ("l05", "04-05-feed-forward-networks"),
        ("l06", "06-ensembling-entity-embedding"), ("l07", "07-balance-property-auto-calibration"),
        ("l08", "08-ice-network-regularization"), ("l09", "09-localglmnet"),
        ("l10", "10-11-attention-transformers"), ("l11", "10-11-attention-transformers"),
        ("l12", "12-foundation-models-in-context-learning"),
    ):
        series: dict[str, str] = {}
        original = vault_dir / f"2026_eth_deep-learning-actuarial-{vault_name}.md"
        if original.exists():
            series["summer school"] = normalise(strip_bibliography(original.read_text(encoding="utf-8")))
        matches = sorted(recast_dir.glob(f"{number[1:]}*.qmd")) or sorted(
            recast_dir.glob(f"{number[1:3]}-*.qmd")
        )
        if matches:
            series["credit recast"] = normalise(strip_bibliography(matches[0].read_text(encoding="utf-8")))
        if series:
            out[number] = series
    return out


def score(terms: list[str], text: str, short: str | None = None) -> tuple[float, int, tuple[str, ...]]:
    """Share of the node's subject terms present, the smallest count among those
    that are, and the terms that are absent. Depth matters as much as coverage:
    a term appearing once has been mentioned, whereas a term appearing eight
    times has been taught."""
    if not terms:
        return 1.0, 0, ()
    counts = {term: count_term(term, text) for term in terms}
    if short and (found := count_term(short, text)):
        counts[short] = found
    present = [count for count in counts.values() if count]
    missing = tuple(term for term, count in counts.items() if not count)
    return len(present) / len(terms), (min(present) if present else 0), missing


def audit(top: int) -> int:
    corpus = load_corpus(REPO)
    d424 = load_d424()
    lectures = load_lectures()

    rows: list[Row] = []
    unverifiable: dict[str, int] = {}

    for node in corpus.nodes.values():
        for anchor in node.anchor:
            if anchor == "chosen":
                continue
            body = anchor.split(".")[0]
            terms = subject_terms(node)

            if body == "bcbs":
                if d424 is None:
                    unverifiable["bcbs (vault absent)"] = unverifiable.get("bcbs (vault absent)", 0) + 1
                    continue
                lines, ranges = d424
                _, _, section, item = (anchor.split(".") + [""])[:4]
                match = re.fullmatch(r"para-(\d{1,3})", item)
                if section not in ranges or match is None:
                    rows.append(Row(node.id, anchor, 0.0, 0, (), "anchor does not name a d424 paragraph"))
                    continue
                text = paragraph_text(lines, ranges[section], int(match.group(1)))
                if text is None:
                    rows.append(Row(node.id, anchor, 0.0, 0, (), f"paragraph absent from section {section}"))
                    continue
                coverage, depth, missing = score(terms, normalise(text), acronym(node))
                rows.append(Row(node.id, anchor, coverage, depth, missing, ""))

            elif body == "ucsc":
                number = anchor.split(".")[-1]
                series = lectures.get(number)
                if not series:
                    rows.append(Row(node.id, anchor, 0.0, 0, (), f"no local text for {number}"))
                    continue
                best_name, best = "", (0.0, 0, tuple(terms))
                for name, text in series.items():
                    result = score(terms, text, acronym(node))
                    if result[:2] > best[:2]:
                        best_name, best = name, result
                spread = ""
                if len(series) == 2:
                    each = {name: score(terms, text, acronym(node))[0] for name, text in series.items()}
                    if abs(each["summer school"] - each["credit recast"]) >= 0.34:
                        spread = "series disagree, see the l01 finding"
                rows.append(Row(node.id, anchor, best[0], best[1], best[2], (f"{best_name}; {spread}".strip("; ") if best_name else "")))

            else:
                unverifiable[body] = unverifiable.get(body, 0) + 1

    rows.sort(key=Row.sort_key)

    print(f"Anchor audit over {len(corpus.nodes)} nodes\n")
    print(f"{'node':42s} {'anchor':34s} {'cover':>6s} {'depth':>6s}  note")
    print("-" * 120)
    for row in rows[:top]:
        note = row.note
        if row.missing:
            absent = ", ".join(row.missing[:4])
            note = f"{note}; absent: {absent}" if note else f"absent: {absent}"
        print(f"{row.node_id:42s} {row.anchor:34s} {row.coverage:6.2f} {row.depth:6d}  {note}")

    print(f"\n{len(rows)} anchor references audited, weakest {min(top, len(rows))} shown.")
    if unverifiable:
        total = sum(unverifiable.values())
        named = ", ".join(f"{body} {count}" for body, count in sorted(unverifiable.items()))
        print(f"{total} references unverifiable, since nobody holds the document: {named}.")
    print("This report gates nothing. Read the top of the list and rule on each by hand.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Rank verifiable anchors by topic overlap.")
    parser.add_argument("--top", type=int, default=40, help="how many of the weakest to print")
    args = parser.parse_args()
    return audit(args.top)


if __name__ == "__main__":
    raise SystemExit(main())
