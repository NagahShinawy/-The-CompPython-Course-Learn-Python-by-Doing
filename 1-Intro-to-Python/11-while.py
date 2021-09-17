connection = False
counter = 1
while not connection:
    print(f"Trying to connect ({counter}) ...")
    if counter >= 500:
        break
    counter += 1

users = ["james", "john", "adam", "smith", "loen"]

username = input("Enter username: ")

while username.lower() not in users:
    username = input("Invalid username, Try Again: ")

print("Success!")

