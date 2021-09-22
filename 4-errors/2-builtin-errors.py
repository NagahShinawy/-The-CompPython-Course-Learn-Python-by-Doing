# todo#1 IndexError

# print("test"[10])  # IndexError: string index out of range
# print([4, 6, 7, 2][10])  # IndexError: list index out of range

# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#2 NameError

# email = "James"
# print(email)


# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#3 KeyError

user = {
    "username": "Loen",
    "email": "loen@test.com",
    "dob": "2000-01-01",
}

# print(user["is_active"])  # KeyError: 'is_active'


# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#4 AttributeError


class Profile:
    def __init__(
        self, username,
    ):
        self.username = username


john = Profile("johnsmith")

# print(john.info)  # AttributeError: 'Profile' object has no attribute 'info'


# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#5 SyntaxError

# SyntaxError: invalid syntax  (missing : )
# if True
#     pass


# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#6 ValueError

# print(int("test"))  # ValueError: invalid literal for int() with base 10: 'test'


# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#7 TypeError

# print("Test" + 12)  # TypeError: can only concatenate str (not "int") to str
