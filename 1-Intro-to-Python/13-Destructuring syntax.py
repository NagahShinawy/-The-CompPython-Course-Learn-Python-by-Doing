# Destructuring is unpacking means take tuple and convert it to many vars

# https://www.teclado.com/30-days-of-python/python-30-day-9-enumerate-zip


CURRENCY = "$"

currencies = 15, 21

# unpacking is Destructuring means take tuple and convert it to many vars
dollar, eur = currencies


print(f"Dollar: {dollar}")
print(f"Eur: {eur}")

print("#" * 100)


item = {"item": "phone", "price": 12}
name, price = item

print(f"{name} = {item[name]}")
print(f"{price} = {item[price]}")

print("#" * 100)


users = [
    ("john", "john@test.com"),
    ("leon", "loen@test.com"),
    ("smith", "smith@test.com"),
]

for username, email in users:
    print(f"{username} ==> {email}")

print("#" * 100)

for user in users:
    username, email = user
    # username = user[0]
    # email = user[1]
    print(f"{username} ==> {email}")


print("#" * 100)

books = ["clean code", "python.org", "web services with django"]

for counter, book in enumerate(books, start=1):
    print(f"{counter}-{book}")


print("#" * 100)

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, job in people:
    print(f"Name is '{name}' with '{age}' and Job '{job}'")


print("#" * 100)

# Ignoring Values


_, token = ("james", "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9")


print(f"Token: {token}")

for _ in range(10):
    print("Sending email ..")

print("#" * 100)

# Using * to Collect Values

items = ["phone", "laptop", "watch", "mouse", "keyboard"]

mobile, *other = items

print(f"Mobile: {mobile}")
print(f"other: {other}")  # list of others items

head, *tail = [1, 2, 3, 4, 5]

print(head)  # 1
print(tail)  # [2, 3, 4, 5]

print("#" * 100)


themes = ("black", "white", "gray", "green", "blue", "yellow", "red")

*exclude_last, last = themes

print(f"Themes: {themes}")
print(f"All Without Last: {exclude_last}")
print(f"Last: {last}")

print("#" * 100)

black, *middle, red = themes

print(f"Black: {black}")
print(f"Middle: {middle}")
print(f"Red: {red}")

print("#" * 100)

info = ("james", 34, "developer")

name, *other = info

print(name)
if other:
    print(other)

print("#" * 100)

movies = ['Loen The Prof', 'Inception', 'Mask']
years = [1994, 2010, 199]

movie_by_year = zip(movies, years)
movies = list(zip(movies, years))
for movie, year in movie_by_year:
    print(movie, year)


for movie, year in movies:
    print(movie, year)