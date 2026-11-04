from fastapi import APIRouter, status, HTTPException
from src.schemas.movie import MovieSchema
from src.services.movie_service import (
    get_all_movies,
    get_movie_by_id,
    add_movie,
    update_movie,
    delete_movie
)

router = APIRouter()


@router.get("/movies")
def get_movies(genre: str | None = None):
    return get_all_movies(genre)
@router.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    movie = get_movie_by_id(movie_id)

    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found"
        )

    return movie

@router.post("/movies", status_code=status.HTTP_201_CREATED)
def create_movie(movie: MovieSchema):
    return add_movie(movie)

@router.put("/movies/{movie_id}")
def edit_movie(movie_id: int, movie: MovieSchema):
    updated_movie = update_movie(movie_id, movie)

    if updated_movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found"
        )

    return updated_movie


@router.delete("/movies/{movie_id}")
def remove_movie(movie_id: int):
    deleted_movie = delete_movie(movie_id)

    if deleted_movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found"
    )

    return {"message": "Movie deleted successfully", "movie": deleted_movie}

