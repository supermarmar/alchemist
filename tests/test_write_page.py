import subprocess
import sys
from pathlib import Path

from conftest import PAGE_BODY, write_stub
from scripts.alchemist.model import Spend, parse_node

REPO = Path(__file__).resolve().parents[1]


def run(root, *args):
    return subprocess.run(
        [sys.executable, "scripts/write_page.py", "--root", str(root), *args],
        capture_output=True, text=True, cwd=REPO,
    )


def body_file(tmp_path, text=PAGE_BODY):
    path = tmp_path / "body.md"
    path.write_text(text)
    return str(path)


def test_it_writes_a_page_and_reports_the_spends(page_repo, tmp_path):
    write_stub(page_repo, "hazard")
    result = run(page_repo, "--node", "hazard", "--body", body_file(tmp_path),
                 "--spends", "obj.hazard:credit")
    assert result.returncode == 0, result.stderr
    assert "hazard: drafted, 1 spends declared" in result.stdout
    node = parse_node(page_repo / "nodes" / "hazard.md")
    assert node.status == "drafted" and node.spends == (Spend("obj.hazard", "credit"),)


def test_check_alone_writes_nothing_and_exits_2_on_a_breach(page_repo, tmp_path):
    broken = body_file(tmp_path, PAGE_BODY.replace("## The expression", "## Formula"))
    result = run(page_repo, "--check", broken)
    assert result.returncode == 2 and "in that order" in result.stderr
    result = run(page_repo, "--check", body_file(tmp_path))
    assert result.returncode == 0 and "conforms" in result.stdout
    assert not list((page_repo / "nodes").iterdir())


def test_a_refused_spend_leaves_the_node_a_stub(page_repo, tmp_path):
    write_stub(page_repo, "hazard")
    result = run(page_repo, "--node", "hazard", "--body", body_file(tmp_path),
                 "--spends", "obj.ghost:credit")
    assert result.returncode == 2 and "unknown object" in result.stderr
    assert parse_node(page_repo / "nodes" / "hazard.md").status == "stub"


def test_a_malformed_spend_is_refused(page_repo, tmp_path):
    write_stub(page_repo, "hazard")
    result = run(page_repo, "--node", "hazard", "--body", body_file(tmp_path),
                 "--spends", "obj.hazard")
    assert result.returncode == 2 and "object:domain" in result.stderr


def test_a_reviewed_node_needs_force(page_repo, tmp_path):
    write_stub(page_repo, "hazard", status="reviewed")
    body = body_file(tmp_path)
    assert run(page_repo, "--node", "hazard", "--body", body).returncode == 2
    assert run(page_repo, "--node", "hazard", "--body", body, "--force").returncode == 0
    assert parse_node(page_repo / "nodes" / "hazard.md").status == "drafted"


def test_an_unknown_node_is_refused(page_repo, tmp_path):
    result = run(page_repo, "--node", "ghost", "--body", body_file(tmp_path))
    assert result.returncode == 2 and "no such node" in result.stderr


def test_omitting_node_or_body_without_check_is_an_error(page_repo):
    result = run(page_repo, "--node", "hazard")
    assert result.returncode == 2 and "--node and --body are required" in result.stderr
