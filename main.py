
from fastapi import FastAPI
from src.api.movies import router as movies_router

app = FastAPI(title="OTT Content Aggregator API")


@app.get("/")
def home():
    return {"message": "Welcome to OTT Content Aggregator API"}


app.include_router(movies_router)
