from resume_agent.vectorstore.resume_rag import ResumeRAG

rag = ResumeRAG()

docs = rag.retrieve(
    "Agentic AI Resume Automation Docker"
)

for doc in docs:

    print("\n")
    print("=" * 80)

    print(
        doc["title"]
    )

    print()

    print(
        "Vector Score:",
        round(
            doc["vector_score"],
            3
        )
    )

    print(
        "Final Score:",
        round(
            doc["final_score"],
            3
        )
    )

    print()

    print(
        "Domain:",
        doc["domain"]
    )

    print(
        "Project Type:",
        doc["project_type"]
    )

    print()

    print(
        "Importance:",
        doc["importance"]
    )

    print()

    print(
        "Skills:"
    )

    print(
        ", ".join(
            doc["skills"]
        )
    )

    print()

    print(
        "Impact:"
    )

    for impact in doc["impact"]:

        print(
            "-",
            impact
        )
