print()

print("=" * 80)

print("STARTING NVIDIA API TEST")

print("=" * 80)

from resume_agent.llm.nvidia_client import (
NvidiaClient
)

print()

print("Creating Nvidia client...")

llm = NvidiaClient()

print()

print("Calling invoke()...")

try:
    response = llm.invoke(

        "Hello, introduce yourself."

    )

    print()

    print("=" * 80)

    print("RESPONSE")

    print("=" * 80)

    print()

    print(response)
except Exception as e:


    print()

    print("=" * 80)

    print("ERROR")

    print("=" * 80)

    print()

    print(type(e))

    print(e)