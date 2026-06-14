from resume_agent.appliers.greenhouse_applier import (
GreenhouseApplier
)

from resume_agent.models.job_model import (
Job
)

job = Job(


title="Staff Forward Deployed AI Engineer",

company="Turing",

url="https://job-boards.greenhouse.io/turing/jobs/8229975002",

location="Remote",

salary="",

remote=True,

jd="",

source="Greenhouse"


)

resume_path = (


"resume_agent/outputs/resumes/turing.pdf"


)

GreenhouseApplier().apply(


job,

resume_path


)
