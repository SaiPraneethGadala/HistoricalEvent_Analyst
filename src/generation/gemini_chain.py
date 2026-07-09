import os

import google.generativeai as genai

from dotenv import load_dotenv

from src.generation.prompt import SYSTEM_PROMPT

from src.retrieval.retriever import Retriever


load_dotenv()


class GeminiRAG:

    def __init__(self):

        genai.configure(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

        self.retriever = Retriever()

    def ask(self, question):

        context, docs = self.retriever.get_context(question)

        prompt = f"""

{SYSTEM_PROMPT}

Retrieved Context

{context}

User Question

{question}

"""

        response = self.model.generate_content(
            prompt
        )

        return {

            "answer": response.text,

            "documents": docs

        }