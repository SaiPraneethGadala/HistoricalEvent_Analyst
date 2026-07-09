from pathlib import Path
from typing import List, Dict


class DocumentLoader:
    """
    Loads all .txt files from data/raw/
    """

    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def load_documents(self) -> List[Dict]:

        documents = []

        for file in sorted(self.data_path.glob("*.txt")):

            text = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            documents.append(
                {
                    "text": text,
                    "title": file.stem,
                    "filename": file.name,
                    "source_type": "historical_notes"
                }
            )

        print(f"Loaded {len(documents)} documents")

        return documents