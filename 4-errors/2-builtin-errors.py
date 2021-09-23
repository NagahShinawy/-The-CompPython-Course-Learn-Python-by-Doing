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
# print(int("20.5"))  # ValueError: invalid literal for int() with base 10: 'test'


# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#7 TypeError

# print("Test" + 12)  # TypeError: can only concatenate str (not "int") to str


# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#8 ImportError

# from . import *  # ImportError: attempted relative import with no known parent package

# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#9 NotimplementedError


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return self.username.title()

    def login(self):
        raise NotImplementedError("Login feature is not implemented yet")


james = User("james", "james@123")

print(james)

# james.login() # NotImplementedError: Login feature is not implemented yet


# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo# SyntaxError


def add(x, y):
    pass


# return x + y  # SyntaxError: 'return' outside function


# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#10 TabError


# ######## ######## ######## ######## ######## ######## ######## ######## #######


def power(number: int, exp: int):
    return number ** exp  # 2 ^ 4


print(power(2, 4))  # 2 ^ 4 = 16


# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#11 ModuleNotFoundError

# import testing  # ModuleNotFoundError: No module named 'testing'


# ######## ######## ######## ######## ######## ######## ######## ######## #######

# todo#12 DeprecationWarning
# means : it is no longer the best way (the accepted way) to doing something
