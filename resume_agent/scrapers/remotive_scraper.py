import requests

from resume_agent.models.job_model import Job


URL = "https://remotive.com/api/remote-jobs"


def fetch_remotive_jobs():

    jobs = []

    try:

        response = requests.get(
            URL,
            timeout=30
        )

        data = response.json()

        for item in data.get(
                "jobs",
                []
        ):

            jobs.append(

                Job(

                    title=item.get(
                        "title",
                        ""
                    ),

                    company=item.get(
                        "company_name",
                        ""
                    ),

                    url=item.get(
                        "url",
                        ""
                    ),

                    location=item.get(
                        "candidate_required_location",
                        ""
                    ),

                    salary=item.get(
                        "salary",
                        ""
                    ),

                    remote=True,

                    jd=item.get(
                        "description",
                        ""
                    ),

                    source="Remotive"

                )

            )

    except Exception as e:

        print(
            "Remotive:",
            e
        )

    return jobs