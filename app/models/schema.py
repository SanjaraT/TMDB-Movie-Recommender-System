from pydantic import BaseModel
from typing import List


class MovieResponse(BaseModel):
    title: str
    poster: str


class RecommendationResponse(BaseModel):
    movie: str
    recommendations: List[MovieResponse]