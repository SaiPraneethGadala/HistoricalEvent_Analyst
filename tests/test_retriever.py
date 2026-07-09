from src.retrieval.retriever import Retriever


def test_retriever():

    retriever = Retriever()

    docs = retriever.retrieve(

        "Why did World War I start?"

    )

    assert isinstance(docs, list)

    assert len(docs) > 0