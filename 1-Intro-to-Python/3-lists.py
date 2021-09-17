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

# insert item at index


emails = [
    "test@outlook.com",  # 0
    "james@outlook.com",  # 1
    "sara@outlook.com",  # 2
    "john@outlook.com",  # 3
]

print(emails)

emails.insert(2, "adam@outlook.com")

print(emails)

# pop: remove item by index and return removed item

sara = emails.pop(2)

print(sara)

print(emails)

item = emails.pop()  # default index is -1, so "john@outlook.com" was deleted

print(item)

print(emails)

# print(emails.pop(12))  # IndexError: pop index out of range
# print(emails.pop(-12))  # IndexError: pop index out of range


# clear

evens = [4, 10, 2, 22, 24, 26]

print(evens)

evens.clear()

print(evens)

evens = [4, 10, 2, 22, 24, 26]
print(evens)
evens = []

print(evens)
