# https://blog.teclado.com/python-list-comprehensions/

numbers = [6, 7, 3, 10, 20]

doubles = [number * 2 for number in numbers]

print(doubles)


def get_name(email: str):
    return email.split("@")[0]


emails = ["john@test.com", "james@test.com", "loen@test.com", "adam@test.com"]

names = [get_name(email).title() for email in emails]

print(names)
