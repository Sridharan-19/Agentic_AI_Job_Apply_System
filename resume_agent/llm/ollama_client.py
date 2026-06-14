from ollama import Client

class OllamaClient:

    def __init__(
            self,
            model="gemma3:4b"
    ):

        self.client = Client()

        self.model = model

    def invoke(
            self,
            prompt
    ):

        response = self.client.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response["message"]["content"]