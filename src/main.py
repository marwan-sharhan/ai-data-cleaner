import argparse
from pathlib import Path

import pandas as pd

from src.cleaner import CleaningResult, clean_dataset
from src.data_loader import load_csv
from src.reporter import create_cleaning_report, save_report
from src.validator import validate_dataset


def parse_arguments() -> argparse.Namespace:
    """Read command-line arguments supplied by the user."""
    parser = argparse.ArgumentParser(description="Inspect and clean a CSV dataset.")

    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the raw CSV file.",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/cleaned_data.csv"),
        help="Path for the cleaned CSV file.",
    )

    parser.add_argument(
        "--report",
        type=Path,
        default=Path("reports/cleaning_report.txt"),
        help="Path for the cleaning report.",
    )

    return parser.parse_args()


def print_basic_summary(data: pd.DataFrame) -> None:
    """Print a concise summary of a dataset."""
    print("Dataset summary")
    print("-" * 30)
    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")

    print("\nMissing values per column:")
    print(data.isna().sum().to_string())

    print("\nDuplicate rows:")
    print(data.duplicated().sum())


def print_cleaning_summary(result: CleaningResult) -> None:
    """Print the changes made during cleaning."""
    print("\nCleaning summary")
    print("-" * 30)
    print(f"Duplicate rows removed: {result.duplicates_removed}")
    print(f"Missing values filled: {result.missing_values_filled}")
    print(f"Final number of rows: {len(result.data)}")


def main() -> int:
    """Run the data inspection and cleaning workflow."""
    arguments = parse_arguments()

    try:
        raw_data = load_csv(arguments.input_file)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return 1

    print_basic_summary(raw_data)

    result = clean_dataset(raw_data)
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    result.data.to_csv(arguments.output, index=False)

    report_content = create_cleaning_report(
        original_data=raw_data,
        result=result,
        input_path=arguments.input_file,
        output_path=arguments.output,
    )
    save_report(report_content, arguments.report)

    print_cleaning_summary(result)
    print(f"\nCleaned file saved to: {arguments.output}")
    print(f"Report saved to: {arguments.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
