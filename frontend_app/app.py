import streamlit as st
from response import get_movies, get_recommendations

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title(" Movie Recommender System")



def movies():
    if not hasattr(movies, "_cache"):
        movies._cache = get_movies()
    return movies._cache
# movies = get_movies()

# select box for movies
selected_movie = st.selectbox(
    "Select a Movie",
    movies
)

# Recommend button
if st.button("Recommend"):

    with st.spinner("Fetching recommendations..."):

        data, error = get_recommendations(selected_movie)

        if error:
            st.error(error)
        else:
            st.subheader(f"Recommendations for {data['movie']}")

            # Getting 5 movies
            cols = st.columns(5)

            for idx, movie in enumerate(data["recommendations"]):
                with cols[idx]:
                    st.image(movie["poster"])
                    st.caption(movie["title"])