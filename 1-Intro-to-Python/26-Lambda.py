
# quick function, small processing, anonymous function
def with_bonus(salary):
    return salary + 1000


salaries = [6, 8, 2, 1, 9, 12, 4, 7]  # 6$, 8$, ..

print(salaries)

salaries = list(map(lambda salary: f"{salary}$", salaries))

print(salaries)

salaries = [5000, 4000, 1000, 3000, 10000]

salaries_with_bonus = map(with_bonus, salaries)

print(salaries)
print(list(salaries_with_bonus))

