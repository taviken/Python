import re
from typing import List, Dict, Tuple, Union
from collections import namedtuple, deque
from dataclasses import dataclass
from pathlib import Path
from traceback import format_exc

Token = namedtuple("Token", ["text", "kind", "lineno", "span"])


@dataclass
class Lexicon:
    keywords: List[str]
    symbols: Dict[str, str]
    rules: Dict[str, str]


_default_lexicon = Lexicon(
    keywords=[
        "long",
        "short",
        "unsigned",
        "module",
    ],
    symbols={
        "EQ": r"\=",
        "Plus": r"\+",
        "Minus": r"\-",
        "LeftBrace": r"\{",
        "RightBrace": r"\}",
        "LeftBracket": r"\[",
        "RightBracket": r"\]",
        "ForwardSlash": "/",
        "BackSlash": "\\",
        "Quote": '"',
    },
    rules={
        "whitespace": " |\t",
        "alpha": "[A-Za-z_]+",
        "numeric": "[0-9]+",
    },
)


class LexicalError(Exception):
    pass


class TokenSet:
    _tokens: List[Token]

    def __init__(self, tokens: List[Token]):
        self._tokens = deque(tokens)
        self._stack = deque()

    def get_token(self):
        if self._tokens:
            token = self._tokens.popleft()
            self._stack.append(token)
            return token

    def peek_token(self):
        if self._tokens:
            return self._tokens[0]


class Lexer:
    def __init__(
        self,
        source: List[str],
        lexicon: Lexicon,
    ):
        self._source = source.copy()
        self.pos = 0

        self.rules = None
        self.keywords = None
        self.symbols = None
        self._lexicon = None
        self.lexicon = lexicon
        self.parts = []
        self._process_keywords(keywords=lexicon.keywords)
        self._process_rules(rules=lexicon.rules)
        self._process_symbols(symbols=lexicon.symbols)

        self._tokens = []

        # parts.extend(self.symbols.values())
        # parts.extend(self.keywords.values())
        # parts.extend(self.rules.values())

        # pre check compilation
        for part in self.parts:
            try:
                re.compile(part)
            except Exception:
                exc = format_exc()
                msg = f"failed to compile phrase: {part}.\n"
                print(f"Traceback:\n{exc}")
                raise LexicalError(msg)

        self._lexing_pattern = re.compile("|".join(self.parts))

        self.run()

    def mark(self):
        return self.pos

    def reset(self, pos):
        self.pos = pos

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
    def manual_parameters(
        cls,
        source: List[str],
        rules: List[Tuple[str, str]],
        keywords: List[str],
        symbols: List[Tuple[str, str]],
        **options,
    ) -> "Lexer":
        lexicon = Lexicon(keywords=keywords, symbols=symbols, rules=rules)
        return cls(source, lexicon, **options)

    @classmethod
    def from_file(
        cls, filepath: Path, lexicon: Lexicon, **options
    ) -> Union["Lexer", None]:
        mode = options.get("mode", "r")
        with open(filepath, mode) as f:
            source = f.readlines()
            return cls(source=source, lexicon=lexicon, **options)

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    @property
    def tokenset(self) -> TokenSet:
        return TokenSet(self.tokens)

    def _process_symbols(self, symbols):
        for kind, symbol in symbols.items():
            pattern = f"(?P<{kind}>{symbol})"
            self.parts.append(pattern)

    def _process_keywords(self, keywords):

        for word in keywords:
            pattern = f"(?P<{word}>{word})"
            self.parts.append(pattern)

    def _process_rules(self, rules):
        for word, pattern in rules.items():
            group_pattern = f"(?P<{word}>{pattern})"
            self.parts.append(group_pattern)

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
