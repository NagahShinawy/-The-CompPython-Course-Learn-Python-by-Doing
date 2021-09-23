# https://www.teclado.com/30-days-of-python/python-30-day-24-exceptions-advanced


def to_int(value):

    try:
        return int(value)
    except (ValueError, TypeError):
        return False
    finally:  # runs everytime
        print("End ...")


print(to_int("36"))
print(to_int("36.5"))
print(to_int("test"))

if to_int("-1") is not False:
    print("Int")
