from resume_agent.agents.tailor_agent import TailorAgent


agent = TailorAgent()


def tailor_node(state):

    resumes = []

    for job, score in state["approved_jobs"]:

        resume_path = agent.tailor_resume(

            job.jd,

            job.company

        )

        resumes.append(

            (

                job,
                score,
                resume_path

            )

        )

    return {

        "tailored_resumes": resumes

    }