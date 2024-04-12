from ._lexer import Lexer, Lexicon, _default_lexicon
from dataclasses import dataclass
from typing import List, Union, Any
from functools import wraps

grammar = [
    "statement: assignment | expr | if_statement",
    "expr: expr '+' term | expr '-' term | term",
    "term: term '*' atom | term '/' atom | atom",
    "atom: NAME | NUMBER | '(' expr ')'",
    "assignment: target '=' expr",
    "target: NAME",
    "if_statement: 'if' expr ':' statement",
]

meta_grammar = [
    "grammar: rule+ ENDMARKER",
    "rule: NAME ':' alternative ('|' alternative)* NEWLINE",
    "alternative: item+",
    "item: NAME | STRING",
]


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


@dataclass
class Rule:
    name: str
    alts: List[str]


class Parser:
    def __init__(self, lexer: Lexer):
        self.tokenset = lexer.tokenset

    def expect(self, arg):
        token = self.tokenset.peek_token()
        if token.kind == arg or token.text == arg:
            return self.tokenset.get_token()
        return None


# class GrammarParser(Parser):
#     def grammar(self):
#             pos = self.mark()
#             if rule := self.rule():
#                 rules = [rule]
#                 while rule := self.rule():
#                     rules.append(rule)
#                 if self.expect(ENDMARKER):
#                     return rules    # <------------- final result
#         self.reset(pos)
#         return None
#     def rule(self):
#         pos = self.mark()
#         if name := self.expect(NAME):
#             if self.expect(":"):
#                 if alt := self.alternative():
#                     alts = [alt]
#                     apos = self.mark()
#                     while (self.expect("|")
#                            and (alt := self.alternative())):
#                         alts.append(alt)
#                         apos = self.mark()
#                     self.reset(apos)
#                     if self.expect(NEWLINE):
#                         return Rule(name.string, alts)
#         self.reset(pos)
#         return None    def alternative(self):
#         items = []
#         while item := self.item():
#             items.append(item)
#         return items    def item(self):
#         if name := self.expect(NAME):
#             return name.string
#         if string := self.expect(STRING):
#             return string.string
#         return None
