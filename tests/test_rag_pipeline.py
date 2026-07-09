from src.generation.gemini_chain import GeminiRAG


def test_complete_pipeline():

    rag = GeminiRAG()

    response = rag.ask(

        "Explain the assassination of Franz Ferdinand."

    )

    assert "answer" in response

    assert "documents" in response

    assert isinstance(

        response["documents"],

        list

    )