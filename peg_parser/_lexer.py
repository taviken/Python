from typing import List, Union, Optional
from _lexicon import Lexicon
from pathlib import Path
import re
import io
from sre_parse import error as sre_pare_error
from ._tokens import Token, TokenSet


class LexicalError(Exception):
    pass


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
            pos = 0
            while match := self._pattern.search(line, pos):
                if match:
                    start, end = match.span()
                    if pos < start:
                        self._make_unknown_token(line, lineno, pos, start)
                    self._make_token(match, lineno, lexicon)
                    pos = end

    def _make_unknown_token(self, line, lineno, begin, end) -> None:
        token = Token(line[begin:end], "UNKNOWN", lineno, (begin, end))
        self._tokens.append(token)

    def _make_token(self, match, lineno, lexicon) -> None:
        text, kind = self._get_data_from_group(match)
        if text in lexicon.keywords:
            kind = "KEYWORD"
        token = Token(text, kind, lineno, match.span())
        self._tokens.append(token)

    def _get_data_from_group(self, match):
        return [(v, k) for k, v in match.groupdict().items() if v][0]

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
            "imagnumber",
            group(r"[0-9](?:_?[0-9])*[jJ]", group(Pointfloat, Expfloat) + r"[jJ]"),
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

        operators = group(*map(re.escape, sorted(lexicon.operators, reverse=True)))
        operators = named_group("operators", operators)

        parts = (
            comment,
            Whitespace,
            Imagnumber,
            Floatnumber,
            Hexnumber,
            Binnumber,
            Octnumber,
            Decnumber,
            operators,
            Name,
            String,
        )
        _parts = filter(None, parts)
        for part in _parts:
            try:
                _compile(part)
            except sre_pare_error:
                msg = f"Failed to compile pattern: {part}"
                raise LexicalError(msg)

        pattern = _compile("|".join(tuple(parts)))
        return pattern
