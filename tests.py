from sample import read, \
    scatter_plot


def main():
    df = read("data/dataset_test.csv")
    scatter_plot(df, 'Hogwarts', 'Index', 'Astronomy')


if __name__ == "__main__":
    main()
