import requests

from resume_agent.models.job_model import Job


LEVER_COMPANIES = [

    "perplexity-ai",

    "elevenlabs",

    "windsurf",

    "cognition",

    "scaleai",

    "glean"

]


def fetch_lever_jobs():

    jobs = []

    for company in LEVER_COMPANIES:

        try:

            url = (

                f"https://api.lever.co/v0/postings/"
                f"{company}"

            )

            response = requests.get(
                url,
                timeout=30
            )
            data = response.json()

            print(company)
            print(type(data))
            print(data.keys())

            return []
            # data = response.json()    

            # for item in data:

            #     jobs.append(

            #         Job(

            #             title=item.get(
            #                 "text",
            #                 ""
            #             ),

            #             company=company,

            #             url=item.get(
            #                 "hostedUrl",
            #                 ""
            #             ),

            #             location=item.get(
            #                 "categories",
            #                 {}
            #             ).get(
            #                 "location",
            #                 ""
            #             ),

            #             salary="",

            #             remote=True,

            #             jd=""

            #         )

            #     )

        except Exception as e:

            print(
                company,
                e
            )

    return jobs