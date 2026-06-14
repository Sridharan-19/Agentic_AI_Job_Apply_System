from resume_agent.database.sqlite_manager import (
    SQLiteManager
)

db = SQLiteManager()

print(

    db.get_application_summary()

)