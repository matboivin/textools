#!/usr/bin/env python3

from src.removal import remove_urls


def test_remove_urls():
    text = "https://localhost http://localhost :/"
    result = remove_urls(text)
    assert result == "  :/"
