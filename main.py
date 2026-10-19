
from fastapi import FastAPI

app = FastAPI(title="NeuralForge")


@app.get("/")
def home():
    return {"message": "Welcome to NeuralForge"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "Hello, NeuralForge!"}


@app.get("/search")
def search_hotels(city: str, max_price: int = None):
    return {
        "city": city,
        "max_price": max_price,
        "hotels": []
    }