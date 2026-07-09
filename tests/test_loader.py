import tempfile
from pathlib import Path

from src.ingestion.loader import DocumentLoader


def test_document_loader():

    with tempfile.TemporaryDirectory() as tmp:

        file = Path(tmp) / "chapter1.txt"

        file.write_text(
            "World War I began in 1914.",
            encoding="utf-8"
        )

        loader = DocumentLoader(tmp)

        docs = loader.load_documents()

        assert len(docs) == 1

        assert docs[0]["title"] == "chapter1"

        assert "1914" in docs[0]["text"]