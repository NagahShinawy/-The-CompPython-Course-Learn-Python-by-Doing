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

    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


def main():
    james = Student("James", "MIT")
    adam = WorkingStudent("Adam", "MIT", 1000)
    print(james)
    print(adam)


if __name__ == '__main__':
    main()

