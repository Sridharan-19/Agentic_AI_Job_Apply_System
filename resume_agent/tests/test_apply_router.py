from resume_agent.agents.search_agent import (
    SearchAgent
)

from resume_agent.appliers.apply_router import (
    ApplyRouter
)

jobs = SearchAgent().run()

router = ApplyRouter()

for job in jobs:

    if job.source == "Greenhouse":

        print()

        print(job.title)

        print(job.url)

        router.apply(

            job,

            "resume_agent/outputs/resumes/turing.pdf"

        )

        break