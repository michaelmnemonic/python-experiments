# list slicing
students = ["Max", "Monika", "Erik", "Franziska"]
# removes last element and assigns it to a variable
last_student = students.pop()

# Lists can be concatinated with "+"
students = students + ["Bob"]

# delete specific entries with its index
del students[3]

# delete specific entries using its value
students.remove("Monika")
students.append("Monika")

students = ["Max", "Monika", "Erik", "Franziska"]

# negative index reference end of list
students[-1]
students[-2]

# slice list using []
print(students[2:4])
print(students[2:])
print(students[:-1])

# list comprehension
xs = list(range(1, 10))  # generate list [1, 2, ..., 9]
ys = [x * x for x in xs]  # square each entry in xs and assign it to a new list ys
# alternative example
length_of_name = [len(name) for name in students]

print(students)
