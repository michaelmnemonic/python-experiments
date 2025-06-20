def main():
    # Using 'with' ensures the file is properly closed after its suite finishes, even if an error occurs during the processing of the file.
    with open("data/read.txt", "r") as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    main()