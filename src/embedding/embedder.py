import os

import google.generativeai as genai

from dotenv import load_dotenv


load_dotenv()


class GeminiEmbedder:

    def __init__(self):

        genai.configure(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = "models/gemini-embedding-001"

    def embed(self, text):

        response = genai.embed_content(

            model=self.model,

            content=text,

            task_type="retrieval_document"
        )

        return response["embedding"]

    def embed_query(self, query):

        response = genai.embed_content(

            model=self.model,

            content=query,

            task_type="retrieval_query"
        )

        return response["embedding"]

    def embed_documents(self, chunks):

        embeddings = []

        for chunk in chunks:

            vector = self.embed(chunk["text"])

            embeddings.append(vector)

        return embeddings