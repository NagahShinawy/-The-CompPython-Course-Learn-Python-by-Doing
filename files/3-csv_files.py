from prettytable import PrettyTable


STD_COLS = ["Name", "Email", "Age"]
std_table = PrettyTable()
std_table.field_names = STD_COLS

with open("students.txt", "r") as f:
    students = [line.strip().split(",") for line in f.readlines()[1:]]

std_table.add_rows(students)

print(std_table)


# using unpacking
print("#" * 100)

for student in students:
    name, email, age = student
    print(*student)
    print(name, email, age)