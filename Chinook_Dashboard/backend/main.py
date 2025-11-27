# backend/main.py
# FastAPI 서버 구현

from typing import List

from fastapi import FastAPI
from . import database
from .schemas import TopArtist

app = FastAPI(title="Chinook Dashboard API")


@app.get("/top_artists/{limit}", response_model=List[TopArtist])
def get_top_artists(limit: int):
    data = database.get_top_artists_data(limit)
    return data
Запуск backend:
uvicorn backend.main:app --reload --port 8000
