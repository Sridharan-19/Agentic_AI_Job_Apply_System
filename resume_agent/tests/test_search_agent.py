from resume_agent.agents.search_agent import SearchAgent


agent = SearchAgent()

jobs = agent.run()

print()

print(

    f"Relevant jobs found: {len(jobs)}"

)

for job in jobs[:20]:

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