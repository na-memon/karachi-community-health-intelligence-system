from pathlib import Path
import pandas as pd
import streamlit as st

# Determine the directory where app.py resides
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = (
    BASE_DIR.parent
    / "data"
    / "Karachi Community Health Surveillance Analytics System_cleaned.xlsx"
)


@st.cache_data
def load_data():
  if not DATA_PATH.exists():
    return None
  return pd.read_excel(DATA_PATH)


df = load_data()

# Graceful error handling so the server never crashes
if df is None:
  st.error(
      "⚠️ **Dataset File Missing on GitHub Repository!**\n\nStreamlit Cloud"
      f" could not find the Excel file at:\n`{DATA_PATH}`\n\n**How to"
      " fix:** Make sure your cleaned Excel file is committed and pushed inside"
      " the `data/` folder on your GitHub repository."
  )
  st.stop()