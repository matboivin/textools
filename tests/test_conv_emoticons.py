"""Test emoticons conversion."""

from textools.conversion import convert_emoticons


def test_convert_emoticons() -> None:
    """Test emoticons conversion."""
    text: str = ":) :D 8D"
    result: str = convert_emoticons(text)

    assert result == (
        "Happy_face_or_smiley Laughing_big_grin_or_laugh "
        "Laughing_big_grin_or_laugh_with_glasses"
    )
