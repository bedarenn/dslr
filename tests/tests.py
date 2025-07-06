from dslr import read, plt_matrix, str_data


def main():
    df = read("data/dataset_train.csv")

    COURSES = ['Astronomy',
               'Herbology',
               'Defense Against the Dark Arts',
               'Ancient Runes']

    plt_matrix(df, courses=COURSES)


if __name__ == "__main__":
    main()
