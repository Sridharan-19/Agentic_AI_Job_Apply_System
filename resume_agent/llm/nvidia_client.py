from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve().parents[2]

load_dotenv(
ROOT_DIR / ".env"
)

class NvidiaClient:

    def __init__(self):

        api_key = os.getenv(
            "NVIDIA_API_KEY"
        )

        self.client = OpenAI(

            base_url="https://integrate.api.nvidia.com/v1",

            api_key=api_key

        )

    def invoke(

            self,

            prompt,

            temperature=0.2,

            max_tokens=4096

    ):

        response = (

            self.client.chat.completions.create(

                model="meta/llama-3.3-70b-instruct",

                messages=[

                    {

                        "role": "user",

                        "content": prompt

                    }

                ],

                temperature=temperature,

                max_tokens=max_tokens

            )

        )

        return (

            response

            .choices[0]

            .message.content

        )