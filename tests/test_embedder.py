import os

from src.embedding.embedder import GeminiEmbedder


def test_embedding_dimension():

    if os.getenv("GEMINI_API_KEY") is None:

        return

    embedder = GeminiEmbedder()

    vector = embedder.embed(

        "World War I"

    )

    assert isinstance(vector, list)

    assert len(vector) > 0