import pandas as pd
import matplotlib.pyplot as plt


houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
colors = ['red', 'blue', 'yellow', 'green']


def plt_hist(df: pd.DataFrame, course: str) -> None:
    """
    Plot an histogram of a course.
    """

    assert isinstance(df, pd.DataFrame), \
        f"plt_hist :WrongType: df = {type(df)}"
    assert isinstance(course, str), \
        f"plt_hist :WrongType: course = {type(course)}"

    plt.figure(figsize=(8, 4.5))
    plt.grid(True)

    for i, j in zip(houses, colors):
        tab = df[df['Hogwarts House'] == i][course].dropna()
        plt.hist(tab, bins=10, label=i, color=j, edgecolor='black', alpha=0.2)

    plt.title(course)
    plt.xlabel('Score')
    plt.ylabel('Pupils')

    plt.legend()
    plt.show()
