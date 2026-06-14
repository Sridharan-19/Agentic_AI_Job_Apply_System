import requests

from resume_agent.models.job_model import Job


GREENHOUSE_COMPANIES = [

    "cursor",

    "modal",

    "runway",

    "baseten",

    "cartesia",

    "harvey",

    "gretel",

    "turing"

]


def fetch_greenhouse_jobs():

    jobs = []

    for company in GREENHOUSE_COMPANIES:

        try:

            url = (

                f"https://boards-api.greenhouse.io/v1/boards/"

                f"{company}/jobs"

            )

            response = requests.get(

                url,

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

                        company=company,

                        url=item.get(

                            "absolute_url",

                            ""

                        ),

                        location=item.get(

                            "location",

                            {}

                        ).get(

                            "name",

                            ""

                        ),

                        salary="",

                        remote=True,

                        jd="",

                        source="Greenhouse"

                    )

                )

        except Exception as e:

            print(
                company,
                e
            )

    return jobs