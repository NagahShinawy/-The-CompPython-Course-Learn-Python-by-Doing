# https://blog.teclado.com/python-enumerate/

names = ["loen", "daniel", "stephen", "james", "john", "adam"]

names = list(
    enumerate(names, start=1)
)  # list of tuples [(1, 'loen'), (2, 'daniel'), ...]

print(names)

print("#" * 100)
# do the same of enumerate without using enumerate
items = ["iphone", "macbook", "watch", "touchpad"]

items1 = zip(range(1, len(items) + 1), items)
items2 = zip(range(1, len(items) + 1), items)
print(list(items1))  # list of tuples
print(dict(items2))  # list of dict
