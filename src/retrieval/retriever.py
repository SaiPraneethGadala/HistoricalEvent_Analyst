from src.embedding.embedder import GeminiEmbedder
from src.embedding.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedder = GeminiEmbedder()

        self.store = VectorStore()

        self.store.load()

    def retrieve(self, query: str, top_k: int = 5):

        results = self.store.similarity_search(
            query=query,
            embedder=self.embedder,
            k=top_k
        )

        return results

    def get_context(self, query: str, top_k: int = 5):

        documents = self.retrieve(query, top_k)

        context = ""

        for i, doc in enumerate(documents, start=1):

            metadata = doc["metadata"]

            context += f"""
========================
Source {i}

Chapter : {metadata["chapter"]}

File : {metadata["filename"]}

Chunk : {metadata["chunk_id"]}

Content:
{doc["text"]}

"""

        return context, documents