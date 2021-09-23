class BaseError(Exception):
    text = ""
    description = None
    code = None

    @classmethod
    def raise_error(cls, *args):
        raise cls(cls.text.format(*args))


class CarAlreadyExist(BaseError):
    text = "Car <{}>  already exist"
    description = None
    code = None


class NotCarObj(BaseError):
    text = "Value of <{}> is not <{}> obj. it is <{}>."
    description = None
    code = None


class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__}({self.model}, {self.price})"


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if car in self.cars:
            error = CarAlreadyExist()
            error.raise_error(car)
        if not isinstance(car, Car):
            error = NotCarObj()
            error.raise_error(car, Car.__name__, car.__class__.__name__)
        self.cars.append(car)

    def remove_car(self, car):
        raise NotImplementedError("Can not remove cars!. Not implemented Yet")


if __name__ == "__main__":
    garage = Garage()
    bwm = Car("BMW", "120K")
    nissan = Car("Nissan", "100K")
    garage.add_car(bwm)
    garage.add_car(nissan)
    # garage.add_car(nissan)  # __main__.CarAlreadyExist: Car <Car(Nissan, 100K)>  already exist
    # garage.remove_car(nissan)  # NotImplementedError: Can not remove cars!. Not implemented Yet
    # garage.add_car("kia")  # __main__.NotCarObj: Value of <kia> is not <Car> obj. it is <str>
