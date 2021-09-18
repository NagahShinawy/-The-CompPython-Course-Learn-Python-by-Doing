# Set comprehensions

names = [
    "john",
    "loen",
    "smith",
    "bob",
    "anna",
    "james",
    "adam",
    "james",
    "john",
    "sara",
    "adam",
]

unique_names = {name for name in names}

print(names)
print(unique_names)

names = {name: len(name) for name in names}

print(names)
print("#" * 100)
users = [
    {"username": "john", "email": "john@test.com", "is_active": True, "gender": "male"},
    {"username": "james", "email": "james@test.com", "is_active": False, "gender": "female"},
    {"username": "sara", "email": "sara@test.com", "is_active": True, "gender": "female"},
    {"username": "loen", "email": "loen@test.com", "is_active": False, "gender": "female"},
]

active_users = [user for user in users if user["is_active"]]
users = [{key: value for key, value in user.items() if key in ["username", "gender"]} for user in active_users]

print(active_users)

print("#" * 100)
print(users)
