import numpy as np


class SimilaritySearch:

    def cosine_similarity(self, query_embedding, embeddings):
        """
        Returns cosine similarity between
        query embedding and all chunk embeddings.
        """

        dot_products = np.dot(embeddings, query_embedding)

        embedding_norms = np.linalg.norm(
            embeddings,
            axis=1
        )
        # norm - distance(length of the embedding vector) (How long is this vector?)
        query_norm = np.linalg.norm(
            query_embedding
        )
        # we normalize the result
        similarities = dot_products / (
            embedding_norms * query_norm
        )

        return similarities

    def top_k(self, similarities, k=3):
        """
        Returns the indices of the top k most similar chunks.
        """
        top_k_indices = np.argsort(similarities)[-k:][::-1]
        return top_k_indices