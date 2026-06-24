import requests

from bs4 import BeautifulSoup

from resume_agent.models.job_model import Job


URL = "https://weworkremotely.com/remote-jobs"


def fetch_wwr_jd(job_url):
    try:
        response = requests.get(job_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            job_section = soup.find(id="job-section")
            if job_section:
                return job_section.text.strip()
            container = soup.find(class_="listing-container")
            if container:
                return container.text.strip()
    except Exception as e:
        print(f"Error fetching WWR JD: {e}")
    return ""


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

        # Let's limit to top 10 jobs to keep it fast
        list_items = soup.find_all("li")[:25]

        for section in list_items:

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
                    job_url = "https://weworkremotely.com" + href["href"]
                    jd_text = fetch_wwr_jd(job_url)

                    jobs.append(

                        Job(

                            title=title.text.strip(),

                            company=company.text.strip(),

                            url=job_url,

                            location="Remote",

                            salary="",

                            remote=True,

                            jd=jd_text,

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