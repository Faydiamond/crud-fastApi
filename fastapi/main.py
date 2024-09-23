from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app =FastAPI()

class Movie (BaseModel):
    year: int
    name: str
    director: str
    duration: Optional[float]
    gender: Optional[str]


@app.get("/")
def index():
    return { "message": "ha funcionado", "status": True }

@app.get("/movies/{id}")
def mostrarLibro(id:int):
    return {  "id" : id  }

@app.post("/movie")
def insertMovie (movie:Movie):
    return { "message" : f"pelicula {movie.name} insertada!" }

