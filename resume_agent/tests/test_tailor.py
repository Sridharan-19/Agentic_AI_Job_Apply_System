from resume_agent.agents.tailor_agent import TailorAgent

job_description = """

Looking for a Senior AI Engineer.

Requirements:

Python
LangGraph
Playwright
RAG
Gemma
FAISS
Docker
Agentic AI

"""

agent = TailorAgent()

path = agent.tailor_resume(job_description,"openai")

print("Resume saved to:")

print(path)
