import pandas as pd
import matplotlib.pyplot as plt


COLORS = ['red', 'blue']


def plt_scatter(df: pd.DataFrame, course1: str, course2: str,
                colors=COLORS) -> None:
    """
    Plot a scatter plot of two course.
    """

    assert isinstance(df, pd.DataFrame), \
        f"plt_hist :WrongType: df = {type(df)}"
    assert isinstance(course1, str), \
        f"plt_hist :WrongType: course1 = {type(course1)}"
    assert isinstance(course2, str), \
        f"plt_hist :WrongType: course2 = {type(course2)}"

    plt.figure(figsize=(8, 4.5))
    plt.grid(True)

    mask = mask_iqr(df, course1) & mask_iqr(df, course2)

    plt.scatter(df.loc[mask, course1], df.loc[mask, course2],
                color=colors[1], alpha=0.5)

    plt.title(course1 + " VS." + course2)
    plt.xlabel(course1)
    plt.ylabel(course2)

    plt.show()


def mask_iqr(df, col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return (df[col] >= lower) & (df[col] <= upper)
