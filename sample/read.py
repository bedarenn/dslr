import pandas as pd


def read(filename: str) -> pd.DataFrame:
    """
    Read CSV and return Dataframe.
    """

    assert isinstance(filename, str), \
        f"read :WrongType: filename = {type(filename)}"

    df = pd.read_csv(filename)
    return (df)
