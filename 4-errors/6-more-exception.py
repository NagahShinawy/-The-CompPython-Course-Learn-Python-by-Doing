# https://www.teclado.com/30-days-of-python/python-30-day-24-exceptions-advanced
# https://www.teclado.com/30-days-of-python/python-30-day-19-exception-handling


import math

# ##################################################### ######################################################

numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except LookupError:  # LookupError is a IndexError
    print("Could not retrieve that value.")

# ##################################################### ######################################################


numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except IndexError:
    print("The requested index is out of range")  # this line will be executed
except LookupError:
    print("Could not retrieve that value.")

# ##################################################### ######################################################


person = {"name": "Phil", "city": "Budapest"}

try:
    print(person["age"])  # <- Referencing an undefined key
except IndexError:
    print("The requested index is out of range")
except LookupError:
    print("Could not retrieve that value.")  # this line will be executed

# ##################################################### ######################################################

# Accessing the original exception


numbers = [1, 2, 3, 4, 5]

try:
    print(numbers[100])  # <- Out of range index
except LookupError as ex:
    print(f"Error: {ex}")


def intify(number):
    try:
        return int(number)
    except ValueError:
        try:
            f_number = float(number)
        except ValueError:
            raise ValueError(
                f"could not convert string to an integer: {number}"
            ) from None
        else:
            return round(f_number)


# with open("numbers.txt", "r") as numbers_file:
#     numbers = [int(number) for number in numbers_file]


def average(nums):
    try:
        mean = math.fsum(nums) / len(nums)
    except ZeroDivisionError:
        print(0)
    except TypeError:
        print("You provided invalid values!")
    else:
        print(mean)  # runs only in the case of success
    finally:
        print("Runs Everytime, in both cases, success and fail")


average([7, 3, 1])
