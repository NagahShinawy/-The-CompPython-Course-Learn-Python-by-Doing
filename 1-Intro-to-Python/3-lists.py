friends = ["John", "James", "Loen", "Adam"]

print(friends)

print(friends[0])
print(friends[1])
print(friends[2])
# print(friends[3])  # IndexError: list index out of range

last = friends[-1]
first = friends[0]
print("===============================")
print(last)
print(first)

print(len(friends))

students = [["John", 23], ["James", 24], ["Adam", 18], ["Sara", 20]]

loen = ["Loen", 34]

students.append(loen)
print(len(students))

print(students)

print(len(students[0]))  # index 0 is ==> ["John", 23]

names = [student[0] for student in students if student]
ages = [student[1] for student in students if len(student) > 1]

print(names)

print(ages)

if loen in students:
    print(f"Removing {loen}")
    students.remove(loen)


print(students)