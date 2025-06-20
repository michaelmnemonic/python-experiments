
def main():
    with open("data/data.csv", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[2] == "BER" or data[2] == "BUD":
                print(data[0] + ": "+ data[1])

if __name__ == "__main__":
    main()