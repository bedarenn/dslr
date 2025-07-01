import pandas as pd
from typing import Callable
from pandas import Series

from .stat import \
    get_count, get_mean, \
    get_min, get_max, \
    get_median, get_quartile_1, get_quartile_3


SIZE = 10


def str_data(df: pd.DataFrame, size: int = SIZE) -> str:
    """
    Return a str that contain all stat of a dataframe.
    """

    assert isinstance(df, pd.DataFrame), \
        f"str_data :WrongType: df = {type(df)}"
    assert isinstance(size, int), \
        f"str_data :WrongType: size = {type(size)}"

    name = [
        col for col in df.columns
        if not df[col].dropna().empty and
        pd.api.types.is_numeric_dtype(df[col])
    ]
    text = "Name".rjust(size) + "  "
    cols = {}
    for i in name:
        text += f"{i[:size].rjust(size)}  "
        cols[i] = df[i].dropna().astype(float)
    text += "\n"

    text += "Count".rjust(size) + "  " + \
        write_line(cols, name, get_count, size=size) + "\n"
    text += "Mean".rjust(size) + "  " + \
        write_line(cols, name, get_mean, size=size) + "\n"
    text += "Min".rjust(size) + "  " + \
        write_line(cols, name, get_min, size=size) + "\n"
    text += "25%".rjust(size) + "  " + \
        write_line(cols, name, get_quartile_3, size=size) + "\n"
    text += "50%".rjust(size) + "  " + \
        write_line(cols, name, get_median, size=size) + "\n"
    text += "75%".rjust(size) + "  " + \
        write_line(cols, name, get_quartile_1, size=size) + "\n"
    text += "Max".rjust(size) + "  " + \
        write_line(cols, name, get_max, size=size) + "\n"

    return (text)


def write_line(df: dict, name: list[str],
               func: Callable[[Series], float],
               size: int = SIZE) -> str:

    assert isinstance(df, dict), \
        f"write_line :WrongType: df = {type(df)}"
    assert isinstance(name, list) and all(isinstance(i, str) for i in name), \
        f"write_line :WrongType: name = {type(name)}"
    assert isinstance(func, Callable), \
        f"write_line :WrongType: func = {type(func)}"

    text = ""
    for i in name:
        s = f"{func(df[i]): {size}.2f}"
        text += f"{s[:size].rjust(size)}  "
    return (text)
