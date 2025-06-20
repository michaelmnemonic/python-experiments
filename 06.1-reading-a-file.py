def main():
    name_of_file = "read.text"

    file = open ("data/read.txt", "r")
    for line in file:
        # Remove trailing newline characters from each line before printing
        # to avoid adding extra newlines
        print(line.strip())

    file = open("data/write.txt", "w")
    file.write("This is an example line of text.")
    file.write("\n")
    file.close()

if __name__ == "__main__":
    main()