# https://www.teclado.com/30-days-of-python/python-30-day-13-return-statements


cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]


def welcome(name: str) -> str:
    print(locals())  # {'name': 'John'}
    return f"Welcome, {name}"


def calc_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg


def main():
    print(welcome("John"))
    print(welcome("James"))
    print(welcome("Adam"))

    car = {
        "make": "Ford",
        "model": "Fiesta",
        "mileage": 23000,
        "fuel_consumed": 460,
    }

    print(calc_mpg(car))
    for car in cars:
        mpg = calc_mpg(car)
        print(f"{mpg:,.3f}")

    print(globals())
    print(locals())


if __name__ == "__main__":
    main()
    # print(locals())
