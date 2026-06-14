import requests

from resume_agent.models.job_model import Job


YC_COMPANIES = {

    "Airbyte":
    "https://airbyte.com/careers",

    "Supabase":
    "https://supabase.com/careers",

    "Qdrant":
    "https://qdrant.tech/careers",

    "Mintlify":
    "https://mintlify.com/careers",

    "Langfuse":
    "https://langfuse.com/careers",

    "Unstructured":
    "https://unstructured.io/careers"

}


def fetch_yc_jobs():

    jobs = []

    for company, url in YC_COMPANIES.items():

        jobs.append(

            Job(

                title="AI/ML Roles",

                company=company,

                url=url,

                location="Remote",

                salary="",

                remote=True,

                jd="Generative AI LangChain RAG Agentic AI",

                source="YC"

            )

        )

    return jobs