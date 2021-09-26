# import file_operations

# ########### ########### ########### ########### ########### ########### ##########

# from file_operations import save_to_file, read_file ===> just import that you will use only
# no need to import entire library to just use one/two functions

# ########### ########### ########### ########### ########### ########### ##########

# from file_operations import save_to_file
# from operations import save_to_file

# it will take the last one you write 'from operations import save_to_file'

# SOLVED: from file_operations import save_to_file as file_ops_savefile
# from operations import save_to_file as ops_savefile

# BUT NOT RECOMMENDED TO DO THAT

# USE :
# import file_operations
# import operations

# ########### ########### ########### ########### ########### ########### ##########

import file_operations as ops  # run 'file_operations' as module mode

# from utils.dtime import today  # it works
import utils.dtime as dt


def main():
    ops.save_to_file("Jose", "names.txt")
    print(ops.read_lines("names.txt"))  # ['Jose']
    print(ops.read_file("names.txt"))  # ['Jose']

    print(f"Today is {dt.today()}")
    print(f"Yesterday is {dt.yesterday()}")
    print(f"Tomorrow is {dt.tomorrow()}")


if __name__ == "__main__":
    main()  # run app.py as script mode
