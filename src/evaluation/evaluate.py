from src.retrieval.retriever import Retriever


class Evaluator:

    def __init__(self):

        self.retriever = Retriever()

    def evaluate_retrieval(

        self,

        questions

    ):

        results = []

        for question in questions:

            docs = self.retriever.retrieve(question)

            results.append({

                "question": question,

                "retrieved_chunks": len(docs),

                "chapters": [

                    d["metadata"]["chapter"]

                    for d in docs

                ]

            })

        return results


if __name__ == "__main__":

    sample_questions = [

        "Why did World War I start?",

        "What happened at Verdun?",

        "Who was Gavrilo Princip?",

        "Explain the Schlieffen Plan.",

        "What was the Battle of the Somme?"

    ]

    evaluator = Evaluator()

    results = evaluator.evaluate_retrieval(

        sample_questions

    )

    for r in results:

        print("=" * 60)

        print("Question")

        print(r["question"])

        print()

        print("Retrieved Chapters")

        for c in r["chapters"]:

            print("-", c)