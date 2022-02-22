#!/usr/bin/env python3

from src.removal import remove_punctuation

def test_remove_punctuation():
    text = "!#$%&'\"()*+,-./:;?@[]^_`{|}~\\"
    result = remove_punctuation(text)
    assert result == ""
