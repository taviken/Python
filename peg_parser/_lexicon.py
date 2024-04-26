from dataclasses import dataclass
from typing import List, Dict
from _constants import _operators


@dataclass
class Lexicon:
    keywords: List[str]
    operators: Dict[str, str]
    comments: Dict[str, str]


default_lexicon = Lexicon(
    keywords=[],
    operators=_operators,
    comments={
        "LINE_COMMENT": r"//.*$",
        "PYTHON_COMMENT": r"#.*$",
    },
)
