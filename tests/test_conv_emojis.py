#!/usr/bin/env python3

from src.conversion import convert_emojis


def test_convert_emojis():
    text = "😎"
    result = convert_emojis(text)
    assert result == "smiling_face_with_sunglasses"
