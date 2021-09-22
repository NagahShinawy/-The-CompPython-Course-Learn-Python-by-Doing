# todo#1 NameError: name 'name' is not defined

# print(name)

name = "Smith"

print(name)


# todo#2 TypeError: list indices must be integers or slices, not str
countries = ["Egypt", "German", "US", "KSA", "Morocco"]

# print(countries[""])  # TypeError: list indices must be integers or slices, not str

print(countries[:3])  # ['Egypt', 'German', 'US']
