# https://blog.teclado.com/python-list-comprehensions/


# https://www.teclado.com/30-days-of-python/python-30-day-15-comprehensions


numbers = [6, 7, 3, 10, 20]

doubles = [number * 2 for number in numbers]

print(doubles)


def get_name(email: str):
    return email.split("@")[0]


emails = ["john@test.com", "james@test.com", "loen@test.com", "adam@test.com"]

names = [get_name(email).title() for email in emails]

print(names)


names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people = [(name.title(), age) for name, age in zip(names, ages)]

print(people)

# Set comprehensions

names = [
    "john",
    "loen",
    "smith",
    "bob",
    "anna",
    "james",
    "adam",
    "james",
    "john",
    "sara",
    "adam",
]

unique_names = {name.title() for name in names}

print(len(names))  # 11
print(len(unique_names))  # 8

names = {name: len(name) for name in names}

print(names)
