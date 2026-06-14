from resume_agent.profile_rag.profile_rag import (
    ProfileRAG
)


rag = ProfileRAG()


results = rag.retrieve(

    "Agentic AI LangGraph RAG",

    k=5

)


for doc, score in results:

    print()

    print(

        round(

            score,

            3

        )

    )

    print(

        doc["text"][:300]

    )