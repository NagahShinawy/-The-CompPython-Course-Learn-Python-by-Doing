
class Director:

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return f"{self.name}-{self.dob}"


class Movie:

    def __init__(self, title: str, director: Director, year: int):
        self.title = title
        self.director = director
        self.year = year

    def __repr__(self):
        return f"{self.title}({self.year})"


def main():
    john = Director("John", "01-01-1970")
    loen_the_pro = Movie("Loen The Pro", john, 1994)



if __name__ == '__main__':
    main()