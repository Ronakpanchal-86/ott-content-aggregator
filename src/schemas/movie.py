
from pydantic import BaseModel, Field


class MovieSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    genre: str
    platform: str
    release_year: int
