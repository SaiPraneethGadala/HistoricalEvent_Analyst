import tempfile

from src.embedding.embedder import GeminiEmbedder
from src.embedding.vector_store import VectorStore


def test_vector_store():

    chunks = [

        {

            "text": "World War I started in 1914.",

            "metadata": {

                "chapter": "chapter1",

                "filename": "chapter1.txt",

                "chunk_id": 0

            }

        }

    ]

    embedder = GeminiEmbedder()

    store = VectorStore()

    store.build_index(

        chunks,

        embedder

    )

    with tempfile.TemporaryDirectory() as tmp:

        store.save(tmp)

        store.load(tmp)

        assert store.index.ntotal == 1