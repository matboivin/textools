"""Test stopwords removal."""

from typing import List
from nltk.tokenize import word_tokenize
import pytest

from textools.removal import remove_stopwords

LANGUAGE: str = "French"
TEXT: str = """Wikipédia est un projet d’encyclopédie collective en ligne,
universelle, multilingue et fonctionnant sur le principe du wiki. Ce projet
vise à offrir un contenu librement réutilisable, objectif et vérifiable, que
chacun peut modifier et améliorer."""
TOKENS: List[str] = word_tokenize(TEXT, LANGUAGE)
EXPECTED: List[str] = [
    "Wikipédia", "projet", "’", "encyclopédie", "collective", "ligne", ",",
    "universelle", ",", "multilingue", "fonctionnant", "principe", "wiki", ".",
    "projet", "vise", "offrir", "contenu", "librement", "réutilisable", ",",
    "objectif", "vérifiable", ",", "chacun", "peut", "modifier", "améliorer",
    "."
]


def test_remove_stopwords_err() -> None:
    """Test stopwords removal error.

    Raises
    ------
    ValueError
        If language is not handled by NLTK.

    """
    with pytest.raises(ValueError):
        remove_stopwords("français", TOKENS)


def test_remove_stopwords() -> None:
    """Test stopwords removal."""
    result: List[str] = remove_stopwords(LANGUAGE, TOKENS)

    assert result == EXPECTED
