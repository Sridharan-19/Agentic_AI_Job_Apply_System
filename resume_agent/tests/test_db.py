from datetime import datetime

from resume_agent.database.sqlite_manager import SQLiteManager

from resume_agent.models.job_model import Job

db = SQLiteManager()

job = Job(

title="Senior AI Engineer",

company="OpenAI",

url="https://openai.com/careers",

location="Remote",

salary="$200k",

remote=True,

jd="Python LangGraph Agentic AI"

)

db.save_job(job)

job_id = db.get_job_id(

job.url

)

db.save_resume(job_id, "resume_agent/outputs/resumes/openai.md")

db.save_application(job_id,"PENDING", datetime.now())

print(db.get_jobs())


print(db.get_applications())