# https://blog.teclado.com/python-updating-dictionaries/

# https://www.teclado.com/30-days-of-python/python-30-day-10-dictionaries


from pprint import pprint


book = {"title": "clean code", "price": "30$", "author": "bob"}


print(book)

# update value

book["title"] = "CLean Code"
book["price"] = "15$"

print(book)

# update using update method

book.update({"author": "BOB"})

print(book)


# remove
author = book.pop("author")
# test = book.pop("test")  # KeyError: 'test'


print(book)
print(author)


books = [
    {"title": "when we meet", "price": "40$", "author": "John"},
    {"title": "django for pro", "price": "50$", "author": "James"},
    {"title": "Python for pro", "price": "70$", "author": "Loen"},
]

print(books)

print(len(books))

books = [
    {
        "title": "when we meet",
        "price": "40$",
        "author": {"name": "John", "email": "john@test.com"},
    },
    {
        "title": "django for pro",
        "price": "50$",
        "author": {"name": "James", "email": "james@test.com"},
    },
    {
        "title": "Python for pro",
        "price": "70$",
        "author": {"name": "Loen", "email": "loen@test.com"},
    },
]


pprint(books)

print("#" * 100)

book1 = books[0]
book2 = books[1]
book3 = books[2]

print(book1)
print(book2)
print(book3)
print("#" * 100)

# ValueError: dictionary update sequence element #0 has length 4; 2 is required
# items = [ ("test", 1, "testing", 2), ("test2", 3, "testing2", 4), ("test3", 5, "testing4", 6), ]
# print(dict(items))

basic_info = {"name": "Adam", "age": 13}

grades = {
    "English": 59,
    "Math": 80,
    "Arabic": 90,
    "science": 95,
}

student_profile = {**basic_info, **grades}
print(student_profile)

vital_signs = {
    "tall": "170cm",
    "weight": "80kg",
}
medical_profile = {"blood_type": "A+", "diseases": "cancer"}

profile = vital_signs | medical_profile

print(profile)