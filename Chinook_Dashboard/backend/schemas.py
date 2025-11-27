# backend/schemas.py
# Pydantic 모델 정의

from pydantic import BaseModel


class TopArtist(BaseModel):
    ArtistName: str
    TrackCount: int
