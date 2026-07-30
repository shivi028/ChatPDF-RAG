from sentence_transformers import SentenceTransformer

class EmbeddingsGenerator:
    """
    Converts text chunks into embedding vectors.
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        print("Loading embedding model...")
        self.model = SentenceTransformer(model_name)
        print("Model loaded successfully.")

    def generate_embeddings(self, texts):
        """
        Accepts either:
        - a single string
        - a list of strings
        - multiple chunks
        """
        embeddings = self.model.encode(texts, convert_to_numpy=True, show_progress_bar=True)

        return embeddings 

    # "all-MiniLM-L6-v2"
    # Fast
    # Free
    # Small
    # Very popular
    # Produces 384-dimensional vectors