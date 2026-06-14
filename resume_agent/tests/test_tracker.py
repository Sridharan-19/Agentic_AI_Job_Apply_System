from datetime import datetime

from resume_agent.database.sqlite_manager import (
    SQLiteManager
)


db = SQLiteManager()


db.save_application(

    job_id=1,

    status="APPLIED",

    applied_at=datetime.now(),

    resume_path="outputs/resumes/turing.md",

    notes="Initial application"

)


db.update_application(

    1,

    "INTERVIEW",

    "Interview scheduled",

    datetime.now()

)


print(

    db.get_by_status(

        "INTERVIEW"

    )

)