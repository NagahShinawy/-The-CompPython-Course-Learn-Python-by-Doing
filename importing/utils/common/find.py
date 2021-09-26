def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i

    raise NotFoundError(f"Not found {expected}")


class NotFoundError(Exception):
    pass
