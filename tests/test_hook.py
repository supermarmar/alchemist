"""Tests for the hook script itself.

There is deliberately no test that `core.hooksPath` is set, because such a test
grades the developer's machine rather than the hook. The setting lives in
`.git/config`, which no clone carries, so the assertion failed on a fresh clone
and passed in CI only because the workflow set it one step earlier, which made
it tautological there. What matters is that the hook script is correct, and
`test_the_hook_actually_runs_the_checks` below covers that. The wiring command
stays in the README's clone recipe as setup guidance.
"""

import os
import stat
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def test_the_hook_is_executable():
    hook = REPO / ".githooks" / "pre-commit"
    assert hook.is_file()
    assert hook.stat().st_mode & stat.S_IXUSR


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


def test_the_hook_refuses_to_run_outside_a_repository(tmp_path):
    """`cd ""` returns 0 in bash and leaves the directory unchanged, so
    `cd "$(...)" || exit 1` never fires on an empty result. The old form also
    exits non-zero from outside a repo, but for the wrong reason: check.py is
    simply not found. So assert the guard's own message, which only the
    value-checking form can produce.
    """
    done = subprocess.run(
        ["bash", str(REPO / ".githooks" / "pre-commit")],
        cwd=tmp_path, capture_output=True, text=True,
    )
    assert done.returncode != 0
    assert "must run inside a git repository" in done.stderr
