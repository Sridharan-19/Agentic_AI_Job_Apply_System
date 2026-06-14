from resume_agent.profile.profile_builder import (
ProfileBuilder
)

from resume_agent.data.project_documents import (
PROJECT_DOCUMENTS
)

from resume_agent.vectorstore.embedding_manager import (
EmbeddingManager
)

from resume_agent.vectorstore.faiss_manager import (
FaissManager
)

class ProfileRAG:

    def __init__(self):

        self.embedder = EmbeddingManager()

        self.documents = []

        profile_text = (

            ProfileBuilder()

            .build_profile_text()

        )

        self.documents.append(

            {

                "text": profile_text,

                "type": "profile"

            }

        )

        self.documents.extend(

            PROJECT_DOCUMENTS

        )

        embeddings = (

            self.embedder.embed_texts(

                [

                    doc["text"]

                    for doc in self.documents

                ]

            )

        )

        dim = embeddings.shape[1]

        self.faiss_db = (

            FaissManager(

                dim

            )

        )

        self.faiss_db.add_documents(

            self.documents,

            embeddings

        )

    def retrieve(

            self,

            query,

            k=5

    ):

        q_embedding = (

            self.embedder.embed_texts(

                [

                    query

                ]

            )[0]

        )

        return (

            self.faiss_db.search(

                q_embedding,

                k

            )

        )