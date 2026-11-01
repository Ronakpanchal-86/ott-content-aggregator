
from fastapi import FastAPI

app = FastAPI(title="OTT Content Aggregator API")


@app.get("/")
def home():
    return {"message": "Welcome to OTT Content Aggregator API"}


@app.get("/movies")
def get_movies(genre: str | None = None):
    movies = [
        {"id": 1, "title": "Inception", "genre": "Sci-Fi"},
        {"id": 2, "title": "Interstellar", "genre": "Sci-Fi"},
        {"id": 3, "title": "3 Idiots", "genre": "Comedy"},
    ]

    if genre:
        movies = [
            movie for movie in movies
            if movie["genre"].lower() == genre.lower()
        ]

    return movies
