import streamlit as st
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]

sys.path.append(
    str(ROOT_DIR)
)

from resume_agent.agents.tracker_agent import (
    TrackerAgent
)


tracker = TrackerAgent()

st.title(

    "Offers"

)

rows = tracker.offers()

for row in rows:

    st.write(

        row

    )