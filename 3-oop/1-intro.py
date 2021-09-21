from prettytable import PrettyTable

john = {
    "name": "john",
    "email": "john@test.com",
    "subjects": [
        {"title": "Arabic", "grade": 60},
        {"title": "English", "grade": 70},
        {"title": "Math", "grade": 90},
        {"title": "music", "grade": 50},
    ],
}
grades = [subject["grade"] for subject in john["subjects"]]
avrg_grades = sum(grades) / len(grades)

print(avrg_grades)


class Student:

    STUDENT_FIELDS = ["Name", "Email", "Total"]
    __students = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.subjects = []
        self.__students.append(self)

    @property
    def average(self):
        return sum(self.grades) / len(self.grades)

    @property
    def grades(self):
        if self.subjects:
            return [subject["degree"] for subject in self.subjects]
        return None

    @property
    def score(self):
        if self.grades:
            return sum(self.grades)
        return ""

    def show_info(self):
        student = PrettyTable()
        student.field_names = self.STUDENT_FIELDS
        student.add_row([self.name, self.email, self.score])
        return student

    @classmethod
    def show_all(cls):
        students = PrettyTable()
        students.field_names = cls.STUDENT_FIELDS
        students.add_rows(([student.name, student.email, student.score] for student in cls.__students))
        return students

    def add_subject(self, title, degree):
        self.subjects.append({"title": title, "degree": degree})


if __name__ == "__main__":
    james = Student("James", "james@test.edu.eg")
    james.add_subject(title="Math", degree=100)
    james.add_subject(title="English", degree=40)
    print(james.show_info())
    print(james.__class__)  # <class '__main__.Student'>
    print(james.__class__.__name__)  # Student

    # ###### ###### ###### ###### ###### ###### ###### ###### ###### #####
    loen = Student("Loen", "loen@test.edu")
    loen.add_subject("Arabic", degree=20)
    print(Student.show_all())
