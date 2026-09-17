from pathlib import Path

import pandas as pd

from src.data_loader import load_csv


def print_basic_summary(data: pd.DataFrame) -> None:
    """Print a concise summary of a dataset."""
    print("Dataset summary")
    print("-" * 30)
    print(f"Rows: {len(data)}")
    print(f"Columns: {len(data.columns)}")

    print("\nColumn names:")
    print(", ".join(data.columns))

    print("\nMissing values per column:")
    print(data.isna().sum().to_string())

    print("\nDuplicate rows:")
    print(data.duplicated().sum())


def main() -> int:
    """Run the initial data-inspection workflow."""
    input_path = Path("data/raw/customers.csv")

    try:
        data = load_csv(input_path)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return 1

    print_basic_summary(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
