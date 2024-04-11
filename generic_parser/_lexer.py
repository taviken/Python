import re
from typing import List, Dict, Set, Iterator, Tuple
from collections import namedtuple
from dataclasses import dataclass
from pathlib import Path

Token = namedtuple("Token", ["text", "kind", "lineno", "span"])


@dataclass
class Lexicon:
    keywords: List[str]
    symbols: Dict[str, str]
    rules: Dict[str, str]


_default_lexicon = Lexicon(keywords=["long",                                     "short",                                     "unsigned",
                                     "module",
                                     ]

                           symbols={"EQ": "=",
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

                           rules={"whitespace": " |\t",
                                  "alpha": "[A-Za-z_]+",
                                  "numeric": "[0-9]+",
                                  }
                           )


class LexicalError(Exception):
    pass


class Lexer:
    def __init__(
        self,
        source: List[str],
        lexicon: Lexicon,
    ):
        self._source = source.copy()

        self.rules = None
        self.keywords = None
        self.symbols = None
        self._lexicon = None
        self.lexicon = lexicon
        self._process_keywords(keywords=keywords)
        self._process_rules(rules=rules)
        self._process_symbols(symbols=symbols)
        self.run()
        self._tokens = []

        parts = []
        parts.extend(self.symbols.values())
        parts.extend(self.keywords.values())
        parts.extend(self.rules.values())
        self._lexing_pattern = re.compile("|".join(parts))

    @property
    def lexicon(self) -> Lexicon:
        return self._lexicon

    @lexicon.setter
    def lexicon(self, new_lexicon: Lexicon) -> None:
        if isinstance(new_lexicon, Lexicon):
            self._lexicon = new_lexicon
            self.keywords = new_lexicon.keywords
            self.symbols = new_lexicon.symbols
            self.rules = new_lexicon.rules
        else:
            msg = f'Argument "new_lexicon" must be of Type[Lexicon],\
                  received Type[{type(new_lexicon)}]'
            raise LexicalError(msg)

    @classmethod
    def manual_parameters(cls,
                          source: List[str],
                          rules: List[Tuple[str, str]],
                          keywords: List[str],
                          symbols: List[Tuple[str, str]],
                          **options):
        lexicon = Lexicon(keywords=keywords, symbols=symbols, rules=rules)
        return cls(source, Lexicon, **options)

    @classmethod
    def from_file(cls, filepath: Path, lexicon: Lexicon, **options):
        mode = options.get('mode', 'r')
        with open(filepath, mode) as f:
            source = f.readlines()
            lexcer = cls(source=source, lexicon=lexicon, **options)

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
                regex_match = self._lexing_pattern.search(
                    line, current_position)
                if regex_match is not None:
                    current_position = regex_match.end()
                    self._make_token(regex_match, lineno)

    def _make_token(self, match, lineno):
        text, kind = [
            (text, kind) for kind, text in match.groupdict().items() if text is not None
        ].pop()
        token = Token(text=text, kind=kind, lineno=lineno, span=match.span())
        self._tokens.append(token)
