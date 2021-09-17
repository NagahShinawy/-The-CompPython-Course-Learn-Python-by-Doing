def is_prime_number(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime


def is_prime_number2(num):
    for i in range(2, num):
        if num % i == 0:
            break

    else:
        # comes here if loop complete all iterations
        return True


for number in range(10, 21):
    if is_prime_number2(number):
        print(f"Number {number} is Prime")
