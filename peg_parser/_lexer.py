from typing import List, Dict, Union, Optional, Iterator
from collections import namedtuple
from dataclasses import dataclass
from pathlib import Path
import re
import io
from sre_parse import error as sre_pare_error

Token = namedtuple("Token", ["text", "kind", "lineno", "span"])


EXACT_TOKEN_TYPES = {
    "!": "EXCLAMATION",
    "!=": "NOTEQUAL",
    "%": "PERCENT",
    "%=": "PERCENTEQUAL",
    "&": "AMPER",
    "&=": "AMPEREQUAL",
    "(": "LPAR",
    ")": "RPAR",
    "*": "STAR",
    "**": "DOUBLESTAR",
    "**=": "DOUBLESTAREQUAL",
    "*=": "STAREQUAL",
    "+": "PLUS",
    "+=": "PLUSEQUAL",
    ",": "COMMA",
    "-": "MINUS",
    "-=": "MINEQUAL",
    "->": "RARROW",
    ".": "DOT",
    "...": "ELLIPSIS",
    "/": "SLASH",
    "//": "DOUBLESLASH",
    "//=": "DOUBLESLASHEQUAL",
    "/=": "SLASHEQUAL",
    ":": "COLON",
    ":=": "COLONEQUAL",
    ";": "SEMI",
    "<": "LESS",
    "<<": "LEFTSHIFT",
    "<<=": "LEFTSHIFTEQUAL",
    "<=": "LESSEQUAL",
    "=": "EQUAL",
    "==": "EQEQUAL",
    ">": "GREATER",
    ">=": "GREATEREQUAL",
    ">>": "RIGHTSHIFT",
    ">>=": "RIGHTSHIFTEQUAL",
    "@": "AT",
    "@=": "ATEQUAL",
    "[": "LSQB",
    "]": "RSQB",
    "^": "CIRCUMFLEX",
    "^=": "CIRCUMFLEXEQUAL",
    "{": "LBRACE",
    "|": "VBAR",
    "|=": "VBAREQUAL",
    "}": "RBRACE",
    "~": "TILDE",
}
_operators = {v: k for k, v in EXACT_TOKEN_TYPES.items()}


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
    },
)


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
    def __init__(self, source: Union[str, List], lexicon: Lexicon):
        if isinstance(source, str):
            io_str = io.StringIO(source)
            source = io_str.readlines()

        self._tokens = []
        self._pattern = self._super_pattern(lexicon)
        self._process_source(source, lexicon)

    @classmethod
    def from_file(
        cls, file_path: Union[str, Path], lexicon: Lexicon
    ) -> Optional["Lexer"]:
        with open(file_path, "r") as file_:

            return cls(file_.readlines(), lexicon)

    @property
    def tokenset(self) -> TokenSet:
        return TokenSet(self._tokens)

    @property
    def tokens(self) -> List[Token]:
        return self._tokens

    def _process_source(self, source: List[str], lexicon: Lexicon) -> None:
        for lineno, line in enumerate(source):
            pos, max_len = 0, len(line)
            while (match := self._pattern.search(line, pos)) and pos < max_len:
                if match:
                    start, end = match.span()
                    if pos < start:
                        self._make_unknown_token(line, lineno, pos, start)
                    self._make_token(match, lineno, lexicon)
                    pos = end
                else:
                    pos += 1

    def _make_unknown_token(self, line, lineno, begin, end) -> None:
        token = Token(line[begin:end], "UNKNOWN", lineno, (begin, end))
        self._tokens.append(token)

    def _make_token(self, match, lineno, lexicon) -> None:
        text, kind = self._get_data_from_group(match)
        if text in lexicon.keywords:
            kind = "KEYWORD"
        token = Token(match.group(), kind, lineno, match.span())
        self._tokens.append(token)

    def _get_data_from_group(self, match):
        return [(k, v) for k, v in match.groupdict() if v][0]

    def _super_pattern(self, lexicon: Lexicon):
        def group(*choices):
            return "(" + "|".join(choices) + ")"

        def any(*choices):
            return group(*choices) + "*"

        def maybe(*choices):
            return group(*choices) + "?"

        def named_group(name: str, choices):
            return f"(?P<{name}>{choices})"

        def _compile(expr):
            return re.compile(expr, re.MULTILINE | re.UNICODE)

        # Note: we use unicode matching for names ("\w") but ascii matching for
        # number literals.
        Whitespace = named_group("whitespace", r"[ |\t]+")
        Name = named_group("name", r"\w+")

        Hexnumber = named_group("hexnumber", r"0[xX](?:_?[0-9a-fA-F])+")
        Binnumber = named_group("binumber", r"0[bB](?:_?[01])+")
        Octnumber = named_group("octnumber", r"0[oO](?:_?[0-7])+")
        Decnumber = named_group("decnumber", r"(?:0(?:_?0)*|[1-9](?:_?[0-9])*)")
        Exponent = r"[eE][-+]?[0-9](?:_?[0-9])*"
        Pointfloat = group(
            r"[0-9](?:_?[0-9])*\.(?:[0-9](?:_?[0-9])*)?", r"\.[0-9](?:_?[0-9])*"
        ) + maybe(Exponent)
        Expfloat = r"[0-9](?:_?[0-9])*" + Exponent
        Floatnumber = named_group("floatnumber", group(Pointfloat, Expfloat))
        Imagnumber = named_group(
            "imagnumber", group(r"[0-9](?:_?[0-9])*[jJ]", Floatnumber + r"[jJ]")
        )

        comment = (
            named_group("COMMENT", group(*list(lexicon.comments.values())))
            if lexicon.comments
            else None
        )

        String = named_group(
            "string",
            group(r"'[^\n'\\]*(?:\\.[^\n'\\]*)*'", r'"[^\n"\\]*(?:\\.[^\n"\\]*)*"'),
        )

        parts = (
            comment,
            Whitespace,
            Imagnumber,
            Floatnumber,
            Hexnumber,
            Binnumber,
            Octnumber,
            Decnumber,
            Name,
            String,
        )
        parts = filter(None, parts)
        for part in parts:
            try:
                _compile(part)
            except sre_pare_error:
                msg = f"Failed to compile pattern: {part}"
                raise LexicalError(msg)

        return _compile("|".join(parts))
