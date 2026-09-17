from pathlib import Path

import pandas as pd

from src.cleaner import CleaningResult


def create_cleaning_report(
    original_data: pd.DataFrame,
    result: CleaningResult,
    input_path: Path,
    output_path: Path,
) -> str:
    """Create a human-readable summary of the cleaning process."""
    missing_values = original_data.isna().sum()

    missing_lines = [
        f"- {column}: {count}"
        for column, count in missing_values.items()
        if count > 0
    ]

    if not missing_lines:
        missing_lines = ["- No missing values found."]

    report_lines = [
        "AI Data Cleaner - Cleaning Report",
        "=" * 35,
        f"Input file: {input_path}",
        f"Output file: {output_path}",
        "",
        f"Rows before cleaning: {len(original_data)}",
        f"Rows after cleaning: {len(result.data)}",
        f"Duplicate rows removed: {result.duplicates_removed}",
        f"Missing values filled: {result.missing_values_filled}",
        "",
        "Missing values before cleaning:",
        *missing_lines,
    ]

    return "\n".join(report_lines)


def save_report(report_content: str, report_path: Path) -> None:
    """Save the cleaning report as a UTF-8 text file."""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_content, encoding="utf-8")
