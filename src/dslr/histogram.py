import pandas as pd
import matplotlib.pyplot as plt


HOUSES = {
    'Gryffindor': 'red',
    'Hufflepuff': 'blue',
    'Ravenclaw': 'yellow',
    'Slytherin': 'green'
}


def plt_hist(df: pd.DataFrame, course: str,
             header='Hogwarts House', fam=HOUSES) -> None:
    """
    Plot an histogram of a course.
    """

    assert isinstance(df, pd.DataFrame), \
        f"plt_hist :WrongType: df = {type(df)}"
    assert isinstance(course, str), \
        f"plt_hist :WrongType: course = {type(course)}"

    plt.figure(figsize=(8, 4.5))
    plt.grid(True)

    for key, value in fam.items():
        tab = df[df[header] == key][course].dropna()
        plt.hist(tab, bins=10,
                 label=key, color=value, edgecolor='black',
                 alpha=0.2)

    plt.title(course)
    plt.xlabel('Score')
    plt.ylabel('Pupils')

    plt.legend()
    plt.show()
