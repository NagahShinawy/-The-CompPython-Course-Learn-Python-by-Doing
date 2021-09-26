# use dict insteadof if else


def welcome():
    print("Hi everyone")


welcome()  # run function
print(welcome)  # <function welcome at 0x000001EBFBABD430>
print(welcome.__class__)  # <class 'function'>
print(welcome.__name__)  # welcome
print(welcome.__class__.__name__)  # function

greeting = welcome

greeting()

avg = lambda items: sum(items) / len(items)
total = lambda items: sum(items)
top = lambda items: max(items)

prices = [6, 4, 1, 20, 8]

print(avg(prices))
print(total(prices))
print(top(prices))

stds = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in stds:
    name = student["name"]
    grades = student["grades"]
    option = input("Enter a for avrg, t for total, o for top")
    print(f"Student is {name}")
    if option == "a":
        print(avg(grades))
    elif option == "t":
        print(total(grades))
    elif option == "o":
        print(top(grades))
    else:
        print("Invalid Option")
    print("#" * 100)


options = {
    "a": lambda items: sum(items) / len(items),
    "t": sum,
    "o": max,
}

for student in stds:
    name = student["name"]
    grades = student["grades"]
    choice = input("Enter a for avrg, t for total, o for top")
    print(f"Student is {name}")
    action = options.get(choice)
    if action:
        print(action(grades))
    else:
        print("Invalid Choice")
