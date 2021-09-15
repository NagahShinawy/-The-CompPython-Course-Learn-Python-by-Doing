
print(bool(35))   # True
print(bool(""))   # False

print(bool([]))  # False
print(bool([""]))   # True

print(35 and 1)  # 1 means True
print(35 and 0)   # 0 means False


name = ""

surname = "James"

welcome = name or f"{surname}"

print(welcome)

