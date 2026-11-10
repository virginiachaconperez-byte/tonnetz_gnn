"""Configuration command workflows for valid and invalid inputs."""

import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import tomllib
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
VALID_TOML = 'dataset_path = "data/raw/dcml-mozart"\nseed = 42\ncontext_length = 8\n'


class ConfigTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.input = self.root / "config.toml"
        self.output = self.root / "results/config.json"
        self.command = [
            sys.executable, str(PROJECT_ROOT / "scripts/validate_config.py"),
            "--config", str(self.input), "--output", str(self.output),
        ]

    def test_command_records_example_settings_and_protects_existing_snapshot(self):
        content = (PROJECT_ROOT / "configs/pilot.toml").read_text(encoding="utf-8")
        self.input.write_text(content, encoding="utf-8")
        result = subprocess.run(self.command, cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        snapshot = self.output.read_bytes()
        self.assertEqual(json.loads(snapshot), tomllib.loads(content))

        self.input.write_text(VALID_TOML.replace("seed = 42", "seed = 7"), encoding="utf-8")
        result = subprocess.run(self.command, cwd=self.root, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(result.stderr.strip())
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(self.output.read_bytes(), snapshot)

    def test_command_reports_invalid_inputs_without_creating_output(self):
        cases = {
            "unknown setting": VALID_TOML + "context_lenght = 8\n",
            "missing setting": VALID_TOML.replace("context_length = 8\n", ""),
            "zero context length": VALID_TOML.replace("context_length = 8", "context_length = 0"),
            "negative seed": VALID_TOML.replace("seed = 42", "seed = -1"),
            "wrong seed type": VALID_TOML.replace("seed = 42", 'seed = "42"'),
            "blank dataset path": VALID_TOML.replace("data/raw/dcml-mozart", "   "),
            "invalid TOML": "seed = [",
            "missing file": None,
        }
        for name, content in cases.items():
            with self.subTest(case=name):
                if content is None:
                    self.input.unlink(missing_ok=True)
                else:
                    self.input.write_text(content, encoding="utf-8")
                result = subprocess.run(
                    self.command, cwd=self.root, capture_output=True, text=True
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertTrue(result.stderr.strip())
                self.assertNotIn("Traceback", result.stderr)
                self.assertFalse(self.output.parent.exists())
