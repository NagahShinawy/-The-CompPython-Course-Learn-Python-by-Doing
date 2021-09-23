
def count_from_zero_to_n(n):
    print(type(n))
    if not isinstance(n, int):
        raise TypeError(f"Must be int not {n.__class__.__name__}")

    if n < 0:
        raise ValueError("Input should be a non-negative integer")

    for i in range(n + 1):
        yield i


count = count_from_zero_to_n("test")

for number in count:
    print(number)
