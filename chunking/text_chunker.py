from pydoc import text


class TextChunker:
    """A class for chunking text into smaller segments based on a specified chunk size and overlap."""
    def __init__(self, chunk_size=500, overlap=100):
        """
        Initializes the TextChunker with a specified chunk size and overlap.

        :param chunk_size: The maximum number of characters in each chunk.
        :param overlap: The number of characters to overlap between chunks.
        """
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text:str):
        print("Inside chunk()")
        print("Length:", len(text))
        print("Chunk size:", self.chunk_size)
        print("Overlap:", self.overlap)
        chunks = []
        start = 0
        while start < len(text):
            print("Start:", start)
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)

            start += self.chunk_size - self.overlap
        return chunks
