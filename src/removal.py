#!/usr/bin/env python3

import re
import string

def remove_punctuation(text):
    text = "".join([i for i in text if i not in string.punctuation])
    return text

def remove_urls(text):
    return re.sub(r'https?://\S+|www\.\S+', "", text)
