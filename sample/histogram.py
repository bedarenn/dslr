import pandas as pd
import matplotlib.pyplot as plt


def histogram(df: pd.DataFrame, title: str, x: str, y: str) -> None:
    """
    Plot a dot graph of gived data from dataframe.
    """

    assert isinstance(df, pd.DataFrame), \
        f"plot :WrongType: df = {type(df)}"
    assert isinstance(title, str), \
        f"plot :WrongType: title = {type(title)}"
    assert isinstance(x, str), \
        f"plot :WrongType: x = {type(x)}"
    assert isinstance(y, str), \
        f"plot :WrongType: y = {type(y)}"

    plt.figure(figsize=(8, 4.5))
    plt.grid(True)

    plt.scatter(df[x], df[y], color='blue', marker='o')

    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)

    plt.show()