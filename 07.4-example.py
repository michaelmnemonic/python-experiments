def get_data():
    with open("data/names.csv", "r") as file:
        next(file)  # skip first line
        # columns in names.csv are: Id,Name,Year,Gender,State,Count
        data = []
        for line in file:
            data.append(line.strip().split(","))
    return data


def count_occurance_of_names(data):
    names = {}
    for line in data:
        if line[1] not in names:
            names[line[1]] = int(line[5])
        else:
            names[line[1]] = names[line[1]] + int(line[5])
    return names


def main():
    data = get_data()
    names = count_occurance_of_names(data)
    most_used_name = ""
    max = 0
    for name, count in names.items():
        if count > max:
            most_used_name = name
            max = count
    print(
        "The most used name is: " + most_used_name + " with " + str(max) + " occurances"
    )


if __name__ == "__main__":
    main()
