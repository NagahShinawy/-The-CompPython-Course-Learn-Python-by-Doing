# continue : means skipp
# break : means stop

numbers = [7, 8, 35, 6, 7, 90, 12, 34, 27]


directors = ["james", "john"]
developers = ["leon", "smith", "danial", "sara", "adam"]
emps = developers + directors
# skipp odd
for number in numbers:
    if number % 2 == 0:
        continue

    print(number, end=" ")

print()

print("#" * 100)


def find_number(num):
    return num in numbers


for number in numbers:
    if number == 35:
        break

    print(number)

for emp in emps:
    if emp in directors:
        continue
    print(f"Sending email to {emp}")