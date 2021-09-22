class ClassMixin:
    @classmethod
    def cls(cls):
        # action of @classmethod depends on cls or class attr
        return cls.__name__

    @staticmethod
    def pwd():
        # it is method belong to class but not depends on self[instance attrs] either cls [class attrs]
        # it is related somehow to the class
        return __file__


class Article(ClassMixin):
    def __init__(self, title, author, desc=""):
        self.title = title
        self.author = author
        self.desc = desc

    def __repr__(self):
        return f"{self.title} By {self.author}"


django = Article("ORM in Django", "John")

print(django.cls())  # calling classmethod with obj
print(Article.cls())  # calling classmethod with class

print("#" * 50)
print(django.pwd())  # calling staticmethod with obj
print(Article.pwd())  # calling staticmethod with class
