# https://blog.teclado.com/python-slices/

# https://blog.teclado.com/python-slices-part-2/

# https://blog.teclado.com/python-quick-sequence-reversal/

colors = ["white", "black", "red", "green", "blue", "yellow", "gray"]

print(len(colors))


index = 0
for color in colors:
    if index == 3:
        break
    print(color)
    index += 1

# print(colors[STATING_POINT:ENDING_POINT])

print(colors)
print(colors[:3])
print(colors[0:3])
print(colors[-1])
print(colors[:-1])  # ['white', 'black', 'red', 'green', 'blue', 'yellow']
print(colors[::2])  # ['white', 'red', 'blue', 'gray']


print(colors[-3:])  # ['blue', 'yellow', 'gray']

colors2 = colors[::]

print(colors2 == colors)  # 2 lists contain the same values
print(colors2 is colors)  # but actually there are diff lists

#           0                   1                   2               3               4
emails = [
    "john@test.com",
    "james@test.com",
    "adam@test.com",
    "sara@test.com",
    "bob@test.com",
]

slc = slice(2, -1)

print(emails[slc])


"""
But the example above will give us back an empty tuple.
This is because it's impossible to get from index 1 to index 4 in steps of -1.
What would should have written is t[4:1:-1], starting at a higher index than where we finish,
which would print (5, 4, 3).
"""
print(
    emails[0:5:-1]
)  # [] starting point is 0 and you tell it to step back -1. so, it has no values
print(emails[4:1:-1])


players = ["Messi", "Ronaldo", "Zidane", "Kaka", "Ronaldinho"]

zidane = players[2:3]

print(zidane)

# it will replace 'Zidane' with 'ZIN DIN ZIDANE' at the list
players[2:3] = ["ZIN DIN ZIDANE"]

print(players)  # ['Messi', 'Ronaldo', 'ZIN DIN ZIDANE', 'Kaka', 'Ronaldinho']


print("#" * 100)

numbers = [1, 3, 3]
# numbers[1:2] = (2,)  # Don't forget the comma!
numbers[1:2] = {2}

print(numbers)

print("#" * 100)

# Zero Length Slices


numbers = [10, 50]
numbers[1:1] = [21, 33, 49]

print(numbers)  # [10, 21, 33, 49, 50]
