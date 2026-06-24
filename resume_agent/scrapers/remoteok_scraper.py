import requests
from bs4 import BeautifulSoup

from resume_agent.models.job_model import Job

URL = "https://remoteok.com/api"

def fetch_remoteok_jobs():

    response = requests.get(

        URL,

        headers={

            "User-Agent":
            "Mozilla/5.0"

        }

    )

    data = response.json()

    jobs = []

    for item in data[1:]:

        jobs.append(

            Job(

                title=item.get(
                    "position",
                    ""
                ),

                company=item.get(
                    "company",
                    ""
                ),

                url=item.get(
                    "url",
                    ""
                ),

                location=item.get(
                    "location",
                    ""
                ),

                salary="",

                remote=True,

                jd=BeautifulSoup(item.get("description", ""), "html.parser").text.strip() if item.get("description") else " ".join(item.get("tags", []))

            )

        )

    return jobs