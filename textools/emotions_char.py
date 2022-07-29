"""List of emojis, emoticons and dongers."""

from typing import Dict, List
from emot.emo_unicode import EMOTICONS_EMO

__all__: List[str] = ["EMOTICONS_EXPAND", "DONGER_EMO"]

EMOTICONS_EXPAND: Dict[str, str] = EMOTICONS_EMO

EMOTICONS_EXPAND.update({
    u"8‑)": "Happy face with glasses",
    u"8)": "Happy face with glasses",
    u"xD": "Laughing, big grin or laugh",
    u":‑D": "Laughing, big grin or laugh",
    u":D": "Laughing, big grin or laugh",
    u"X‑D": "Laughing, big grin or laugh",
    u"XD": "Laughing, big grin or laugh",
    u"=D": "Laughing, big grin or laugh",
    u"=3": "Laughing, big grin or laugh"
})

DONGER_EMO: Dict[str, str] = {
    u"ᕕ( ՞ ᗜ ՞ )ᕗ": "happy",
    u"☆*:. o(≧▽≦)o .:*☆": "happy",
    u"(⊙ᗜ⊙)": "happy",
    u"╰(◕ᗜ◕)╯": "happy",
    u"╰( ◕ ᗜ ◕ )╯": "happy",
    u"ლ(ಥ Д ಥ )ლ": "sad",
    u"(-_-｡)": "sad"
}
