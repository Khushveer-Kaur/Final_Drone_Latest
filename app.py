import streamlit as st
import os

st.set_page_config(layout="wide", page_title="Drone Mission Dashboard")

st.title("🚁 Autonomous Drone Mission Control")

st.markdown("""
This dashboard shows real-time drone telemetry, path tracking, safety alerts,
and mission control systems.
""")

backend_url = os.environ.get("BACKEND_URL", "http://localhost:5050")
st.components.v1.iframe(backend_url, height=900, scrolling=True)