#!/usr/bin/env python3

import tests.pathmagic
from src.removal import remove_urls


def test_remove_urls():
    text = "https://t.co/FI3WNCV36e http://t.co/FI3WNCV36e :/"
    result = remove_urls(text)
    assert result == "  :/"
