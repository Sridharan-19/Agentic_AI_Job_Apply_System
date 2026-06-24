from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    description = Column(Text)
    url = Column(String, unique=True)
    source = Column(String)
    created_at = Column(DateTime)

class Application(Base):
    __tablename__ = 'applications'
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer)
    status = Column(String)
    applied_at = Column(DateTime)
    resume_path = Column(String)
    notes = Column(Text)
