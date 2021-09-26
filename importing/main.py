# import file_operations
from utils.dtime import today  # absolute import ==> means full path
from utils.os_operations import createdir, deletedir

print(today())
createdir("test", "test")
deletedir("test")