import requests
import time
from config import API_URL


def get_movies():
    for _ in range(3):  # retry 3 times
        try:
            res = requests.get(f"{API_URL}/movies", timeout=10)
            if res.status_code == 200:
                return res.json()["movies"]
        except:
            time.sleep(3)  # wait for backend to wake up
    return []
# def get_movies():
#     response = requests.get(f"{API_URL}/movies")
#     return response.json()["movies"]


def get_recommendations(movie):
    for _ in range(3):
        try:
            res = requests.get(f"{API_URL}/recommend/{movie}", timeout=10)
            if res.status_code == 200:
                return res.json(), None
        except:
            time.sleep(3)

    return None, "Backend is waking up, please try again."