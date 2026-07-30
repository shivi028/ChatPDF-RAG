from pathlib import Path
from parser.pdf_loader import PDFLoader
from chunking.text_chunker import TextChunker
from embeddings.embedding_generator import EmbeddingsGenerator
from retrieval.similarity import SimilaritySearch
from prompts.prompt_builder import PromptBuilder
from llm.gemini_client import GeminiClient

import llm.gemini_client
print(llm.gemini_client.__file__)

def main():
    pdf_path = Path("data/julyCV.pdf")
    loader = PDFLoader(pdf_path)
    chunker = TextChunker(chunk_size=500, overlap=100)
    text = loader.load()
    # print("Length of extracted text:", len(text))
    # print(type(text))
    chunks = chunker.chunk(text)
    search = SimilaritySearch()
    prompt_builder = PromptBuilder()
    client = GeminiClient()

    embedding_generator = EmbeddingsGenerator()
    embeddings = embedding_generator.generate_embeddings(chunks)
    query = "Tell me about FlexiRecharge AI"
    query_embedding = embedding_generator.generate_embeddings(query)
    similarities = search.cosine_similarity(query_embedding, embeddings)
    top_k_indices = search.top_k(similarities, k=3)

    # print("Chunks object:", chunks)
    print(f"Total Chunks: {len(chunks)}")
    print()
    print("=" * 60)
    for i, chunk in enumerate(chunks):
        print("=" * 70)
        print(f"Chunk {i}")
        print("=" * 70)
        print(chunk)
        print()

    print(f"Embedding Shape: {embeddings.shape}")
    # print()
    # print("First Vector:")
    # print(embeddings[0][:10])
    print("Query Embedding : ", query_embedding.shape)
    # print(type(query_embedding))
    # print(query_embedding.ndim)

    print("\nTop Matching Chunks\n")
    for index in top_k_indices:
        print("=" * 60)
        print(f"Chunk {index}")
        print("=" * 60)
        print("\nSimilarity Score:", f"{similarities[index]:.4f}")
        print()
        print(chunks[index])

    context = "\n\n".join([chunks[i] for i in top_k_indices])
    
    prompt = prompt_builder.build(context=context, question=query)

    answer = client.generate(prompt)
    print("\n\nAnswer:\n")
    print(answer)
    


if __name__ == "__main__":
    main()

# from pathlib import Path

# print(Path.cwd())
# print(Path("data/julyCV.pdf").exists())