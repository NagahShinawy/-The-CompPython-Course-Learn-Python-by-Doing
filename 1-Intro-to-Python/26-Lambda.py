# quick function, small processing, anonymous function
def with_bonus(salary):
    return salary + 1000


def calc_degrees_avrg(student):
    grades = student["grades"]
    return sum(grades) / len(grades)


salaries = [6, 8, 2, 1, 9, 12, 4, 7]  # 6$, 8$, ..

print(salaries)

salaries = list(map(lambda salary: f"{salary}$", salaries))

print(salaries)

salaries = [5000, 4000, 1000, 3000, 10000]

salaries_with_bonus = map(with_bonus, salaries)

print(salaries)
print(list(salaries_with_bonus))


divide = lambda x, y: x / y

print(divide(10, 4))
print(divide(10, 2))

add = (lambda number1, number2: number1 + number2)(4, 9)

print(add)


students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

students_grades = [
    {student["name"]: calc_degrees_avrg(student)} for student in students
]

print(students_grades)

students_grades = map(
    lambda student: sum(student["grades"]) / len(student["grades"]), students
)


print(list(students_grades))