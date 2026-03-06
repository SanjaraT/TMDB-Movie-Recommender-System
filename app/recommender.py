import pickle
import pandas as pd
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

movies_dict = pickle.load(open(BASE_DIR / "model/movie_dict.pkl", "rb"))
similarity = pickle.load(open(BASE_DIR / "model/similarity.pkl", "rb"))

movies = pd.DataFrame(movies_dict)

API_KEY = "54c4036453b0e10f7accc5c3b69d15fb"

# fetching the poster from the website
def fetch_poster(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    # converting response into json dict
    data = requests.get(url).json()

    # full image path
    poster_path = data.get("poster_path")
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return ""

# extracting movie titles + converting to list
def get_all_movies():
    return movies["title"].values.tolist()


def get_recommendations(movie_name: str):

    if movie_name not in movies["title"].values:
        return None

    # getting movie index
    movie_index = movies[movies["title"] == movie_name].index[0]

    # similarity score
    distances = similarity[movie_index]

    # sorting
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    results = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        poster = fetch_poster(movie_id)

        results.append({
            "title": movies.iloc[i[0]].title,
            "poster": poster
        })

    return results