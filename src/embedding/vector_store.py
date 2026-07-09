import pickle
from pathlib import Path

import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.index = None

        self.metadata = []

    def build_index(

        self,

        chunks,

        embedder

    ):

        vectors = []

        metadata = []

        print("Generating Embeddings...")

        for chunk in chunks:

            vector = embedder.embed(

                chunk["text"]

            )

            vectors.append(vector)

            metadata.append(chunk)

        vectors = np.array(

            vectors,

            dtype=np.float32

        )

        dimension = vectors.shape[1]

        self.index = faiss.IndexFlatL2(

            dimension

        )

        self.index.add(vectors)

        self.metadata = metadata

        print("FAISS Index Built")

    def save(

        self,

        folder="data/vectorstore"

    ):

        folder = Path(folder)

        folder.mkdir(

            parents=True,

            exist_ok=True

        )

        faiss.write_index(

            self.index,

            str(folder / "faiss.index")

        )

        with open(

            folder / "metadata.pkl",

            "wb"

        ) as f:

            pickle.dump(

                self.metadata,

                f
            )

        print("Vector Store Saved")

    def load(

        self,

        folder="data/vectorstore"

    ):

        folder = Path(folder)

        self.index = faiss.read_index(

            str(folder / "faiss.index")

        )

        with open(

            folder / "metadata.pkl",

            "rb"

        ) as f:

            self.metadata = pickle.load(f)

        print("Vector Store Loaded")

    def similarity_search(

        self,

        query,

        embedder,

        k=5

    ):

        query_vector = np.array(

            [embedder.embed_query(query)],

            dtype=np.float32

        )

        distances, indices = self.index.search(

            query_vector,

            k
        )

        results = []

        for idx in indices[0]:

            results.append(

                self.metadata[idx]

            )

        return results