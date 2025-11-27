# frontend/app.py
# Streamlit 대시보드 - FastAPI에서 데이터 가져와 시각화

import requests
import pandas as pd
import plotly.express as px
import streamlit as st

API_URL = "http://127.0.0.1:8000"


st.title("🎵 Chinook Top Artists Dashboard")

limit = st.slider("Number of top artists", min_value=3, max_value=20, value=10, step=1)

if st.button("Load data") or True:
    resp = requests.get(f"{API_URL}/top_artists/{limit}")
    if resp.status_code == 200:
        data = resp.json()
        df = pd.DataFrame(data)
        st.subheader("Raw data")
        st.dataframe(df)

        st.subheader("Top Artists by Track Count")
        fig = px.bar(df, x="ArtistName", y="TrackCount", title="Top Artists by Track Count")
        fig.update_layout(xaxis_title="Artist", yaxis_title="Track Count")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error(f"Failed to load data from API: {resp.status_code}")
Запуск frontend:
streamlit run frontend/app.py
