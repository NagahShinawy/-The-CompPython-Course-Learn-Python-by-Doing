from collections import namedtuple

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

Movie = namedtuple("Movie", ["title", "director", "year"])


def make_movie(movie: dict):
    obj = Movie(*movie.values())
    return obj


def repr_movie(movie: Movie):
    return f"{movie.title}({movie.year})"


def add_movie():
    # You may want to create a function for this code
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({"title": title, "director": director, "year": year})


def list_movies():
    for counter, movie in enumerate(movies, start=1):
        mv = make_movie(movie)
        print(f"{counter}-Movie: {repr_movie(mv)}")


def find_movie(title: str):
    for movie in movies:
        if movie["title"].lower() == title.lower():
            return make_movie(movie)
    return None


def main():
    # And another function here for the user menu
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection == "a":
            add_movie()
        elif selection == "l":
            list_movies()
        elif selection == "f":
            title = input("Movie title: ")
            movie = find_movie(title=title)
            print(f"You Search for {repr_movie(movie)}")
        else:
            print("Unknown command. Please try again.")

        selection = input(MENU_PROMPT)


if __name__ == '__main__':
    main()
