from resume_agent.appliers.apply_router import (
    ApplyRouter
)

router = ApplyRouter()

def apply_node(state):

    applied = []

    for job, score, resume_path in state["tailored_resumes"]:

        success = agent.apply(

            job,

            resume_path

        )

        applied.append(

            (

                job,

                success

            )

        )

    return {

        "applied_jobs": applied

    }