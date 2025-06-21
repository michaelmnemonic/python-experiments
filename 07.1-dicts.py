# create a dictionary
airport = {}
print(airport)  # empty
airport = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}
print(airport)  # not empty
print(airport["Helsinki"])  # look up entry using key
airport["Budapest"] = "BUD"
print(airport)  # new entry added
del airport["Saigon"]
print(airport)  # entry deleted

if "Berlin" in airport:
    print("Berlin is contained in the dictionary")

print(airport.get("Saigon"))  # None
