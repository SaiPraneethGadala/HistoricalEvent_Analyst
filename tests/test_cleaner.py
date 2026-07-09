from src.ingestion.cleaner import TextCleaner


def test_clean_text():

    cleaner = TextCleaner()

    dirty = """

        Hello      World


        Page 10

        https://google.com

    """

    clean = cleaner.clean(dirty)

    assert "Page" not in clean

    assert "https://" not in clean

    assert "Hello World" in clean