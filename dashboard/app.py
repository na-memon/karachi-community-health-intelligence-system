from pathlib import Path
import pandas as pd
import streamlit as st

# Determine the directory where app.py resides
BASE_DIR = Path(__file__).resolve().parent

# Build absolute path to data file (moves 1 folder up to root, then into data/)
DATA_PATH = (
    BASE_DIR.parent
    / "data"
    / "Karachi Community Health Surveillance Analytics System_cleaned.xlsx"
)


@st.cache_data
def load_data():
  if not DATA_PATH.exists():
    raise FileNotFoundError(
      f"Dataset not found at expected path: {DATA_PATH}"
    )
  return pd.read_excel(DATA_PATH)


df = load_data()