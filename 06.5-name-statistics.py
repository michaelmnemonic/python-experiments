# This implementation is inefficient, but irrelevant for this exercise

import matplotlib.pyplot as plt


def get_data():
    with open("data/names.csv", "r") as file:
        next(file)  # skip first line
        data = []
        for line in file:
            data.append(line.strip().split(","))
    return data


def get_all_years(data):
    years = []
    for line in data:
        if not line[2] in years:
            years.append(line[2])
    return years


def get_count_by_name(data, name, year):
    count = 0
    for line in data:
        if line[1] == name and line[2] == year:
            count += int(line[5])
    return count


# columns in names.csv are: Id,Name,Year,Gender,State,Count
def main():
    name = "Anna"
    data = get_data()
    years = get_all_years(data)
    count = []
    for year in years:
        countForThisYear = get_count_by_name(data, name, year)
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
