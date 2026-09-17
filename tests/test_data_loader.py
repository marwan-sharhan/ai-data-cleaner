import pytest

from src.data_loader import load_csv


def test_load_csv_raises_error_for_missing_file(tmp_path) -> None:
    missing_file = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError, match="File not found"):
        load_csv(missing_file)
