"""List of emojis, emoticons and dongers."""

from typing import Dict, List

from emot.emo_unicode import EMOTICONS_EMO

__all__: List[str] = ["EMOTICONS_EXPAND", "DONGER_EMO"]

EMOTICONS_EXPAND: Dict[str, str] = EMOTICONS_EMO

EMOTICONS_EXPAND.update(
    {
        "8‑)": "Happy face with glasses",
        "8)": "Happy face with glasses",
        "xD": "Laughing, big grin or laugh",
        ":‑D": "Laughing, big grin or laugh",
        ":D": "Laughing, big grin or laugh",
        "X‑D": "Laughing, big grin or laugh",
        "XD": "Laughing, big grin or laugh",
        "=D": "Laughing, big grin or laugh",
        "=3": "Laughing, big grin or laugh",
    }
)

DONGER_EMO: Dict[str, str] = {
    "ᕕ( ՞ ᗜ ՞ )ᕗ": "happy",
    "☆*:. o(≧▽≦)o .:*☆": "happy",
    "(⊙ᗜ⊙)": "happy",
    "╰(◕ᗜ◕)╯": "happy",
    "╰( ◕ ᗜ ◕ )╯": "happy",
    "ლ(ಥ Д ಥ )ლ": "sad",
    "(-_-｡)": "sad",
}
