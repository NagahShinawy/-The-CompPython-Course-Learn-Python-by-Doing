numbers = [7, 6, 3, 12, 80, 30, 24, 20, 11, 12, 15]
evens = [num for num in numbers if num % 2 == 0]

print(numbers)
print(evens)

allowed = ["john", "james", "danial"]
guest = ["Loen", "Smith", "Sara", "Adam", "james", "anna", "angel", "john"]

intersections = [name for name in guest if name in allowed]

print(intersections)

names = ["Matthew", "John", "Helen", "Stephen", "Alexandra", "Rolf"]
short_names = [name for name in names if len(name) < 6]

print(short_names)


names = ["Matthew", "John", "Helen", "Stephen", "Alexandra", "Rolf"]
short_names = [len(name) < 6 for name in names]
print(short_names)

names = ["Matthew", "John", "Helen", "Stephen", "Alexandra", "Rolf"]
short_final_n = [name for name in names if len(name) < 6 if name[-1] == "n"]
print(short_final_n)
