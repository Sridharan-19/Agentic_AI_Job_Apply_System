from resume_agent.job_rag.job_ranker import JobRanker
from resume_agent.profile.profile_builder import ProfileBuilder


builder = ProfileBuilder()


def rank_node(state):

    profile_text = builder.build_profile_text()

    ranker = JobRanker(

        state["jobs"],

        profile_text

    )

    ranked = ranker.rank(

        k=10

    )

    return {

        "ranked_jobs": ranked

    }