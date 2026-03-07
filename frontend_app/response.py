import requests
from config import API_URL


def get_movies():
    response = requests.get(f"{API_URL}/movies")
    return response.json()["movies"]


def get_recommendations(movie_name: str):
    response = requests.get(f"{API_URL}/recommend/{movie_name}")

    if response.status_code == 200:
        return response.json(), None
    else:
        return None, response.json()