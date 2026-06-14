from pathlib import Path

import streamlit as st
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]

sys.path.append(
    str(ROOT_DIR)
)

folder = Path(

    "resume_agent/outputs/resumes"

)

st.title(

    "Resume Versions"

)

for file in folder.glob(

        "*.md"

):

    st.write(

        file.name

    )