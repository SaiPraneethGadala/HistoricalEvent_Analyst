"""
Text Cleaner
Historical Event Analyst
"""

import re
from typing import List, Dict


class TextCleaner:
    """
    Cleans raw documents before chunking.
    """

    def __init__(self):
        pass

    @staticmethod
    def clean(text: str) -> str:
        """
        Clean a single document.
        """

        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Remove URLs
        text = re.sub(r"http\S+|www\.\S+", "", text)

        # Remove page numbers like "Page 12"
        text = re.sub(r"Page\s+\d+", "", text, flags=re.IGNORECASE)

        # Remove multiple blank lines
        text = re.sub(r"\n{2,}", "\n\n", text)

        # Remove multiple spaces/tabs
        text = re.sub(r"[ \t]+", " ", text)

        # Remove repeated punctuation spacing
        text = re.sub(r"\s+([.,!?;:])", r"\1", text)

        # Remove non-printable characters
        text = re.sub(r"[\x00-\x1F\x7F]", "", text)

        # Trim whitespace
        text = text.strip()

        return text

    def clean_documents(self, documents: List[Dict]) -> List[Dict]:
        """
        Clean all loaded documents.
        """

        cleaned_documents = []

        for doc in documents:

            cleaned_doc = {
                "text": self.clean(doc["text"]),
                "title": doc["title"],
                "filename": doc["filename"],
                "source_type": doc.get("source_type", "historical_notes")
            }

            cleaned_documents.append(cleaned_doc)

        print(f"Cleaned {len(cleaned_documents)} documents.")

        return cleaned_documents