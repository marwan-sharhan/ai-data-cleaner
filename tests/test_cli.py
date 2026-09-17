from pathlib import Path
import subprocess
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_cli(*arguments: str) -> subprocess.CompletedProcess[str]:
    """Run the application as a user would run it from the terminal."""
    return subprocess.run(
        [sys.executable, "-m", "src.main", *arguments],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_cli_help_exits_successfully() -> None:
    result = run_cli("--help")

    assert result.returncode == 0
    assert "Inspect and clean a CSV dataset." in result.stdout


def test_cli_returns_error_for_missing_file() -> None:
    result = run_cli("missing_file.csv")

    assert result.returncode == 1
    assert "Error: File not found" in result.stdout
