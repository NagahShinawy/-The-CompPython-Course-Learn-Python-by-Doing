class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def __repr__(self):
        if hasattr(self, "salary"):
            return f"{self.name}-{self.salary}"
        return self.name

    @property
    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):

    WEEKLY_WORKING_HOURS = 37.5
    DOLLAR = "$"

    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property  # we are using @property because we are not perform actions, we just calc a value
    def weekly_salary(self):
        return f"{self.salary * self.WEEKLY_WORKING_HOURS}{self.DOLLAR}"


def main():
    james = Student("James", "MIT")
    adam = WorkingStudent("Adam", "Oxford", 50)
    print(james)
    print(adam)
    print(adam.weekly_salary)


if __name__ == "__main__":
    main()
