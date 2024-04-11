import re
import re._parser as _parser
import re._compiler as _compiler
from re import RegexFlag
from re._constants import BRANCH, SUBPATTERN

OPERATOR = "OPERATOR"
KEYWORD = "KEYWORD"
NUMERIC = "Numeric"
ALPHA = "alpha"
END_STMNT = "END_STMNT"
WHITE_SPACE = "WHITE_SPACE"


def operator(scanner, text):
    return OPERATOR, text


def keyword(scanner, text):
    return KEYWORD, text


def numeric(scaner, text):
    return NUMERIC, text


def alpha(scanner, text):
    return ALPHA, text


def end_stmnt(scanner, text):
    return END_STMNT, text


def white_space(scanner, text):
    return WHITE_SPACE, text


class Scanner:
    def __init__(self, lexicon, flags=0):

        if isinstance(flags, RegexFlag):
            flags = flags.value
        self.lexicon = lexicon
        # combine phrases into a compound pattern
        phrases = []
        state = _parser.State()
        state.flags = flags
        for phrase, action in lexicon:
            gid = state.opengroup()
            phrases.append(
                _parser.SubPattern(
                    state,
                    [
                        (SUBPATTERN, (gid, 0, 0, _parser.parse(phrase, flags))),
                    ],
                )
            )
            state.closegroup(gid, phrases[-1])
        phrases = _parser.SubPattern(state, [(BRANCH, (None, phrases))])
        self.scanner = _compiler.compile(phrases)

    def scan(self, string):
        result = []
        append = result.append
        match = self.scanner.scanner(string).match
        i = 0
        while True:
            m = match()
            if not m:
                break
            j = m.end()
            if i == j:
                break
            action = self.lexicon[m.lastindex - 1][1]
            if callable(action):
                self.match = m
                action = action(self, m.group())
            if action is not None:
                append(action)
            i = j
        return result, string[i:]


# scanner = re.Scanner(
scanner = Scanner(
    [
        (r"int|float|string|const", keyword),
        (r"[a-zA-Z_]+", alpha),
        (r"[\+|\-|\\|\*|\=]", operator),
        (r"[0-9]+(\.[0-9]+)?", numeric),
        (r";", end_stmnt),
        (r"\s+", white_space),
    ]
)
