"""Test punctuation removal."""

from textools.removal import remove_punctuation


def test_remove_punctuation() -> None:
    """Test punctuation removal."""
    text: str = "!#$%&'\"()*+,-./:;?@[]^_`{|}~\\"
    result: str = remove_punctuation(text)

    assert result == ""
