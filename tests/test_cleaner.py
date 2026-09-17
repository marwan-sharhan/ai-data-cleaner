import pandas as pd

from src.cleaner import clean_dataset


def test_clean_dataset_removes_duplicates_and_fills_missing_values() -> None:
    raw_data = pd.DataFrame(
        {
            "customer_id": [1, 2, 3, 2],
            "age": [20.0, 30.0, None, 30.0],
            "city": ["Aden", "Sanaa", None, "Sanaa"],
        }
    )

    result = clean_dataset(raw_data)

    assert result.duplicates_removed == 1
    assert result.missing_values_filled == 2
    assert len(result.data) == 3

    khaled_row = result.data.loc[result.data["customer_id"] == 3].iloc[0]

    assert khaled_row["age"] == 25.0
    assert khaled_row["city"] == "Unknown"
