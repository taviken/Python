import pytest
from peg_parser import Lexer, Token, Lexicon

lexicon = Lexicon(
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
        "LeftBrace": "{",
        "RightBrace": "}",
        "LeftBracket": r"\[",
        "RightBracket": r"\]",
        "ForwardSlash": r"/",
        "BackSlash": r"\\",
        "Quote": r"\"",
        "Start": r"\*",
    },
    rules={
        "whitespace": " |\t",
        "alpha": "[A-Za-z_]+",
        "numeric": "[0-9]+",
    },
)

source = [
    " module test12345 { ",
    "\tunsigned long var = 42;",
    "};",
]


def test_lexer():
    lexer = Lexer(source, lexicon)

    actual_tokens = lexer.tokens
    expected_tokens = [
        Token(text=" ", kind="whitespace", lineno=0, span=(0, 1)),
        Token(text="module", kind="module", lineno=0, span=(1, 7)),
        Token(text=" ", kind="whitespace", lineno=0, span=(7, 8)),
        Token(text="test", kind="alpha", lineno=0, span=(8, 12)),
        Token(text="12345", kind="numeric", lineno=0, span=(12, 17)),
        Token(text=" ", kind="whitespace", lineno=0, span=(17, 18)),
        Token(text="{", kind="LeftBrace", lineno=0, span=(18, 19)),
        Token(text=" ", kind="whitespace", lineno=0, span=(19, 20)),
        Token(text="\t", kind="whitespace", lineno=1, span=(0, 1)),
        Token(text="unsigned", kind="unsigned", lineno=1, span=(1, 9)),
        Token(text=" ", kind="whitespace", lineno=1, span=(9, 10)),
        Token(text="long", kind="long", lineno=1, span=(10, 14)),
        Token(text=" ", kind="whitespace", lineno=1, span=(14, 15)),
        Token(text="var", kind="alpha", lineno=1, span=(15, 18)),
        Token(text=" ", kind="whitespace", lineno=1, span=(18, 19)),
        Token(text="=", kind="EQ", lineno=1, span=(19, 20)),
        Token(text=" ", kind="whitespace", lineno=1, span=(20, 21)),
        Token(text="42", kind="numeric", lineno=1, span=(21, 23)),
        Token(text="}", kind="RightBrace", lineno=2, span=(0, 1)),
    ]

    assert expected_tokens == actual_tokens
