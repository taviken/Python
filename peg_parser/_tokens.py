from collections import namedtuple
from typing import List, Iterator, Optional

Token = namedtuple("Token", ["text", "kind", "lineno", "span"])


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
