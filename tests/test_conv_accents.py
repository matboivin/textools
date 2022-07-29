"""Test accent conversion."""

from textools.conversion import convert_accents


def test_convert_accents() -> None:
    """Test accent conversion."""
    text: str = "àéèôù"
    result: str = convert_accents(text)

    assert result == "aeeou"
