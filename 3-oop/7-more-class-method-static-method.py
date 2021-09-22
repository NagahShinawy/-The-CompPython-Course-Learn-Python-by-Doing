class WorkingHours:

    WEEKLY_HOURS = 37.5
    CURRENCY = "USD"

    @classmethod
    def calc_salary(cls, hour_rate):
        # class of the obj will passed as first argument 'cls'
        return f"{hour_rate * cls.WEEKLY_HOURS} {cls.CURRENCY}"

    @property
    def cls(self):
        return self.__class__.__name__


class EngineerWorkingHours(WorkingHours):
    WEEKLY_HOURS = 40
    CURRENCY = "EUR"


class FixedFloat:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value:.2f})"

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


class Euro(FixedFloat):

    SYMBOL = "€"


engs = EngineerWorkingHours.calc_salary(10)
wh = WorkingHours.calc_salary(2)
print(engs)

print(wh)

print(WorkingHours.cls)  # <property object at 0x0000020012137B30>


engs_workh = EngineerWorkingHours()
print(engs_workh.cls)  # EngineerWorkingHours

print("#" * 50)

salary = FixedFloat(10.54534)

print(salary)
print(salary.from_sum(3, 6.5657))  # ==> cls of 'from_sum' is 'FixedFloat'

profit = Euro(70.9595)

print(profit)  # Euro(70.96)
print(profit.from_sum(10, 30.555))  # Euro(40.55)  ==> cls of 'from_sum' is 'Euro'
