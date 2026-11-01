
movies = [
    {
        "id": 1,
        "title": "Inception",
        "genre": "Sci-Fi",
        "platform": "Netflix",
        "release_year": 2010
    },
    {
        "id": 2,
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "platform": "Prime Video",
        "release_year": 2014
    },
    {
        "id": 3,
        "title": "3 Idiots",
        "genre": "Comedy",
        "platform": "Netflix",
        "release_year": 2009
    }
]


def get_all_movies(genre=None):
    if genre:
        return [
            movie for movie in movies
            if movie["genre"].lower() == genre.lower()
        ]

    return movies

