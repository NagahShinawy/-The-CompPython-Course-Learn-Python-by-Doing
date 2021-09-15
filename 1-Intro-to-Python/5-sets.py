grades = [45, 23, 45, 90, 100, 50, 40, 90]

order = ["checking", "meal", "meal", "checking", "burger"]

print(order)

unique = set(order)

print(unique)

salaries = [("hr", 4000), ("it", 2000), ("accounting", 2000), ("finance", 2000)]

salaries = [salary[-1] for salary in salaries]

print(salaries)

print(set(salaries))

unique_salaries = set(salaries)

print(unique_salaries)

# set operations

unique_salaries.add(3000)
unique_salaries.add(3000)
unique_salaries.add(3000)


unique_salaries.remove(3000)
# unique_salaries.remove(3001)  # KeyError: 3001: must be member

print(unique_salaries)




print(unique_salaries)

