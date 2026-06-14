from dataclasses import dataclass


@dataclass
class Job:

    title: str

    company: str

    url: str

    location: str

    salary: str

    remote: bool

    jd: str

    source: str = ""

    skills: list = None

    posted_date: str = ""