friends = {input(f"Enter friend#{i}").lower() for i in range(1, 4)}

print(friends)

with open("people.txt", "r") as f:
    people = {person.lower().strip() for person in f.readlines()}


print(people)

nearby = friends.intersection(people)

print(nearby)

if nearby:
    nearby = [name.title() for name in nearby]
    print(f"Your Near By Friends are:", ",".join(nearby))
    with open("nearby_friends.txt", "w") as f:
        for name in nearby:
            f.write(name + "\n")

else:
    print("Your are Lonely")
