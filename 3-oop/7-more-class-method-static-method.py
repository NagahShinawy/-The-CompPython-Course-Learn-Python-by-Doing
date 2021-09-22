class WorkingHours:

    WEEKLY_HOURS = 37.5
    CURRENCY = "USD"

    @classmethod
    def calc_salary(cls, hour_rate):
        return f"{hour_rate * cls.WEEKLY_HOURS} {cls.CURRENCY}"

    @property
    def cls(self):
        return self.__class__.__name__


class EngineerWorkingHours(WorkingHours):
    WEEKLY_HOURS = 40
    CURRENCY = "EUR"


engs = EngineerWorkingHours.calc_salary(10)
wh = WorkingHours.calc_salary(2)
print(engs)

print(wh)

print(WorkingHours.cls)  # <property object at 0x0000020012137B30>


engs_workh = EngineerWorkingHours()
print(engs_workh.cls)  # EngineerWorkingHours
