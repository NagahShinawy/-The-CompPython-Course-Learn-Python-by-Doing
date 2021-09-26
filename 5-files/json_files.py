import json

with open("users.json", "r") as f:
    users = json.load(f)  # load means: get data from source [json file 'users.json']


print(type(users))  # list

for user in users:
    print(*user.values())


books = [
    {"title": "clea code", "price": "12$", "author": "bob"},
    {"title": "python for all", "price": "10$", "author": "john"},
    {"title": "flask for web services", "price": "15$", "author": "loen"},
]


with open("books.json", "w") as f:
    json.dump(
        books, f
    )  # dump means: means save data for source [json file 'books.json'].
    # file 'books.json' will be created with 'books' list data


tools = [
    {"name": "pycharm", "is_opensource": True, "developed_by": "jetbrains"},
    {"name": "postman", "is_opensource": False, "developed_by": "test"},
    {"name": "vscode", "is_opensource": True, "developed_by": "microsoft"},
]


to_str = json.dumps(tools)  # from list [like json obj] to str

print(to_str)
print(type(to_str))  # <class 'str'>

apps = '[{"name": "fb", "owner": "mark", "users": "1B"}, {"name": "whatsapp", "owner": "mark", "users": "2B"}]'

to_json = json.loads(apps)  # from to str list [like json obj]


print(to_json)

print(type(to_json))  # <class 'list'>
