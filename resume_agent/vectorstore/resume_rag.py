from resume_agent.data.project_documents import PROJECT_DOCUMENTS
from resume_agent.vectorstore.embedding_manager import EmbeddingManager
from resume_agent.vectorstore.faiss_manager import FaissManager

class ResumeRAG:
    def __init__(self):

        self.embedder = EmbeddingManager()

        embedding_texts = [

            self.create_embedding_text(
                doc
            )

            for doc in PROJECT_DOCUMENTS
        ]

        embeddings = self.embedder.embed_texts(
            embedding_texts
        )

        dim = embeddings.shape[1]

        self.faiss_db = FaissManager(
            dim
        )

        self.faiss_db.add_documents(
            PROJECT_DOCUMENTS,
            embeddings
        )

    def create_embedding_text(
            self,
            doc
    ):

        return f"""

        Title:
        {doc.get('title', '')}

        Domain:
        {doc.get('domain', '')}

        Industry:
        {doc.get('industry', '')}

        Project Type:
        {doc.get('project_type', '')}

        Skills:
        {", ".join(doc.get('skills', []))}

        Technologies:
        {", ".join(doc.get('technologies', []))}

        Frameworks:
        {", ".join(doc.get('frameworks', []))}

        LLM Models:
        {", ".join(doc.get('llm_models', []))}

        Vector Databases:
        {", ".join(doc.get('vector_db', []))}

        Cloud:
        {", ".join(doc.get('cloud', []))}

        Keywords:
        {", ".join(doc.get('keywords', []))}

        Impact:
        {", ".join(doc.get('impact', []))}

        Description:

        {doc.get('text', '')}

        """

    def compute_skill_overlap(
            self,
            query,
            doc
    ):

        query_terms = set(

            word.lower()

            for word in query.split()

        )

        project_terms = set()

        project_terms.update(

            skill.lower()

            for skill in doc.get(
                "skills",
                []
            )

        )

        project_terms.update(

            tech.lower()

            for tech in doc.get(
                "technologies",
                []
            )

        )

        project_terms.update(

            framework.lower()

            for framework in doc.get(
                "frameworks",
                []
            )

        )

        project_terms.update(

            keyword.lower()

            for keyword in doc.get(
                "keywords",
                []
            )

        )

        overlap = len(

            query_terms &
            project_terms

        )

        return overlap

    def rerank(
            self,
            query,
            docs
    ):

        for doc in docs:

            overlap_score = (

                self.compute_skill_overlap(
                    query,
                    doc
                )

                /

                max(
                    1,
                    len(
                        doc.get(
                            "skills",
                            []
                        )
                    )
                )

            )

            importance_score = (

                doc.get(
                    "importance",
                    5
                )

                / 10

            )

            doc["final_score"] = (

                0.7 *
                doc["vector_score"]

                +

                0.2 *
                overlap_score

                +

                0.1 *
                importance_score

            )

        docs.sort(

            key=lambda x:

            x["final_score"],

            reverse=True

        )

        return docs

    def retrieve(
            self,
            query,
            k=5
    ):

        q_embedding = (

            self.embedder.embed_texts(
                [query]
            )[0]

        )

        candidate_docs = (

            self.faiss_db.search_with_scores(
                q_embedding,
                k=20
            )

        )

        ranked_docs = (

            self.rerank(
                query,
                candidate_docs
            )

        )

        return ranked_docs[:k]
