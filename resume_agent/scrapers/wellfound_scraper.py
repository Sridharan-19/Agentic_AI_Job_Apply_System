import requests
from bs4 import BeautifulSoup
from loguru import logger


def fetch_wellfound_jobs():

    jobs = []

    try:

        url = (
            "https://wellfound.com/jobs"
        )

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        soup = BeautifulSoup(
            response.text,
            "lxml"
        )

        cards = soup.find_all(
            "div",
            class_="styles_component__Q4h9A"
        )

        for card in cards:

            try:

                title = card.find("h2")

                company = card.find("h3")

                jobs.append(
                    {
                        "title": (
                            title.text.strip()
                            if title
                            else ""
                        ),
                        "company": (
                            company.text.strip()
                            if company
                            else ""
                        ),
                        "source": "Wellfound",
                        "apply_url": url
                    }
                )

            except Exception:
                pass

        logger.info(
            f"Wellfound jobs fetched: {len(jobs)}"
        )

    except Exception as e:

        logger.error(e)

    return jobs