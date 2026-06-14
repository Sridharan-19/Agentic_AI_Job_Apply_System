import streamlit as st

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]

sys.path.append(
    str(ROOT_DIR)
)

st.set_page_config(

    page_title="AI Career Agent",

    page_icon="🚀",

    layout="wide"

)

st.title(

    "🚀 Autonomous AI Career Agent"

)

st.write(

    "Dashboard"
)