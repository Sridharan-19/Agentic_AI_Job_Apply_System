from resume_agent.scrapers.remoteok_scraper import (fetch_remoteok_jobs)

from resume_agent.utils.job_filter import (
    filter_jobs
)

jobs = fetch_remoteok_jobs()

jobs = filter_jobs(jobs)

print(

    f"Relevant jobs found: {len(jobs)}"
)

for job in jobs:

    print()

    print(
        job.company
    )

    print(
        job.title
    )