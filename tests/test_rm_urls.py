"""Tests URL removal."""

from textools.removal import remove_urls


def test_remove_urls() -> None:
    """Test URL removal."""
    text: str = "https://localhost.foo http://localhost.foo :/"
    result: str = remove_urls(text)

    assert result == "  :/"
