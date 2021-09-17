shape = 9, 3  # short


print(shape)  # (9, 3)


shape = (5, 6)

print(shape)  # more clear

purchases = [("iphone", "12k"), ("laptop", "15k"), ("watch", "10k")]

#
# for item, price in purchases:  # unpacking
#     print(item, price)


print(dict(purchases))

# ############# #############  CHECK ERROR ############# ############# ############
# purchases = [("iphone", "12k", "x", "y"), ("laptop", "15k"), ("watch", "10k")]
# print(dict(purchases))  # ValueError: dictionary update sequence element #0 has length 4; 2 is required

# ############# #############  ############# ############# ############ ############

items = [item[0] for item in purchases]
prices = [item[-1] for item in purchases]

print(items)

print(prices)


prch = zip(items, prices)

print(prch)  # <zip object at 0x000001E1A8DD2108>

for p in prch:  # p ==> ('iphone', '12k')
    print(p)


credentials = "test"

print(credentials, type(credentials))  # test TYPE ==>  str

credentials = ("test",)
print(credentials, type(credentials))  # test TYPE ==>  tuple


# credentials.append("pass@123")  # AttributeError: 'tuple' object has no attribute 'append'

# append to tuple

# credentials += "pass@123"  # TypeError: can only concatenate tuple (not "str") to tuple

credentials = credentials + ("password",)

print(credentials)

credentials += ("admin",)
