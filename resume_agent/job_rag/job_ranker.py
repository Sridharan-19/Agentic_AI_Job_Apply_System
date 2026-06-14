from resume_agent.job_rag.job_embedding_manager import (
JobEmbeddingManager
)

from resume_agent.job_rag.job_faiss_manager import (
JobFaissManager
)

class JobRanker:

    def __init__(

            self,

            jobs,

            profile_text

    ):

        self.jobs = jobs

        self.embedder = JobEmbeddingManager()

        self.profile_text = profile_text

        job_texts = [

            f"""

            {job.title}

            {job.company}

            {job.jd}

            """

            for job in jobs

        ]

        self.job_embeddings = (

            self.embedder.embed_texts(

                job_texts

            )

        )

        dim = self.job_embeddings.shape[1]

        self.faiss_db = JobFaissManager(

            dim

        )

        self.faiss_db.add_embeddings(

            self.job_embeddings

        )

    def rank(

            self,

            k=20

    ):

        profile_embedding = (

            self.embedder.embed_texts(

                [

                    self.profile_text

                ]

            )[0]

        )

        scores, indices = (

            self.faiss_db.search(

                profile_embedding,

                k

            )

        )

        results = []

        for score, idx in zip(

                scores,

                indices

        ):

            results.append(

                (

                    self.jobs[idx],

                    float(score)

                )

            )

        return results