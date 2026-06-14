from resume_agent.scrapers.remoteok_scraper import fetch_remoteok_jobs
from resume_agent.scrapers.remotive_scraper import fetch_remotive_jobs
from resume_agent.scrapers.weworkremotely_scraper import fetch_weworkremotely_jobs
from resume_agent.scrapers.greenhouse_scraper import fetch_greenhouse_jobs
from resume_agent.scrapers.yc_scraper import fetch_yc_jobs
from resume_agent.scrapers.ashby_scraper import fetch_ashby_jobs

from resume_agent.utils.deduplicator import deduplicate_jobs
from resume_agent.utils.job_filter import filter_jobs

from resume_agent.database.sqlite_manager import SQLiteManager


class SearchAgent:

    def __init__(self):

        self.db = SQLiteManager()

    def run(self):

        jobs = []

        jobs.extend(

            fetch_remoteok_jobs()

        )

        jobs.extend(

            fetch_remotive_jobs()

        )

        jobs.extend(

            fetch_weworkremotely_jobs()

        )

        jobs.extend(

            fetch_greenhouse_jobs()

        )

        jobs.extend(

            fetch_yc_jobs()

        )

        jobs.extend(

            fetch_ashby_jobs()

        )

        jobs = deduplicate_jobs(

            jobs

        )

        jobs = filter_jobs(

            jobs

        )

        for job in jobs:

            self.db.save_job(

                job

            )

        return jobs