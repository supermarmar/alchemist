from pathlib import Path

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
    root = fake_repo(tmp_path)
    (root / "assets" / "lecture.css").unlink()
    try:
        inline(root / "lectures" / "L.html", root)
    except FileNotFoundError as exc:
        assert "lecture.css" in str(exc)
    else:
        raise AssertionError("expected FileNotFoundError")
