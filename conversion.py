#!/usr/bin/env python3

import unicodedata
from emot.emo_unicode import EMOTICONS_EMO as EMOTICONS
from emot.emo_unicode import UNICODE_EMOJI as EMOJIS


def convert_emoticons(text):
    for emot in EMOTICONS:
        if emot == ":/" and text.find("://") == -1:
            text = text.replace(emot, "_".join(EMOTICONS[emot].replace(",","").replace(":","").split()))
    return text


def convert_emojis(text):
    for emoj in EMOJIS:
        text = text.replace(emoj, "_".join(EMOJIS[emoj].replace(",","").replace(":","").split()))
    return text


def convert_accents(text):
    return ''.join((c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'))
