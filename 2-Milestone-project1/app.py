from collections import namedtuple
from prettytable import PrettyTable

MENU_PROMPT = r"""
Enter 'a' to add a movie,
's\l' to show\list your movies,
'f' to find a movie by title, or 'q' to quit: 
"""

movies = []
MOVIE_COLS_NAMES = ["Count", "Title", "Director", "Year"]
Movie = namedtuple("Movie", ["title", "director", "year"])
movies_table = PrettyTable()
movies_table.field_names = MOVIE_COLS_NAMES


def make_movie(movie: dict):
    obj = Movie(*movie.values())
    return obj


def repr_movie(movie: Movie):
    return f"{movie.title}({movie.year})"


def add_movie(count: int):
    # You may want to create a function for this code
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({"title": title, "director": director, "year": year})
    movies_table.add_row([count, title, director, year])


def list_movies():
    for counter, movie in enumerate(movies, start=1):
        mv = make_movie(movie)
        print(f"{counter}-Movie: {repr_movie(mv)}")


def show_movies():
    print(movies_table)


def show_movie(movie: Movie):
    movie_table = PrettyTable()
    movie_table.field_names = MOVIE_COLS_NAMES[1:]
    movie_table.add_row([movie.title, movie.director, movie.year])
    return movie_table


def find_movie(title: str):
    for movie in movies:
        if movie["title"].lower() == title.lower():
            return make_movie(movie)
    return None


def menu():
    # And another function here for the user menu
    selection = input(MENU_PROMPT)
    count = 1
    while selection != "q":
        if selection == "a":
            add_movie(count)
            count += 1
        elif selection == "l":
            list_movies()
        elif selection == "f":
            title = input("Movie title: ")
            movie = find_movie(title=title)
            # print(f"You Search for {repr_movie(movie)}")
            print(show_movie(movie))
        elif selection == "s":
            show_movies()

        else:
            print("Unknown command. Please try again.")

        selection = input(MENU_PROMPT)


if __name__ == "__main__":
    menu()
