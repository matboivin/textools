#!/usr/bin/env python3

import nltk
from nltk.tokenize import word_tokenize
from src.removal import remove_stopwords
import pytest

language = "French"
text = "Wikipédia est un projet d’encyclopédie collective en ligne, universelle, multilingue et fonctionnant sur le principe du wiki. Ce projet vise à offrir un contenu librement réutilisable, objectif et vérifiable, que chacun peut modifier et améliorer."
tokens = word_tokenize(text, language)
expected = ["Wikipédia", "projet", "’", "encyclopédie", "collective", "ligne", ",", "universelle", ",", "multilingue", "fonctionnant", "principe", "wiki", ".", "projet", "vise", "offrir", "contenu", "librement", "réutilisable", ",", "objectif", "vérifiable", ",", "chacun", "peut", "modifier", "améliorer", "."]

def test_remove_stopwords_err():
    with pytest.raises(ValueError):
        result = remove_stopwords("français", tokens)

def test_remove_stopwords():
    result = remove_stopwords(language, tokens)
    assert result == expected
