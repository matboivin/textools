#!/usr/bin/env python3

import re


def remove_urls(text):
    return re.sub(r'https?://\S+|www\.\S+', "", text)
