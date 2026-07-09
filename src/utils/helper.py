import json
from pathlib import Path


def save_json(data, filename):

    filename = Path(filename)

    filename.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def load_json(filename):

    with open(
        filename,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def print_banner(title):

    print("=" * 70)

    print(title.center(70))

    print("=" * 70)


def print_sources(documents):

    print()

    print("Retrieved Sources")

    print("-" * 40)

    for doc in documents:

        meta = doc["metadata"]

        print(

            f'{meta["chapter"]} | '
            f'{meta["filename"]} | '
            f'Chunk {meta["chunk_id"]}'

        )