#!/usr/bin/env python3

from src.conversion import convert_emoticons


def test_convert_emoticons():
    text = ":) :D 8D"
    result = convert_emoticons(text)
    assert result == "Happy_face_or_smiley Laughing_big_grin_or_laugh Laughing_big_grin_or_laugh_with_glasses"
