"""
the same what done at os_operations
# ImportError: attempted relative import with no known parent package ==> is you run find.py as script
# it works if you run find.py as module from 'main.py'
"""

from ..dtime import *


def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i

    raise NotFoundError(f"Not found {expected}")


class NotFoundError(Exception):
    pass
