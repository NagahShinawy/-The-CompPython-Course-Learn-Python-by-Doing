themes = ["Black", "White", "Green", "Gray"]

for theme in themes:
    print(theme)


for even in range(0, 11, 2):
    print(even, end=" ")

print()
print("#" * 100)


booking_history = [
    {"from": "Cairo", "to": "Alex", "date": "2021-01-01", "price": "10$"},
    {"from": "Cairo", "to": "Gadda", "date": "2021-01-02", "price": "500$"},
    {"from": "Cairo", "to": "Dubai", "date": "2021-01-03", "price": "600$"},
]

print("From\tTo")
for booking in booking_history:
    print(f"{booking['from']}\t{booking['to']}")


for i in range(10, 0, -1):
    print(i)
