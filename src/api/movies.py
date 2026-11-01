
from fastapi import APIRouter
from src.services.movie_service import get_all_movies

router = APIRouter()


@router.get("/movies")
def get_movies(genre: str | None = None):
    return get_all_movies(genre)
