class Student:
    # by convention variables with prefix "_" are private
    # "__" prefix is enforced by python
    def __init__(self, first_name, last_name):
        self.__first_name = first_name  # assign input values
        self.__last_name = last_name
        self.__term = 1  # initial value not passed during initialization

    def get_full_name(self):
        return self.__first_name + " " + self.__last_name

    def increase_term(self):
        if self.__term >= 9:
            return  # no student shall have more than 9 terms
        self.__term += 1

    def get_term(self):
        return str(self.__term)

    # conversion to a string
    def __str__(self):
        return self.get_full_name() + " (" + self.get_term() + ". Term)"

    # called when asked to represent itself
    def __repr__(self):
        return self.__str__()


class WorkingStudent(
    Student
):  # inherit from Student class (inherits all methods of base class (if not overwritten))
    def __init__(self, first_name, last_name, company):
        super().__init__(first_name, last_name)  # call init function of base class
        self.__company = company

    def __str__(self):
        return (
            self.get_full_name()
            + " ("
            + self.get_term()
            + ". Term, "
            + self.__company
            + ")"
        )


def main():
    erik = Student("Erik", "Mustermann")
    erik.increase_term()
    erik.__term = "jkahs"  # does not modify private variable, but much rather "mangles it" -- https://www.geeksforgeeks.org/python/private-variables-python/
    print(erik)
    erik  # asked to represent itself
    max = WorkingStudent("Max", "Müller", "DB AG")
    print(max)


if __name__ == "__main__":
    main()
