#!/usr/bin/env python3

from src.conversion import convert_dongers

def test_convert_dongers():
    text = "ᕕ( ՞ ᗜ ՞ )ᕗ ╰(◕ᗜ◕)╯ (-_-｡)"
    result = convert_dongers(text)
    assert result == "happy happy sad"
