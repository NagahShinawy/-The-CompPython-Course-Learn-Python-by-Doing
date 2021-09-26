# context manager: open and close files automatically. you have no need to close file manually
file = open("users.json", "r")  # setup: something happens at the start

file.close()  # close file: teardown: something happens at the end


# examples: open db connection at the start and at the end close db connection

# you can use 'with keyword' to apply context manager

with open("data.txt") as f:
    print(f.read())


# here is automatically the file , just you reach to the Indented block the file automatically closed
# print(f.read())  # ValueError: I/O operation on closed file.
