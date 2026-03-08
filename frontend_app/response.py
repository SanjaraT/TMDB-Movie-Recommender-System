import requests
import time
from config import API_URL


def get_movies(retries=5, delay=3):
    for attempt in range(retries):
        try:
            response = requests.get(f"{API_URL}/movies", timeout=15)
            response.raise_for_status()
            return response.json()["movies"]
        except (requests.exceptions.JSONDecodeError,
                requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
                KeyError) as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise Exception(f"Backend unavailable after {retries} attempts: {e}")
# def get_movies():
#     response = requests.get(f"{API_URL}/movies")
#     return response.json()["movies"]


def get_recommendations(movie_name: str):
    response = requests.get(f"{API_URL}/recommend/{movie_name}")

    if response.status_code == 200:
        return response.json(), None
    else:
        return None, response.json()