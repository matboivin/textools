#!/usr/bin/env python3

import nltk
from nltk.corpus import stopwords
import re
import string

__all__ = ["remove_punctuation", "remove_stopwords", "remove_urls"]

def remove_punctuation(text):
    text = "".join([i for i in text if i not in string.punctuation])
    return text

def remove_stopwords(language, tokens):
    if language.lower() not in stopwords.fileids():
        raise ValueError(f"remove_stopwords: language '{language}' is not available")
    ignored_words = nltk.corpus.stopwords.words(language)
    result = [token for token in tokens if token.lower() not in ignored_words]
    return result

def remove_urls(text):
    return re.sub(r'https?://\S+|www\.\S+', "", text)
