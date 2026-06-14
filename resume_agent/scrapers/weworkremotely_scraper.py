import requests

from bs4 import BeautifulSoup

from resume_agent.models.job_model import Job


URL = "https://weworkremotely.com/remote-jobs"


def fetch_weworkremotely_jobs():

    jobs = []

    try:

        response = requests.get(

            URL,

            headers={

                "User-Agent":
                "Mozilla/5.0"

            }

        )

        soup = BeautifulSoup(

            response.text,

            "html.parser"

        )

        for section in soup.find_all(

                "li"

        ):

            try:

                title = section.find(

                    "span",

                    class_="title"

                )

                company = section.find(

                    "span",

                    class_="company"

                )

                href = section.find(

                    "a"

                )

                if (

                        title

                        and company

                        and href

                ):

                    jobs.append(

                        Job(

                            title=title.text.strip(),

                            company=company.text.strip(),

                            url="https://weworkremotely.com"
                            + href["href"],

                            location="Remote",

                            salary="",

                            remote=True,

                            jd="",

                            source="WeWorkRemotely"

                        )

                    )

            except:

                pass

    except Exception as e:

        print(
            "WWR:",
            e
        )

    return jobs