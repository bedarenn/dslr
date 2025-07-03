from dslr import read, plt_hist


def main():
    df = read("data/dataset_train.csv")
    plt_hist(df, 'Defense Against the Dark Arts')


if __name__ == "__main__":
    main()
