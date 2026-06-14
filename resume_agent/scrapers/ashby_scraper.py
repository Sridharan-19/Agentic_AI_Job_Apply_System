from resume_agent.models.job_model import Job


ASHBY_COMPANIES = {

    "ElevenLabs":
    "https://jobs.ashbyhq.com/elevenlabs",

    "Cognition":
    "https://jobs.ashbyhq.com/cognition",

    "Clay":
    "https://jobs.ashbyhq.com/clay",

    "Mercor":
    "https://jobs.ashbyhq.com/mercor",

    "Glean":
    "https://jobs.ashbyhq.com/glean",

    "Windsurf":
    "https://jobs.ashbyhq.com/windsurf"

}


def fetch_ashby_jobs():

    jobs = []

    for company, url in ASHBY_COMPANIES.items():

        jobs.append(

            Job(

                title="AI Roles",

                company=company,

                url=url,

                location="Remote",

                salary="",

                remote=True,

                jd="LLM Agentic AI RAG",

                source="Ashby"

            )

        )

    return jobs