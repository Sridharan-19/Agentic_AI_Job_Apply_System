import streamlit as st
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]

sys.path.append(
    str(ROOT_DIR)
)

from resume_agent.database.sqlite_manager import (
    SQLiteManager
)

db = SQLiteManager()

summary = db.get_application_summary()

st.title(

    "Metrics"

)

for status, count in summary:

    st.metric(

        status,

        count

    )