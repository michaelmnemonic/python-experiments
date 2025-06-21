airport = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}

print(airport.items())  # returns list of tupel

for key, value in airport.items():
    print(key + ": " + value)
