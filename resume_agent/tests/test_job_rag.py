from resume_agent.agents.search_agent import SearchAgent

from resume_agent.job_rag.job_ranker import JobRanker

from resume_agent.profile.profile_builder import (
    ProfileBuilder
)


agent = SearchAgent()

jobs = agent.run()


builder = ProfileBuilder()

profile_text = (

    builder.build_profile_text()

)


ranker = JobRanker(

    jobs,

    profile_text

)


results = ranker.rank(

    k=10

)


for job, score in results:

    print()

    print(

        job.source

    )

    print(

        job.company

    )

    print(

        job.title

    )

    print(

        round(

            score,

            3

        )

    )