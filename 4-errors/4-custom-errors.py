"""
adding custom error
"""


class CustomError(TypeError):
    """
    testing custom error
    """


# raise CustomError("This Is Custom Error")  # __main__.CustomError: This Is Custom Error
# raise CustomError(
#     "This Is Custom Error", 500
# )  # __main__.CustomError: ('This Is Custom Error', 500)


class BaseError(Exception):
    """"
    core error class
    """

    message = ""
    code = None

    @classmethod
    def raise_error(cls, *args):
        """
        raise error message based on cls
        :param args: more params for more message details
        :return:
        """
        raise cls(cls.message)


class DBConnectError(BaseError):
    """
    db connection errors
    """

    message = "db connection error, please check your username & password"
    code = 500


error = DBConnectError()

print(error.__doc__)  # db connection errors  [from class doc string]


"""
raise error message based on cls
        :param args: more params for more message details
        :return:
"""
print(error.raise_error.__doc__)

print("#" * 100)

"""
Help on method raise_error in module __main__:

raise_error(*args) method of builtins.type instance
    raise error message based on cls
    :param args: more params for more message details
    :return:

"""
help(error.raise_error)
# __main__.DBConnectError: db connection error, please check your username & password
# error.raise_error()
