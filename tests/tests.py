from dslr import read, \
    str_data


def main():
    df = read("data/dataset_train.csv")
    print(str_data(df))


if __name__ == "__main__":
    main()
