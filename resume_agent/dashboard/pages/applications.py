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

rows = db.get_all_applications()

st.title(

    "Applications"

)

st.dataframe(

    rows,

    use_container_width=True

)