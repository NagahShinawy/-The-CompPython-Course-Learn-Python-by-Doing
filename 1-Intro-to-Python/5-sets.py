# https://www.teclado.com/30-days-of-python/python-30-day-11-sets

grades = [45, 23, 45, 90, 100, 50, 40, 90]

order = ["checking", "meal", "meal", "checking", "burger"]

print(order)

unique = set(order)

print(unique)

salaries = [("hr", 17000), ("it", 2000), ("accounting", 2000), ("finance", 2000)]

salaries = [salary[-1] for salary in salaries]

print(salaries)

print(set(salaries))

unique_salaries = set(salaries)

print(unique_salaries)

# set operations

unique_salaries.add(3000)
unique_salaries.add(3000)
unique_salaries.add("3000")
unique_salaries.add(3000.01)

# items in sets must be immutables like string, int, float
# unique_salaries.add([])  # TypeError: unhashable type: 'list'


# remove
unique_salaries.remove(3000)
# unique_salaries.remove(3001)  # KeyError: 3001: must be member

print(unique_salaries)

print(unique_salaries)

# update
unique_salaries.update([3000, 5000, 5000])

print(unique_salaries)

# print(unique_salaries[0])  # TypeError: 'set' object is not subscriptable
x = 17000
random_salary = unique_salaries.pop()
for _ in range(1000000):
    pass
    # assert x == random_salary, f"{random_salary}"
print(random_salary)

# remove intersections

bundle_1 = {"John", "James", "Loen"}
bundle_2 = {"Smith", "Loen", "Adam"}

print(bundle_1.symmetric_difference(bundle_2))
