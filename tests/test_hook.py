import os
import stat
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def test_the_hook_is_executable():
    hook = REPO / ".githooks" / "pre-commit"
    assert hook.is_file()
    assert hook.stat().st_mode & stat.S_IXUSR


def test_git_is_configured_to_use_it():
    done = subprocess.run(
        ["git", "config", "core.hooksPath"], cwd=REPO, capture_output=True, text=True
    )
    assert done.stdout.strip() == ".githooks"


def test_the_hook_passes_on_the_current_tree():
    done = subprocess.run(
        ["bash", ".githooks/pre-commit"], cwd=REPO, capture_output=True, text=True,
        env={**os.environ},
    )
    assert done.returncode == 0, done.stdout + done.stderr


def test_the_hook_actually_runs_the_checks():
    """The tree test above passes against a hook whose body is just `exit 0`.
    Assert the checker's own output, which appears only if check.py really ran.
    """
    done = subprocess.run(
        ["bash", ".githooks/pre-commit"], cwd=REPO, capture_output=True, text=True,
        env={**os.environ},
    )
    assert done.returncode == 0, done.stdout + done.stderr
    assert "declared symbols resolve" in done.stdout
    assert "nodes," in done.stdout
