"""Removal helpers."""

import re
import string
from typing import List

import nltk
from nltk.corpus import stopwords

__all__: List[str] = ["remove_punctuation", "remove_stopwords", "remove_urls"]


def remove_punctuation(text: str) -> str:
    """Remove punctuation in a given text.

    Parameters
    ----------
    text : str
        A text to process.

    Returns
    -------
    str
        The text without punctuation.

    """
    return "".join([i for i in text if i not in string.punctuation])


def remove_stopwords(language: str, tokens: List[str]) -> List[str]:
    """Remove stopwords in a given text.

    Parameters
    ----------
    language : str
        The language of the words.
    tokens : list of str
        A list of words.

    Returns
    -------
    str
        The tokens list without stopwords.

    Raises
    ------
    ValueError
        If language is not handled by NLTK.

    """
    if language.lower() not in stopwords.fileids():
        raise ValueError(
            f"remove_stopwords: language '{language}' is not available")

    ignored_words: List[str] = nltk.corpus.stopwords.words(language)
    result: List[str] = [
        token for token in tokens if token.lower() not in ignored_words
    ]
    return result


def remove_urls(text: str) -> str:
    """Remove URLs in a given text.

    Parameters
    ----------
    text : str
        A text to process.

    Returns
    -------
    str
        The text without URLs.

    """
    return re.sub(r'https?://\S+|www\.\S+', "", text)
