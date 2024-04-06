import re
from typing import List, Dict, Set, Iterator, Tuple
from collections import namedtuple

Token = namedtuple("Token", ["text", "kind", "lineno", "span"])

keywords = [
    "long",
    "short",
    "unsigned",
    "module",
]

symbols = {
    "EQ": "=",
    "Plus": "\+",
    "Minus": "-",
    "LeftBrace": "{",
    "RightBrace": "}",
    "LeftBracket": "[",
    "RightBracket": "]",
    "ForwardSlash": "/",
    "BackSlash": "\\",
    "Quote": '"',
}

rules = {
    "whitespace": " |\t",
    "alpha": "[A-Za-z_]+",
    "numeric": "[0-9]+",
}


class Lexer:
    def __init__(
        self,
        source: List[str],
        rules: List[Tuple[str, str]],
        keywords: List[str],
        symbols: List[Tuple[str, str]],
    ):
        self._source = source.copy()
        self.rules = dict()
        self.keywords = dict()
        self.symbols = dict()
        self._process_keywords(keywords=keywords)
        self._process_rules(rules=rules)
        self._process_symbols(symbols=symbols)
        self._tokens = []

        parts = []
        parts.extend(self.symbols.values())
        parts.extend(self.keywords.values())
        parts.extend(self.rules.values())
        self._lexing_pattern = re.compile("|".join(parts))

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    def _process_symbols(self, symbols):
        for kind, symbol in symbols.items():
            pattern = f"(?P<{kind}>{symbol})"
            self.symbols[kind] = pattern

    def _process_keywords(self, keywords):
        for word in keywords:
            pattern = f"(?P<{word}>{word})"
            self.keywords[word] = pattern

    def _process_rules(self, rules):
        for word, pattern in rules.items():
            group_pattern = f"(?P<{word}>{pattern})"
            self.rules[word] = group_pattern

    def run(self):
        for lineno, line in enumerate(self._source):
            regex_match = True
            current_position = 0
            while regex_match is not None:
                regex_match = self._lexing_pattern.search(line, current_position)
                if regex_match is not None:
                    current_position = regex_match.end()
                    self._make_token(regex_match, lineno)

    def _make_token(self, match, lineno):
        text, kind = [
            (text, kind) for kind, text in match.groupdict().items() if text is not None
        ].pop()
        token = Token(text=text, kind=kind, lineno=lineno, span=match.span())
        self._tokens.append(token)
