from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Movie Recommender API",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Movie Recommender API is running"}