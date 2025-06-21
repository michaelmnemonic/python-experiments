tupel = (1, 2, 3)  # define a tupel
print(tupel)
print(tupel[1])  # inidividual values can be accessed with []

# tupel can not be changed after creation

# entries in a tupel can be assigned in one line to multiple variables
student = ("Max Müller", 22, "Informatik")
name, age, subject = student
print(name)
print(age)
print(subject)


# can be used to return multiple values
def get_student():
    return ("Max Müller", 22, "Informatik")


# can be combined with lists
students = [("Max Müller", 22), ("Monika Musterfrau", 24)]

for name, age in students:
    print("Name: " + name + ", Age: " + str(age))
