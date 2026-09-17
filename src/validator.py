import pandas as pd


def validate_dataset(data: pd.DataFrame) -> None:
    """Ensure that a dataset contains usable rows and columns."""
    if data.shape[1] == 0:
        raise ValueError("The dataset contains no columns.")

    if data.shape[0] == 0:
        raise ValueError("The dataset contains no rows.")
