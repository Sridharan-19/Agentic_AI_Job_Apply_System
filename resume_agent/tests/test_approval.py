from resume_agent.agents.search_agent import (
    SearchAgent
)

from resume_agent.job_rag.job_ranker import (
    JobRanker
)

from resume_agent.profile.profile_builder import (
    ProfileBuilder
)

from resume_agent.nodes.approval_node import (
    approval_node
)


jobs = SearchAgent().run()

profile = (

    ProfileBuilder()

    .build_profile_text()

)

ranker = JobRanker(

    jobs,

    profile

)

ranked_jobs = ranker.rank(

    k=5

)

state = {

    "ranked_jobs":

    ranked_jobs

}

result = approval_node(

    state

)

print()

print(

    result

)