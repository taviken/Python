from ._lexer import Lexer, Lexicon, _default_lexicon, TokenSet, Token
from dataclasses import dataclass
from typing import List, Optional, Any, Union
from functools import wraps

ENDMARKER = "ENDMARKER"
STRING = "STRING"
NAME = "NAME"
NEWLINE = "NEWLINE"


def memoize(func):
    @wraps
    def memoize_wrapper(self, *args):
        pos = self.mark()
        memo = self.memos.get(pos)
        if memo is None:
            memo = self.memos[pos] = {}
        key = (func, args)
        if key in memo:
            res, endpos = memo[key]
            self.reset(endpos)
        else:
            res = func(self, *args)
            endpos = self.mark()
            memo[key] = res, endpos
        return res

    return memoize_wrapper


@dataclass
class Node:
    type: str
    children: Union[Any, "Node"]

    def __str__(self) -> str:
        return f"{self.__class__.__name__}:{self.type}"


@dataclass
class Rule:
    name: str
    alts: List[str]


class Parser:
    def __init__(self, lexer: Lexer):
        self.tokenset: TokenSet = lexer.tokenset

    def mark(self) -> int:
        return self.tokenset.mark()

    def reset(self, position: int) -> None:
        self.tokenset.reset(position)

    def expect(self, arg) -> Optional[Token]:
        token = self.tokenset.peek_token()
        if token.kind == arg or token.text == arg:
            return self.tokenset.get_token()
        return None


class GrammarParser(Parser):

    def grammar(self):
        pos = self.mark()
        if rule := self.rule():
            rules = [rule]
            while rule := self.rule():
                rules.append(rule)
            if self.expect(ENDMARKER):
                return rules
        self.reset(pos)
        return None

    def rule(self):
        pos = self.mark()
        if name := self.expect(NAME):
            if self.expect(":"):
                if alt := self.alternative():
                    alts = [alt]
                    apos = self.mark()
                    while self.expect("|") and (alt := self.alternative()):
                        alts.append(alt)
                        apos = self.mark()
                    self.reset(apos)
                    if self.expect(NEWLINE):
                        return Rule(name.string, alts)
        self.reset(pos)
        return None

    def alternative(self):
        items = []
        while item := self.item():
            items.append(item)
        return items

    def item(self):
        if name := self.expect(NAME):
            return name.string
        if string := self.expect(STRING):
            return string.string
        return None
