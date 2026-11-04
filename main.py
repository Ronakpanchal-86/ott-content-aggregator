from fastapi import FastAPI
from src.api.movies import router as movies_router
from src.api.users import router as users_router

app = FastAPI(title="OTT Content Aggregator API")


@app.get("/")
def home():
    return {"message": "Welcome to OTT Content Aggregator API"}


app.include_router(movies_router)
app.include_router(users_router)