# https://blog.teclado.com/creating-a-new-sequence-type-in-python-part-3/
# https://blog.teclado.com/creating-a-new-sequence-type-in-python-part-1/
# https://blog.teclado.com/creating-a-new-sequence-type-in-python-part-2/

movies = ["Matrix", "Loen", "Trueman show", "inception"]

print(movies.__class__)  # <class 'list'>

print("test".__class__)  # <class 'str'>

# __repre__ vs __str__

# __repr__: for debugging. code oriented description
# __str__: for printing/ show for user. user oriented description


# if you want to implement one, use __repre__


class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.__class__.__name__}({self.model}, {self.price})"

    def __repr__(self):
        return "Car"

    def to_json(self):
        return {"model": self.model, "price": self.price}


class Garage:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    def add_car(self, car: Car):
        if car not in self.cars:
            self.cars.append(car)

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)

    def show_cars(self):
        for car in self.cars:
            yield car


def main():
    ford = Car("Ford", "45K$")
    bwm = Car("BMW", "100K$")
    nissan = Car("Nissan", "70K$")
    kia = Car("KIA", "60K$")
    b1 = Garage("Building-23-43")

    cars = [ford, bwm, nissan, kia]
    for car in cars:
        b1.add_car(car)

    cars = b1.show_cars()
    for counter, car in enumerate(cars, start=1):
        print(f"{counter}-{car}")

    print("#" * 50)
    print(len(b1))

    print("#" * 50)

    for car in b1:  # can loop because of __getitem__
        print(car)

    print("#" * 50)
    print(
        b1[0]
    )  # can use indexing because of __getitem__   ==> Garage.__getitem__(b1, 0)
    print(
        b1[1]
    )  # can use indexing because of __getitem__  ==> Garage.__getitem__(b1, 1)

    print(nissan)


if __name__ == "__main__":
    main()
