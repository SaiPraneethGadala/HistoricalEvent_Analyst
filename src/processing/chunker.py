from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " "
            ]
        )

    def chunk_documents(self, documents):

        chunks = []

        for document in documents:

            splits = self.splitter.split_text(document["text"])

            for idx, chunk in enumerate(splits):

                chunks.append(
                    {
                        "text": chunk,
                        "metadata": {
                            "chapter": document["title"],
                            "filename": document["filename"],
                            "source_type": document["source_type"],
                            "chunk_id": idx,
                        },
                    }
                )

        print(f"Generated {len(chunks)} chunks")

        return chunks