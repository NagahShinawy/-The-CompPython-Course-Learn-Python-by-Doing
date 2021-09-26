file = open("data.txt", "r+")   # open file in read write mode
names = file.read()

print(names)

print(type(names))

file.seek(0)

print("#" * 100)
names = file.readlines()


print(names)  # ['john\n', 'james\n', 'loen\n', 'adam\n']

names = [name.strip() for name in names]

print(names)  # ['john', 'james', 'loen', 'adam']


name = input("Please Type Name : ")
file.write(f"{name}\n")

file.close()

