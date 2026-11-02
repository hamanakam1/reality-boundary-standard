"""Boundary and integrity tests for the informative repository tools."""

import csv
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from build_catalog import catalog, generated_files
from check_repository import inventory, link_errors
from new_assessment import write_matrix


class CatalogTests(unittest.TestCase):
    def test_complete_catalog_is_bound_to_exact_normative_bytes(self):
        source = (ROOT / "standard/STANDARD.md").read_bytes()
        result = catalog(source)
        self.assertEqual(result["source_sha256"], hashlib.sha256(source).hexdigest())
        self.assertEqual(len(result["requirements"]), 118)
        self.assertFalse(result["normative"])
        for row in result["requirements"]:
            self.assertTrue(source.decode().splitlines()[row["source_line"] - 1].startswith("**" + row["id"]))

    def test_duplicate_or_malformed_ids_fail_instead_of_disappearing(self):
        for lines in (
            "**RBS-ONE-01.** MUST do A.\n\n**RBS-ONE-01.** MUST do B.",
            "**RBS-ONE-1.** MUST do A.",
        ):
            with self.subTest(lines=lines), self.assertRaises(ValueError):
                catalog(("**Version:** 0.1.0-draft\n## 1. Scope\n\n" + lines).encode())

    def test_wrapped_paragraphs_and_mixed_keywords_are_preserved(self):
        data = catalog(b"**Version:** 0.1.0-draft\n## 1. Scope\n\n**RBS-ONE-01.** MUST do A.\nSHOULD NOT do B.\n\n")
        row = data["requirements"][0]
        self.assertEqual(row["text"], "MUST do A. SHOULD NOT do B.")
        self.assertEqual(row["keywords"], ["MUST", "SHOULD NOT"])

    def test_missing_version_or_empty_catalog_cannot_pass(self):
        for source in (b"## Scope\n", b"**Version:** 0.1.0-draft\n"):
            with self.subTest(source=source), self.assertRaises(ValueError):
                catalog(source)

    def test_generated_explorer_escapes_script_terminators(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "standard").mkdir()
            (root / "tools").mkdir()
            (root / "standard/STANDARD.md").write_text("**Version:** 0.1.0-draft\n## Scope\n\n**RBS-ONE-01.** MUST preserve </script> literally.\n")
            (root / "tools/explorer.template.html").write_text("<script>__RBS_CATALOG__</script>")
            output = generated_files(root)["docs/explorer.html"]
            self.assertEqual(output.count("</script>"), 1)
            self.assertIn("\\u003c/script>", output)


class AssessmentTests(unittest.TestCase):
    def test_matrix_starts_every_requirement_unreviewed_and_unknown(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "assessment.csv"
            self.assertEqual(write_matrix(output, "Export v2, staging", date(2026, 11, 1)), 118)
            with output.open(newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 118)
            self.assertEqual({r["result"] for r in rows}, {"UNKNOWN"})
            self.assertEqual({r["applicability"] for r in rows}, {"UNREVIEWED"})
            self.assertEqual({r["scope"] for r in rows}, {"Export v2, staging"})
            self.assertTrue(all(not r["reviewer"] and not r["evidence_ids"] for r in rows))

    def test_existing_assessment_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "existing.csv"
            output.write_text("completed human review")
            with self.assertRaises(FileExistsError):
                write_matrix(output, "scope", date(2026, 11, 1))
            self.assertEqual(output.read_text(), "completed human review")

    def test_blank_scope_does_not_create_an_artifact(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "invalid.csv"
            with self.assertRaises(ValueError):
                write_matrix(output, "  ", date(2026, 11, 1))
            self.assertFalse(output.exists())


class IntegrityTests(unittest.TestCase):
    def test_manifest_detects_modified_and_added_files(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "a.md").write_text("before")
            first = inventory(root)
            (root / "a.md").write_text("after")
            self.assertNotEqual(first, inventory(root))
            (root / "b.md").write_text("new")
            self.assertEqual(len(inventory(root)["files"]), 2)

    def test_manifest_rejects_symlinks_and_excludes_local_output(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / ".artifacts").mkdir()
            (root / ".artifacts/private.json").write_text("local output")
            self.assertEqual(inventory(root)["files"], [])
            (root / "link").symlink_to(root / ".artifacts/private.json")
            with self.assertRaises(ValueError):
                inventory(root)

    def test_links_check_targets_anchors_and_package_boundary(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "target.md").write_text("# Correct heading\n")
            (root / "README.md").write_text("[good](target.md#correct-heading)\n[bad](missing.md)\n[anchor](target.md#wrong)\n[out](../outside.md)\n")
            errors = link_errors(root)
            self.assertEqual(len(errors), 3)
            self.assertIn("missing link target", errors[0])
            self.assertTrue(any("heading anchor" in error for error in errors))
            self.assertTrue(any("leaves the source package" in error for error in errors))

    def test_catalog_check_detects_drift_without_writing(self):
        # The real CLI must accept the committed generated artifacts.
        result = subprocess.run([sys.executable, str(ROOT / "tools/build_catalog.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
