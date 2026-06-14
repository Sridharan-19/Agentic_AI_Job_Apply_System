from ollama import chat

response = chat(
    model="gemma3:4b",
    messages=[
        {
            "role": "user",
            "content": "Who are you?"
        }
    ]
)

print(
    response["message"]["content"]
)