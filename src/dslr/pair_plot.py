import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


HOUSES = {
    'Gryffindor': 'red',
    'Hufflepuff': 'blue',
    'Ravenclaw': 'yellow',
    'Slytherin': 'green'
}

COURSES = ['Arithmancy',
           'Astronomy',
           'Herbology',
           'Defense Against the Dark Arts',
           'Divination',
           'Muggle Studies',
           'Ancient Runes',
           'History of Magic',
           'Transfiguration',
           'Potions',
           'Care of Magical Creatures',
           'Charms',
           'Flying']


def plt_matrix(df: pd.DataFrame, courses: list[str] = COURSES,
               header='Hogwarts House', fam: dict[str, str] = HOUSES
               ) -> None:

    assert isinstance(df, pd.DataFrame), \
        f"plt_hist :WrongType: df = {type(df)}"
    assert isinstance(courses, list) and \
        all(isinstance(i, str) for i in courses), \
        f"plt_hist :WrongType: courses = {type(courses)}"

    subset = df[courses + [header]].dropna()

    g = sns.pairplot(subset, hue=header, palette=fam, corner=False,
                     plot_kws={'s': 10, 'alpha': 0.2})

    for ax in g.axes.flatten():
        if ax is not None:
            ax.set_xticklabels([])
            ax.set_yticklabels([])

    plt.suptitle("Pair Plot by House")
    plt.tight_layout()
    # plt.subplots_adjust(left=0.02, bottom=0.035, top=0.9, right=0.9)
    plt.show()
