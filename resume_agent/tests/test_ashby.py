from resume_agent.appliers.ashby_applier import (
    AshbyApplier
)

from resume_agent.models.job_model import (
    Job
)


job = Job(

    title="AI Engineer",

    company="ElevenLabs",

    url="https://jobs.ashbyhq.com/elevenlabs",

    location="Remote",

    salary="",

    remote=True,

    jd="",

    source="Ashby"

)

AshbyApplier().apply(

    job,

    "resume_agent/outputs/resumes/elevenlabs.pdf"

)