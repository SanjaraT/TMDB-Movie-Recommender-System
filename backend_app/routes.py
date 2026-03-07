from fastapi import APIRouter, HTTPException
from recommender import get_recommendations, get_all_movies
from schema import RecommendationResponse

# router object to register endpoints
router = APIRouter()

# fetch movie titles
@router.get("/movies")
def list_movies():
    return {"movies": get_all_movies()}


# getting recommendation
@router.get("/recommend/{movie_name}", response_model=RecommendationResponse)
def recommend(movie_name: str):

    recommendations = get_recommendations(movie_name)

    # Error handling
    if recommendations is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    return {
        "movie": movie_name,
        "recommendations": recommendations
    }