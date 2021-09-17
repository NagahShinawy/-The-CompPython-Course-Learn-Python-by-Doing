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
