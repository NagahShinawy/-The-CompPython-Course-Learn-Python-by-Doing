"""
# ########## ########## ########## ########## ########## ########## #########
RELATIVE IMPORT : NEEDS TO KNOW THE PARENT PACKAGE


if you run 'os_operations' as script so
1- __name__  = "__main__"
2- __package__ = ''

so if you running  ==> 'from . import dtime'
it gives 'ImportError: attempted relative import with no known parent package'

because there is no parent package it is empty ''
SOLVED BY : JUST ==> [import dtime ] NOT USE RELATIVE IMPORT

# ####### ####### ####### ####### ######

if you are running file as module from another file

from .dtime import now
from . import dtime
# ####### ####### ####### ####### ######



# ########## ########## ########## ########## ########## ########## #########
if you run 'os_operations' as script a module from another file [main.py] so,

1- __name__  = 'utils.os_operations'
2- __package__ = 'utils'

so if you running  ==> 'from . import dtime'
NOW : PARENT PACKAGE IS KNOWN, SO CAN USE RELATIVE REIMPORT

# ####### ####### ####### ####### ######

if you are running file as script

from common.find import *
import dtime
from dtime import *

# ####### ####### ####### ####### ######

"""
# ########## ########## ########## ########## ########## ########## #########


from .dtime import now
from . import dtime


def createdir(path, dirname):
    print(f"You are creating {path}/{dirname} at {now()}")


def deletedir(dirname):
    print(f"You are Deleting {dirname} at {dtime.now()}")
