# https://blog.teclado.com/logical-comparisons-in-python-and-or/


print(bool(35))  # True
print(bool(""))  # False

print(bool([]))  # False
print(bool([""]))  # True

print(35 and 10)  # 10 returns second value
print(35 and 0)  # 0 means False


name = ""

surname = "James"

welcome = name or f"{surname}"

print(welcome)


created = True

updated = not created


print(created)
print(updated)


print(None and 35)  # None
print(None or 35)  # 35

print(10 and 0)  # 0 ==> second value.


print(20 and [])  # [] second value because we are using and
print(20 or [])  # 20 first value because we are using or
