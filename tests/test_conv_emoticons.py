#!/usr/bin/env python3

import tests.pathmagic
from src.conversion import convert_emoticons


def test_convert_emoticons():
    text = ":)"
    result = convert_emoticons(text)
    assert result == "Happy_face_or_smiley"
