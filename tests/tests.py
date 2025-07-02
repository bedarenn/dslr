from dslr import read, get_mean

import matplotlib.pyplot as plt


def main():
    df = read("data/dataset_train.csv")
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    tab = []
    means = []
    for i in houses:
        fam = df[df['Hogwarts House'] == i]
        tab.append(fam)
        means.append(get_mean(fam['Astronomy'].dropna().astype(float)))

    plt.figure(figsize=(8, 4.5))
    plt.grid(axis='y')

    plt.bar(houses, means, color='blue', edgecolor='black')

    plt.title('Astronomy')
    plt.xlabel('Houses')
    plt.ylabel('Means')

    plt.show()


if __name__ == "__main__":
    main()
