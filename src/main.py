from pathlib import Path

import pandas as pd

from src.cleaner import CleaningResult, clean_dataset
from src.data_loader import load_csv
from src.reporter import create_cleaning_report, save_report


INPUT_PATH = Path("data/raw/customers.csv")
OUTPUT_PATH = Path("data/processed/customers_clean.csv")
REPORT_PATH = Path("reports/cleaning_report.txt")


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
    try:
        raw_data = load_csv(INPUT_PATH)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return 1

    print_basic_summary(raw_data)

    result = clean_dataset(raw_data)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    result.data.to_csv(OUTPUT_PATH, index=False)

    report_content = create_cleaning_report(
        original_data=raw_data,
        result=result,
        input_path=INPUT_PATH,
        output_path=OUTPUT_PATH,
    )
    save_report(report_content, REPORT_PATH)

    print_cleaning_summary(result)
    print(f"\nCleaned file saved to: {OUTPUT_PATH}")
    print(f"Report saved to: {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
