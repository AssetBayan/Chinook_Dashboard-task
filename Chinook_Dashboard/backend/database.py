# backend/database.py
# Chinook.sqlite 연결 및 쿼리 함수

import sqlite3
from pathlib import Path
from typing import List, Dict

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "Chinook.sqlite"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_top_artists_data(limit: int = 10) -> List[Dict]:
    """
    트랙 수 기준 상위 아티스트 조회.
    Chinook 기본 스키마 기준:
    Artist(ArtistId, Name)
    Album(AlbumId, ArtistId)
    Track(TrackId, AlbumId)
    """
    conn = get_connection()
    cur = conn.cursor()
    query = """
        SELECT
            ar.Name AS ArtistName,
            COUNT(t.TrackId) AS TrackCount
        FROM Artist ar
        JOIN Album al ON ar.ArtistId = al.ArtistId
        JOIN Track t ON al.AlbumId = t.AlbumId
        GROUP BY ar.ArtistId, ar.Name
        ORDER BY TrackCount DESC
        LIMIT ?
    """
    cur.execute(query, (limit,))
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]
