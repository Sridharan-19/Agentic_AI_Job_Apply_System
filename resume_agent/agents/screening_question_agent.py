from resume_agent.profile.profile_loader import (
    ProfileLoader
)

from resume_agent.vectorstore.resume_rag import (
    ResumeRAG
)

from resume_agent.llm.llm_manager import (
    LLMManager
)


class ScreeningQuestionAgent:

    def __init__(self):

        self.profile = (

            ProfileLoader()

            .get()

        )

        self.rag = ResumeRAG()

        self.llm = LLMManager()

    def choose_option(
            self,
            question,
            options
        ):

            prompt = f"""

        You are answering a job application question.

        Question:

        {question}

        Available Options:

        {options}

        Rules:

        1. Choose exactly one option.
        2. Return only the option text.
        3. Do not explain.
        4. Never invent new options.

        Answer:

        """

            answer = self.llm.invoke(

                prompt

            )

            return answer.strip()


    def answer_question(

            self,

            question

    ):

        docs = (

            self.rag.retrieve(

                question,

                k=3

            )

        )

        context = ""

        for doc in docs:

            context += (

                doc["text"]

                +

                "\n\n"

            )

        prompt = f"""

You are answering a job application question.

Rules:

1. Never invent information.
2. Use only candidate profile and experience.
3. Keep answers concise.
4. Keep answers professional.
5. Maximum 150 words.

Candidate Profile:

{self.profile}

Relevant Experience:

{context}

Question:

{question}

Answer:

"""

        return (

            self.llm.invoke(

                prompt

            )

        )