# https://www.youtube.com/watch?v=W7QByFjVom8


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

sample_csv_value = ",".join(["Adam", "adam@test.com", 23])

print(sample_csv_value)
