"""The grain audit emits numbers rather than judgements.

Inconsistent grain is invisible in a node list read once and expensive in
Phase 3. What makes it visible is a figure: this body produced 1.9 nodes per
syllabus item and that one produced 0.3.
"""

import pytest

from scripts.alchemist.grain import audit, fused_titles, requires_distribution


def test_counts_nodes_per_body_from_the_manifests():
    manifests = [
        {"body": "ifoa-cs2-2026", "items_in_document": 87, "nodes_emitted": 94},
        {"body": "ifoa-sp7-2026", "items_in_document": 24, "nodes_emitted": 8},
    ]
    report = audit(manifests)
    assert report.per_body["ifoa-cs2-2026"].ratio == pytest.approx(94 / 87)
    assert report.per_body["ifoa-sp7-2026"].ratio == pytest.approx(8 / 24)


def test_flags_a_body_outside_the_band():
    manifests = [
        {"body": "inside", "items_in_document": 100, "nodes_emitted": 120},
        {"body": "too-coarse", "items_in_document": 100, "nodes_emitted": 30},
        {"body": "too-fine", "items_in_document": 100, "nodes_emitted": 210},
    ]
    report = audit(manifests)
    assert set(report.outliers) == {"too-coarse", "too-fine"}


def test_a_body_with_no_items_recorded_is_reported_rather_than_divided():
    """A zero denominator is a manifest problem rather than a ratio of infinity."""
    report = audit([{"body": "b", "items_in_document": 0, "nodes_emitted": 40}])
    assert report.per_body["b"].ratio is None
    assert "b" in report.unmeasurable


def test_band_boundaries_are_inclusive():
    manifests = [
        {"body": "at-low", "items_in_document": 100, "nodes_emitted": 50},
        {"body": "at-high", "items_in_document": 100, "nodes_emitted": 150},
        {"body": "below-low", "items_in_document": 100, "nodes_emitted": 49},
        {"body": "above-high", "items_in_document": 100, "nodes_emitted": 151},
    ]
    report = audit(manifests)
    assert "at-low" not in report.outliers and "at-low" not in report.unmeasurable
    assert "at-high" not in report.outliers and "at-high" not in report.unmeasurable
    assert "below-low" in report.outliers
    assert "above-high" in report.outliers


def test_the_requires_distribution_counts_each_length():
    assert requires_distribution([(), ("a",), ("a", "b"), ("a", "b")]) == {0: 1, 1: 1, 2: 2}


@pytest.mark.parametrize("title,flagged", [
    ("Hazard rate", False),
    ("Estimation and forecasting", True),
    ("Copulas, dependence and tail behaviour", True),
    ("Bornhuetter-Ferguson", False),
    ("Profit and loss attribution", True),
])
def test_flags_a_title_carrying_and_or_a_comma(title, flagged):
    assert bool(fused_titles([title])) is flagged


def test_fused_titles_are_sorted_and_deduplicated():
    titles = [
        "Profit and loss attribution",
        "Estimation and forecasting",
        "Copulas, dependence and tail behaviour",
        "Estimation and forecasting",
    ]
    assert fused_titles(titles) == [
        "Copulas, dependence and tail behaviour",
        "Estimation and forecasting",
        "Profit and loss attribution",
    ]
