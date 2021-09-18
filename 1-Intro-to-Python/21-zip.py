# https://blog.teclado.com/python-zip/

from itertools import zip_longest


names = ["loen", "daniel", "stephen", "james", "john", "adam", "test", "Test2", "Test3"]

salaries = [5, 7, 3, 2, 10, 4]

# like list of tuples [ ('loen', 5), (), (), ...]
# zip : combine one list or more to one list
names_by_salaries = zip(names, salaries)  # take short length
names_by_salaries2 = zip(names, salaries)  # take short length

for name, salary in names_by_salaries:
    print(f"{name} ===> {salary}")


print(
    dict(names_by_salaries2)
)  # {'loen': 5, 'daniel': 7, 'stephen': 3, 'james': 2, 'john': 10, 'adam': 4}


print("#" * 100)

items = ["iphone", "macbook", "watch", "touchpad"]
prices = [3, 10, 5]

# fillvalue: missed values
item_price = list(zip_longest(items, prices, fillvalue="-"))


print(item_price)
