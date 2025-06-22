class Student:
    # by convention variables with prefix "_" are private
    # "__" prefix is enforced by python
    def __init__(self, first_name, last_name):
        self.__firstname = first_name  # assign input values
        self.__last_name = last_name
        self.__term = 1  # initial value not passed during initialization

    def get_full_name(self):
        self.__first_name + " " + self.__last_name

    def increase_term(self):
        if self.__term >= 9:
            return  # no student shall have more than 9 terms
        self.__term += 1

    def get_term(self):
        return self.__term


def main():
    erik = Student("Erik", "Mustermann")
    erik.increase_term()
    erik.__term = "jkahs"  # does not modify private variable, but much rather "mangles it" -- https://www.geeksforgeeks.org/python/private-variables-python/
    print(str(erik.get_term))
    print()


if __name__ == "__main__":
    main()
