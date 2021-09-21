from prettytable import PrettyTable

john = {
    "name": "john",
    "email": "john@test.com",
    "subjects": [
        {"title": "Arabic", "grade": 60},
        {"title": "English", "grade": 70},
        {"title": "Math", "grade": 90},
        {"title": "music", "grade": 50},

    ]
}
grades = [subject["grade"] for subject in john["subjects"]]
avrg_grades = sum(grades) / len(grades)

print(avrg_grades)


class Student:

    STUDENT_FIELDS = ["Name", "Email", "Total"]

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.subjects = []

    @property
    def grades_avrg(self):
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
        student_record = PrettyTable()
        student_record.field_names = self.STUDENT_FIELDS
        student_record.add_row([self.name, self.email, self.score])
        return student_record
    
    def add_subject(self, title, degree):
        self.subjects.append({"title": title, "degree": degree})


if __name__ == '__main__':
    james = Student("James", "james@test.edu.eg")
    james.add_subject(title="Math", degree=100)
    james.add_subject(title="English", degree=40)
    print(james.show_info())
