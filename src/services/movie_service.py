
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

def add_movie(movie):
    new_movie = {
        "id": len(movies) + 1,
        **movie.model_dump()
    }

    movies.append(new_movie)

    return new_movie

def update_movie(movie_id, movie):
    for index, existing_movie in enumerate(movies):
        if existing_movie["id"] == movie_id:
            updated_movie = {
                "id": movie_id,
                **movie.model_dump()
            }

            movies[index] = updated_movie
            return updated_movie

    return None    

def delete_movie(movie_id):
    for index, movie in enumerate(movies):
        if movie["id"] == movie_id:
            return movies.pop(index)

    return None

def get_movie_by_id(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie

    return None