# while
print("control structure ''while''")
counter = 0
while counter < 10:
    print(counter)
    counter += 1

# for
print("control structure ''for''")
for counter in range(0, 10):
    print(counter)

list = [5, 8, 10]
print("control structure ''for'' using a list")
for element in list:
    print(element)

# break, continue
print("control structure ''continue'' and ''break''")
for iterator in range(0,10):
    # this skips this iteration if true
    if iterator == 3:
        continue
    # this cancels the iteration
    if iterator == 9:
        break
    print(iterator)