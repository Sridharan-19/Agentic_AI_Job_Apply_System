from pathlib import Path
from datetime import datetime
import yaml

from resume_agent.vectorstore.resume_rag import ResumeRAG
# from resume_agent.llm.ollama_client import OllamaClient
from resume_agent.llm.llm_manager import (
    LLMManager
)
from resume_agent.profile.profile_loader import (
    ProfileLoader
)

class TailorAgent:

    def __init__(self):

        self.rag = ResumeRAG()

        self.llm = LLMManager()
        self.profile = (ProfileLoader().get())

        with open(
                "resume_agent/prompts/tailoring_prompt.txt",
                encoding="utf-8"
        ) as f:

            self.prompt_template = f.read()


    def build_profile_context(self):

        skills = []

        for category in (

                self.profile["skills"]

                .values()

        ):

            skills.extend(

                category

            )

        skills_str = ", ".join(

            skills

        )

        certifications = ", ".join(

            self.profile["certifications"]

        )

        preferred_roles = ", ".join(

            self.profile["preferred_roles"]

        )

        previous_companies = []

        for company in self.profile["previous_companies"]:

            previous_companies.append(

                f'{company["role"]} at {company["company"]}'

            )

        previous_exp = "\n".join(

            previous_companies

        )

        return f"""

        Name:
        {self.profile["name"]}

        Email:
        {self.profile["email"]}

        Phone:
        {self.profile["phone"]}

        Current Role:
        {self.profile["current_role"]}

        Years of Experience:
        {self.profile["experience_years"]}

        Current Company:
        {self.profile["current_company"]["company"]}

        Preferred Roles:
        {preferred_roles}

        Skills:
        {skills_str}

        Certifications:
        {certifications}

        Previous Experience:

        {previous_exp}

        Current Projects:

        {", ".join(self.profile["current_projects"])}

        Expected Salary:
        ${self.profile["expected_salary"]["amount"]}/{self.profile["expected_salary"]["period"]}

        Notice Period:
        {self.profile["notice_period"]}

        """

    def build_project_context(
            self,
            docs
        ):

        context = ""

        for doc in docs:

            context += f"""
            Title:
            {doc["title"]}

            Domain:
            {doc["domain"]}

            Project Type:
            {doc["project_type"]}

            Skills:
            {", ".join(doc["skills"])}

            Technologies:
            {", ".join(doc["technologies"])}

            Impact:
            {", ".join(doc["impact"])}

            Description:

            {doc["text"]}

            """


        return context

    def tailor_resume(
            self,
            job_description,
            company
        ):

        docs = self.rag.retrieve(
            job_description,
            k=5
        )

        profile_context = self.build_profile_context()

        project_context = self.build_project_context(
            docs
        )

        prompt = self.prompt_template.format(

            profile=profile_context,

            job_description=job_description,

            projects=project_context

        )

        resume_md = self.llm.invoke(
            prompt
        )

        print("=" * 80)
        print("RESUME GENERATED")
        print("=" * 80)
        print(resume_md)
        print("=" * 80)

        output_dir = Path(
            "resume_agent/outputs/resumes"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        output_path = (

            output_dir

            /

            f"{company}_{timestamp}.md"

        )

        if not resume_md:
            raise Exception( "LLM returned empty response")
        output_path.write_text(resume_md, encoding="utf-8")

        return output_path 