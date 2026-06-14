from resume_agent.appliers.greenhouse_applier import (
    GreenhouseApplier
)

from resume_agent.appliers.ashby_applier import (
    AshbyApplier
)

from resume_agent.appliers.lever_applier import (
    LeverApplier
)


class ApplyRouter:

    def apply(

            self,

            job,

            resume_path

    ):

        if job.source == "Greenhouse":

            return (

                GreenhouseApplier()

                .apply(

                    job,

                    resume_path

                )

            )

        elif job.source == "Ashby":

            return (

                AshbyApplier()

                .apply(

                    job,

                    resume_path

                )

            )

        elif job.source == "Lever":

            return (

                LeverApplier()

                .apply(

                    job,

                    resume_path

                )

            )

        else:

            print(

                "Unsupported source"

            )

            return False