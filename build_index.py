"""
Build FAISS Index

Run:

python build_index.py
"""

from src.ingestion.loader import DocumentLoader
from src.ingestion.cleaner import TextCleaner
from src.processing.chunker import DocumentChunker
from src.embedding.embedder import GeminiEmbedder
from src.embedding.vector_store import VectorStore
from src.utils.helper import print_banner


def main():

    print_banner("Historical Event Analyst")

    # --------------------------------------------------------
    # Load Documents
    # --------------------------------------------------------

    loader = DocumentLoader("data/raw")

    documents = loader.load_documents()

    # --------------------------------------------------------
    # Clean Documents
    # --------------------------------------------------------

    cleaner = TextCleaner()

    documents = cleaner.clean_documents(documents)

    print(f"Documents Loaded : {len(documents)}")

    # --------------------------------------------------------
    # Chunk Documents
    # --------------------------------------------------------

    chunker = DocumentChunker()

    chunks = chunker.chunk_documents(documents)

    print(f"Total Chunks : {len(chunks)}")

    # --------------------------------------------------------
    # Generate Embeddings
    # --------------------------------------------------------

    embedder = GeminiEmbedder()

    # --------------------------------------------------------
    # Build Vector Store
    # --------------------------------------------------------

    store = VectorStore()

    store.build_index(

        chunks=chunks,

        embedder=embedder

    )

    store.save()

    print()

    print("=" * 70)

    print("FAISS INDEX CREATED SUCCESSFULLY")

    print("=" * 70)

    print()

    print("Saved Files")

    print("data/vectorstore/faiss.index")

    print("data/vectorstore/metadata.pkl")


if __name__ == "__main__":

    main()