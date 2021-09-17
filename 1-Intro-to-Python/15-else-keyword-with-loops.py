ten = range(1, 11)


for num in ten:
    print(num)
else:
    print("End ...")


users = ["admin", "admin", "user", "admin"]

for user in users:
    if user == "USER":
        break

else:
    # comes here when condition if False
    # means comes here when loop completed with no break
    print("NOT All Admins. Found normal user")