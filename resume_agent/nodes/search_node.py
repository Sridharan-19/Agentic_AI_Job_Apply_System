from resume_agent.agents.search_agent import SearchAgent


agent = SearchAgent()


def search_node(state):

    jobs = agent.run()

    return {

        "jobs": jobs

    }