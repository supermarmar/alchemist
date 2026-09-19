"""The audit reports rather than gates, so nothing else catches it going wrong.

Two of these tests exist because the code was wrong in exactly that way on 17
September 2026: the longest-match rule read an annex paragraph and reported a
sound leverage ratio anchor as the corpus's worst, and a whole-word rule could
not see "back-propagation" from a node called `backpropagation`.
"""

from pathlib import Path

from scripts.alchemist.model import Node
from scripts.anchor_audit import (
    acronym,
    normalise,
    count_term,
    d424_line_ranges,
    paragraph_text,
    score,
    strip_bibliography,
    subject_terms,
)

SECTION_TITLES = [
    "Introduction",
    "Standardised approach for credit risk",
    "Internal ratings-based approach for credit risk",
    "Minimum capital requirements for CVA risk",
    "Minimum capital requirements for operational risk",
    "Output floor",
    "Leverage ratio",
]


def _node(node_id: str, title: str) -> Node:
    return Node(
        id=node_id, title=title, domains=("credit",), status="stub", requires=(), spends=(),
        anchor=("chosen",), vault_articles=(), vault_sources=(), taught_in=None, body="A stub.",
        path=Path(f"nodes/{node_id}.md"),
    )


def _document() -> list[str]:
    """A miniature d424: a table of contents naming Output floor before the
    section itself, then the seven sections in order."""
    lines = ["Contents", "Output floor", "Leverage ratio"]
    for title in SECTION_TITLES:
        lines += [title, f"1. Opening paragraph of {title}, long enough to read as prose rather than a heading."]
    return lines


def test_section_ranges_ignore_the_table_of_contents():
    ranges = d424_line_ranges(_document())
    assert list(ranges) == ["intro", "sa", "irb", "cva", "oprisk", "floor", "lr"]
    assert ranges["floor"][0] > ranges["oprisk"][0]
    for name, (start, end) in ranges.items():
        assert start < end, name


def test_sections_are_consecutive_and_cover_the_document():
    document = _document()
    ranges = d424_line_ranges(document)
    ordered = sorted(ranges.values())
    assert ordered[-1][1] == len(document)
    for (_, end), (start, _) in zip(ordered, ordered[1:]):
        assert end == start


def test_a_numbered_heading_does_not_win_over_the_paragraph():
    lines = ["1. Introduction", "1. Operational risk is defined as the risk of loss resulting from failed processes.", "2. The next one."]
    text = paragraph_text(lines, (0, len(lines)), 1)
    assert text is not None and text.startswith("1. Operational risk")


def test_the_first_prose_match_wins_rather_than_the_longest():
    """The leverage ratio section carries an annex whose paragraphs restart at
    one, so the longest 13 in that range is the annex's."""
    lines = [
        "13. The implementation timeline for the leverage ratio requirement is as follows:",
        "14. Something else entirely.",
        "Annex",
        "13. A 20% CCF will be applied to both the issuing and confirming banks of trade letters of credit, at greater length.",
    ]
    text = paragraph_text(lines, (0, len(lines)), 13)
    assert text is not None and "implementation timeline" in text


def test_an_absent_paragraph_is_reported_rather_than_guessed():
    lines = ["1. The only paragraph here, written at sufficient length to read as prose."]
    assert paragraph_text(lines, (0, len(lines)), 44) is None


def test_a_paragraph_stops_at_the_next_number():
    lines = ["7. The paragraph that matters, long enough to count as prose rather than a heading.", "continued", "8. The next."]
    text = paragraph_text(lines, (0, len(lines)), 7)
    assert text is not None and "continued" in text and "8. The next" not in text


def test_a_term_matches_across_a_hyphen():
    assert count_term("backpropagation", "the back-propagation step") == 1


def test_a_long_term_matches_its_relatives():
    assert count_term("discriminatory", "the discrimination measured on the test set") == 1


def test_a_short_term_does_not_match_inside_a_word():
    assert count_term("rate", "corporate exposures") == 0
    assert count_term("rate", "the rates applied") == 1


def test_three_letter_terms_survive():
    assert "ead" in subject_terms(_node("ead-quantification-standards", "EAD quantification standards"))


def test_stopwords_do_not_carry_subject():
    terms = subject_terms(_node("requirements-for-the-approach", "Requirements for the approach"))
    assert terms == []


def test_an_acronym_is_only_offered_at_a_plausible_length():
    assert acronym(_node("loss-given-default", "Loss given default")) == "lgd"
    assert acronym(_node("backpropagation", "Backpropagation")) is None
    assert acronym(_node("a-very-long-node-id-indeed-here", "Long")) is None


def test_an_absent_acronym_costs_nothing():
    """Otherwise every node whose initials nobody writes carries a term that can
    never match, and they all rank weak together."""
    terms = ["loss", "given", "default"]
    with_acronym = score(terms, "the lgd estimate", "lgd")
    without = score(terms, "the lgd estimate", "mert")
    assert with_acronym[0] > 0
    assert without[0] == 0


def test_a_bibliography_does_not_count_as_teaching():
    """Scoring runs on normalised text, so the test does too: the pipeline
    lowercases before it counts."""
    text = normalise("Early stopping is used here.\n\n## References\n\nSrivastava, N. (2014). Dropout: a simple way.\n")
    assert count_term("dropout", strip_bibliography(text)) == 0
    assert count_term("dropout", text) == 1
