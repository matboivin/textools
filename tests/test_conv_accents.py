#!/usr/bin/env python3

from src.conversion import convert_accents


def test_convert_accents():
    text = "àéèôù"
    result = convert_accents(text)
    assert result == "aeeou"
