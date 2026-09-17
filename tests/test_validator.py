import pandas as pd
import pytest

from src.validator import validate_dataset


def test_validate_dataset_rejects_dataset_without_rows() -> None:
    empty_data = pd.DataFrame(columns=["age", "city"])

    with pytest.raises(ValueError, match="no rows"):
        validate_dataset(empty_data)


def test_validate_dataset_accepts_valid_data() -> None:
    valid_data = pd.DataFrame(
        {
            "age": [20, 30],
            "city": ["Aden", "Sanaa"],
        }
    )

    validate_dataset(valid_data)
