"""Test emojis conversion."""

from textools.conversion import convert_emojis


def test_convert_emojis() -> None:
    """Test emojis conversion."""
    text: str = "😎"
    result: str = convert_emojis(text)

    assert result == "smiling_face_with_sunglasses"
