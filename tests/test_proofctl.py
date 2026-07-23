from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SOURCE_ROOT = Path(__file__).resolve().parents[1]


class ProofctlIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name) / "repo"
        shutil.copytree(
            SOURCE_ROOT,
            self.root,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
        )
        self.script = self.root / "scripts" / "proofctl.py"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_cli(
        self, *arguments: str, expected_returncode: int = 0
    ) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [
                sys.executable,
                str(self.script),
                "--root",
                str(self.root),
                *arguments,
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(
            result.returncode,
            expected_returncode,
            msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}",
        )
        return result

    def test_empty_scaffold_validates(self) -> None:
        result = self.run_cli("validate")
        self.assertIn("Validation passed", result.stdout)

    def test_new_problem_records_and_status(self) -> None:
        self.run_cli(
            "new",
            "test-problem",
            "--title",
            "Test | Problem",
            "--statement",
            "For every integer n, n = n.",
        )
        self.run_cli("add", "test-problem", "session", "Initial audit")
        self.run_cli("add", "test-problem", "attempt", "Direct proof")
        self.run_cli(
            "set-status",
            "test-problem",
            "active",
            "--claim",
            "open",
            "--next",
            "Prove C001 from reflexivity.",
        )
        self.run_cli("validate")

        manifest = json.loads(
            (self.root / "problems" / "test-problem" / "problem.json").read_text()
        )
        self.assertEqual(manifest["id"], "P-001")
        self.assertEqual(manifest["work_status"], "active")
        self.assertTrue(
            list(
                (self.root / "problems" / "test-problem" / "sessions").glob(
                    "S001-*.md"
                )
            )
        )
        index = (self.root / "problems" / "INDEX.md").read_text()
        self.assertIn("Test \\| Problem", index)

    def test_completion_gate_rejects_unreviewed_candidate(self) -> None:
        self.run_cli("new", "gate-test", "--title", "Gate test")
        result = self.run_cli(
            "set-status",
            "gate-test",
            "complete",
            "--claim",
            "proved",
            expected_returncode=2,
        )
        self.assertIn("unresolved obligations", result.stderr)
        self.assertIn("requires 2 review record", result.stderr)
        self.assertIn("integrated candidate", result.stderr)

        manifest = json.loads(
            (self.root / "problems" / "gate-test" / "problem.json").read_text()
        )
        self.assertEqual(manifest["work_status"], "intake")
        self.assertEqual(manifest["claim_status"], "open")

    def test_stale_index_is_detected(self) -> None:
        self.run_cli("new", "index-test", "--title", "Index test")
        index_path = self.root / "problems" / "INDEX.md"
        index_path.write_text(index_path.read_text() + "stale\n")
        result = self.run_cli("validate", expected_returncode=1)
        self.assertIn("INDEX.md is stale", result.stderr)


if __name__ == "__main__":
    unittest.main()

