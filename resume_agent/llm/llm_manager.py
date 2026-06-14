from resume_agent.llm.nvidia_client import (
NvidiaClient
)

class LLMManager:

    def __init__(self):

        self.llm = NvidiaClient()

    def invoke(

            self,

            prompt

    ):

        return (

            self.llm.invoke(

                prompt

            )

        )