# tests/test_checks_titles.py
from pathlib import Path

from scripts.alchemist.checks import check_titles_sentence_case
from scripts.alchemist.model import Corpus, Node


def node(node_id: str, title: str) -> Node:
    return Node(
        id=node_id, title=title, domains=("stats",), status="stub", requires=(), spends=(),
        anchor=(), vault_articles=(), vault_sources=(), taught_in=None, body="",
        path=Path(f"nodes/{node_id}.md"),
    )


def failures(*titles: str) -> list[str]:
    corpus = Corpus({f"n{i}": node(f"n{i}", t) for i, t in enumerate(titles)}, {})
    return check_titles_sentence_case(corpus).failures


def test_a_capitalised_common_noun_fails_and_is_named():
    result = failures("Tail Value at Risk")
    assert len(result) == 1 and "Value" in result[0] and "Risk" in result[0]


def test_sentence_case_passes():
    assert failures("Tail value at risk", "t-distribution", "Weaknesses of value at risk") == []


def test_a_proper_name_on_the_list_passes():
    assert failures("Compound Poisson process", "Shortcomings of the Basel Accord") == []


def test_an_acronym_a_roman_numeral_and_a_single_letter_pass():
    assert failures("Addressing NSFR compliance", "Tier II capital", "Capital buffer versus CCoB plus CCyB", "Distribution of the F-statistic") == []


def test_a_possessive_name_and_a_hyphenated_pair_of_names_pass():
    assert failures("Assumptions underlying Black's model", "Bolzano-Weierstrass and Heine-Borel theorems", "Wave equation and Laplace's equation") == []


def test_a_bracketed_acronym_passes():
    assert failures("Bond stripping (STRIPS)") == []


def test_a_name_off_the_list_fails_so_the_list_is_the_only_exemption():
    assert len(failures("The Keynesian cross")) == 1


def test_the_first_word_is_free():
    assert failures("Keynesian multiplier", "ILAAP") == []


def test_a_hyphenated_name_with_a_lowercase_partner_passes():
    """Markov-chain has one capital, so without splitting on the hyphen the
    whole compound would be checked against the list and flagged."""
    assert failures("Simulation of a Markov-chain model") == []
