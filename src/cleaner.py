from dataclasses import dataclass

import pandas as pd


@dataclass
class CleaningResult:
    """Store the cleaned data and a summary of applied changes."""

    data: pd.DataFrame
    duplicates_removed: int
    missing_values_filled: int


def clean_dataset(data: pd.DataFrame) -> CleaningResult:
    """Remove duplicate rows and fill missing values."""
    cleaned_data = data.copy()

    rows_before = len(cleaned_data)
    cleaned_data = cleaned_data.drop_duplicates()
    duplicates_removed = rows_before - len(cleaned_data)

    missing_values_before = int(cleaned_data.isna().sum().sum())

    numeric_columns = cleaned_data.select_dtypes(include="number").columns
    for column in numeric_columns:
        median_value = cleaned_data[column].median()
        if pd.notna(median_value):
            cleaned_data[column] = cleaned_data[column].fillna(median_value)

    text_columns = cleaned_data.select_dtypes(exclude="number").columns
    for column in text_columns:
        cleaned_data[column] = cleaned_data[column].fillna("Unknown")

    return CleaningResult(
        data=cleaned_data,
        duplicates_removed=duplicates_removed,
        missing_values_filled=missing_values_before,
    )
