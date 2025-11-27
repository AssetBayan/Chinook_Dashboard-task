# Chinook_Dashboard-task
# 🎵 Chinook Dashboard (FastAPI + SQLite + Streamlit)

Chinook 음악 데이터베이스를 기반으로  
FastAPI 백엔드와 Streamlit 프론트엔드로 구성된  
간단한 **MVC 구조 대시보드** 프로젝트입니다.

---

## 📂 Project Structure

Chinook_Dashboard/
│
├── Chinook.sqlite # SQLite 음악 데이터베이스
│
├── backend/ # FastAPI 백엔드
│ ├── database.py # DB 연결 및 쿼리 함수
│ ├── schemas.py # Pydantic 모델
│ └── main.py # FastAPI 엔드포인트
│
└── frontend/ # Streamlit 프론트엔드
└── app.py # 대시보드 UI

yaml
코드 복사

---

## ⚙️ Setup & Install

필요한 라이브러리 설치:

pip install fastapi uvicorn streamlit requests pandas plotly

yaml
코드 복사

---

## 🗄️ 1) Run FastAPI Backend

uvicorn backend.main:app --reload --port 8000

yaml
코드 복사

API 예시:  
http://127.0.0.1:8000/top_artists/10  
API 문서:  
http://127.0.0.1:8000/docs

---

## 🖥️ 2) Run Streamlit Dashboard

streamlit run frontend/app.py

yaml
코드 복사

대시보드 실행:  
http://localhost:8501

---

## 🔌 API Endpoint

- `GET /top_artists/{limit}`  
  - 트랙 수 기준 상위 아티스트 조회  
  - 예: `/top_artists/10`

---

## 📊 Features

- 🎤 상위 아티스트 Top N 조회  
- 📈 Plotly 막대 그래프 시각화  
- 🔗 FastAPI → Streamlit 연동  
- 📦 MVC 기반 구조 (Model / Controller / View 분리)

---

## 👤 Author

**Asset Bayan**  
Kyungbok University • Big Data Department
