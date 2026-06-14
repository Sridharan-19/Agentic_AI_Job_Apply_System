import faiss

class JobFaissManager:

    def __init__(
            self,
            dim
    ):

        self.index = faiss.IndexFlatIP(
            dim
        )

    def add_embeddings(
            self,
            embeddings
    ):

        self.index.add(
            embeddings
        )

    def search(
            self,
            query_embedding,
            k=20
    ):

        scores, indices = self.index.search(

            query_embedding.reshape(
                1,
                -1
            ),

            k

        )

        return scores[0], indices[0]