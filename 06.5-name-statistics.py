import matplotlib.pyplot as plt


def get_all_years():
    with open("data/names.csv", "r") as file:
        next(file)  # skip first line
        years = []
        for line in file:
            column = line.strip().split(",")
            # assume that list of years is acsending
            if not years or years[-1] != column[2]:
                years.append(column[2])
        return years


def get_count_by_name(name, year):
    with open("data/names.csv", "r") as file:
        count = 0
        for line in file:
            column = line.strip().split(",")
            if column[1] == name and column[2] == year:
                count += int(column[5])
        return count  # this is really inefficient, but irrelevant for this exercise


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
            + " kids with name ''"
            + name
            + "'' in year "
            + year
            + "."
        )
        count.append(countForThisYear)

    plt.plot(years, count)
    plt.show()


if __name__ == "__main__":
    main()
