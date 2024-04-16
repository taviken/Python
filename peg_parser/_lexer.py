import re
from typing import List, Dict, Union, Optional, Iterator, IO
from collections import namedtuple, deque
from dataclasses import dataclass
from pathlib import Path
from traceback import format_exc
import tokenize
import io

Token = namedtuple("Token", ["text", "kind", "category", "lineno", "span"])


@dataclass
class Lexicon:
    keywords: List[str]
    rules: Dict[str, str] = None


_default_lexicon = Lexicon(
    keywords=[
        "long",
        "short",
        "unsigned",
        "module",
    ],
    rules=None,
)

token_lookup = {
    getattr(tokenize, name): name
    for name in dir(tokenize)
    if isinstance(getattr(tokenize, name), int) and name.isupper()
}


class LexicalError(Exception):
    pass


class TokenSet:
    tokens: List[Token]

    def __init__(self, tokens: List[Token]):
        self.tokens: List[Token] = tokens.copy()
        self.current_pos: int = 0

    def get_token(self) -> Token:
        token = self.peek_token()
        self.current_pos += 1
        return token

    def reset(self, position: int) -> None:
        self.current_pos = position

    def mark(self) -> int:
        return self.current_pos

    def peek_token(self) -> Optional[Token]:
        if self.current_pos < len(self.tokens):
            return self.tokens[self.current_pos + 1]

    def __iter__(self) -> Iterator[Token]:
        yield from self.tokens

    def __reversed__(self) -> Iterator[Token]:
        yield from reversed(self.tokens)


class Lexer:
    def __init__(self, source: IO, lexicon: Lexicon, **options):
        self.lexicon = lexicon
        self._tokens = []
        self.skip_comment = options.get("skip_comment", False)

        self._process_source(source)

    @classmethod
    def from_str(
        cls, source: Union[str, list], lexicon: Lexicon, **options
    ) -> Optional["Lexer"]:
        if isinstance(source, list):
            source = "".join(source)
        io_string = io.StringIO(source)
        return cls(io_string, lexicon, **options)

    @property
    def tokenset(self) -> TokenSet:
        return TokenSet(self._tokens)

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    def _process_source(self, source: IO) -> None:
        temp = tokenize.generate_tokens(source.readline)
        self._process_tokens(temp)

    def _process_tokens(self, tokens: List[tokenize.TokenInfo]) -> None:
        for info in tokens:
            if self.skip_comment:
                if info.type in (tokenize.NL, tokenize.COMMENT):
                    continue
            if info.type == tokenize.ERRORTOKEN and info.string.isspace():
                continue
            lineno, start = info.start
            _, end = info.end
            kind = token_lookup.get(info.exact_type, "UNKNOWN")
            category = token_lookup.get(info.type, "UNKNOWN")
            text = info.string
            if category == "NAME" and text in self.lexicon.keywords:
                kind = text.upper()

            token = Token(text, kind, category, lineno, (start, end))
            self._tokens.append(token)
