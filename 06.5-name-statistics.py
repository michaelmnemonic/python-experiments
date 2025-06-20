# This implementation is inefficient, but irrelevant for this exercise

import matplotlib.pyplot as plt


def get_data():
    with open("data/names.csv", "r") as file:
        next(file)  # skip first line
        data = []
        for line in file:
            column = line.strip().split(",")
            data.append
    return data


def get_all_years():
    with open("data/names.csv", "r") as file:
        next(file)  # skip first line
        years = []
        for line in file:
            column = line.strip().split(",")
            if not column[2] in years:
                years.append(column[2])
        return years


def get_count_by_name(name, year):
    with open("data/names.csv", "r") as file:
        count = 0
        for line in file:
            column = line.strip().split(",")
            if column[1] == name and column[2] == year:
                count += int(column[5])
        return count


# columns in names.csv are: Id,Name,Year,Gender,State,Count
def main():
    name = "Anna"
    years = get_all_years()
    count = []
    for year in years:
        countForThisYear = get_count_by_name(name, year)
        print(
            "Found "
            + str(countForThisYear)
            + " kids with name "
            + name
            + " in year "
            + year
            + "."
        )
        count.append(countForThisYear)

    plt.plot(years, count)
    plt.tick_params(axis="x", labelrotation=270)
    plt.show()


if __name__ == "__main__":
    main()
