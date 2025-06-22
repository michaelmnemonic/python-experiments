class Student:
    def __init__(self, first_name, last_name):
        self.firstname = first_name  # assign input values
        self.last_name = last_name
        self.tems = 1  # initial value not passed during initialization

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def increase_term(self):
        self.term += 1


def main():
    erik = Student("Erik", "Mustermann")
    erik.increase_term()
    print()


if __name__ == "__main__":
    main()
