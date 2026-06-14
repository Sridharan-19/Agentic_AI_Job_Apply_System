from resume_agent.database.sqlite_manager import (
SQLiteManager
)

class TrackerAgent:

    def __init__(self):

        self.db = SQLiteManager()

    def interviews(self):

        return self.db.get_by_status(

            "INTERVIEW"

        )

    def offers(self):

        return self.db.get_by_status(

            "OFFER"

        )

    def rejected(self):

        return self.db.get_by_status(

            "REJECTED"

        )

    def summary(self):

        return self.db.get_application_summary()
