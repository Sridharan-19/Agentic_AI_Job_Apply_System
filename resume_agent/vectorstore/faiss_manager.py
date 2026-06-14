import faiss
import numpy as np

class FaissManager:

    def __init__(
            self,
            dimension
    ):

        self.index = faiss.IndexFlatIP(
            dimension
        )

        self.documents = []

    def add_documents(
            self,
            documents,
            embeddings
    ):

        self.documents.extend(
            documents
        )

        self.index.add(

            np.array(
                embeddings,
                dtype=np.float32
            )

        )

    def search_with_scores(self, query_embedding, k=20):

        scores, indices = self.index.search(

            np.array(
                [query_embedding],
                dtype=np.float32
            ),
            k
        )

        results = []

        for score, idx in zip(
                scores[0],
                indices[0]
        ):

            doc = self.documents[idx].copy()

            doc["vector_score"] = float(score)

            results.append(
                doc
            )

        return results