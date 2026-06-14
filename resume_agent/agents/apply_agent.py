from datetime import datetime

from resume_agent.appliers.greenhouse_applier import (
GreenhouseApplier
)

from resume_agent.appliers.ashby_applier import (
AshbyApplier
)

from resume_agent.database.sqlite_manager import (
SQLiteManager
)

class ApplyAgent:

    def __init__(self):

        self.greenhouse = GreenhouseApplier()

        self.ashby = AshbyApplier()

        self.db = SQLiteManager()


    def apply(

            self,

            job,

            resume_path

    ):

        success = False


        if job.source == "Greenhouse":

            success = (

                self.greenhouse.apply(

                    job,

                    resume_path

                )

            )


        elif job.source == "Ashby":

            success = (

                self.ashby.apply(

                    job,

                    resume_path

                )

            )


        else:

            print(

                f"No applier for {job.source}"

            )


        status = (

            "APPLIED"

            if success

            else

            "FAILED"

        )


        self.db.save_application(

            job_id=1,

            status=status,

            applied_at=datetime.now(),

            resume_path=resume_path,

            notes=f"{job.company} - {job.title}"

        )


        return success