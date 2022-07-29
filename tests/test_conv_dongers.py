"""Test dongers conversion."""

from textools.conversion import convert_dongers


def test_convert_dongers() -> None:
    """Test dongers conversion."""
    text: str = "ᕕ( ՞ ᗜ ՞ )ᕗ ╰(◕ᗜ◕)╯ (-_-｡)"
    result: str = convert_dongers(text)

    assert result == "happy happy sad"
