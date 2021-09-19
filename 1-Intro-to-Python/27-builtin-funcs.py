# https://www.teclado.com/30-days-of-python/python-30-day-16-lambda-expressions


def get_grade_average(student):
    return student["grade_average"]


students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92},
]

valedictorian = max(students, key=get_grade_average)
print(valedictorian)

valedictorian = max(students, key=lambda student: student["grade_average"])

print(valedictorian)


def divide(a, b):
    if b == 0:
        return "You can't divide by 0!"
    else:
        return a / b


operations = {
    "a": lambda a, b: a + b,
    "s": lambda a, b: a - b,
    "m": lambda a, b: a * b,
    "d": divide,
}


def main():
    selected_option = input(
        """Please select one of the following options:

    a: add
    s: subtract
    m: multiply
    d: divide

    What would you like to do? """
    )

    operation = operations.get(selected_option)

    if operation:
        a = int(input("Please enter a value for a: "))
        b = int(input("Please enter a value for b: "))

        print(operation(a, b))
    else:
        print("Invalid selection")


if __name__ == "__main__":
    main()
