from resume_agent.agents.search_agent import SearchAgent

from resume_agent.agents.apply_agent import (
    ApplyAgent
)


search_agent = SearchAgent()

jobs = search_agent.run()


apply_agent = ApplyAgent()


for job in jobs:

    if job.source in [

            "Greenhouse",

            "Ashby"

    ]:

        apply_agent.apply(

            job,

            "resume_agent/outputs/resumes/openai.md"

        )

        break