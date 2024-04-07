import pytest
from generic_parser import Lexer, Token

keywords = [
    "long",
    "short",
    "unsigned",
    "module",
]

symbols = {
    "EQ": "=",
    "Plus": r"\+",
    "Minus": "-",
    "LeftBrace": "{",
    "RightBrace": "}",
    "LeftBracket": "[",
    "RightBracket": "]",
    "ForwardSlash": "/",
    "BackSlash": "\\",
    "Quote": r'\"',
}

rules = {
    "whitespace": " |\t",
    "alpha": "[A-Za-z_]+",
    "numeric": "[0-9]+",
}

source = [
    " module test12345 { ",
    "\tunsigned long var = 42;",
    "};",
]


def test_lexer():
    lexer = Lexer(source, rules, keywords, symbols)
    lexer.run()
    actual_tokens = lexer.tokens
    expected_tokens = [
        Token(" ", "whitespace", 1, (0, 1)),
        Token("module", "module", 1, (1, 6)),
        Token(" ", "whitespace", 1, (6, 7)),
        Token("test", "alpha", 1, (7, 11)),
        Token("12345", "numeric", 1, (0, 1)),
        Token(" ", "whitespace", 1, (0, 1)),
        Token("{", "LeftBrace", 1, (0, 1)),
        Token(" ", "whitespace", 1, (0, 1)),
        Token("\t", "whitespace", 2, (0, 1)),
        Token("unsigned", "unsigned", 2, (0, 1)),
        Token(" ", "whitespace", 2, (0, 1)),
        Token("long", "long", 2, (0, 1)),
        Token("var", "alpha", 2, (0, 1)),
        Token(" ", "whitespace", 2, (0, 1)),
        Token("42", "numeric", 2, (0, 1)),
        Token(";", "Semicolon", 2, (0, 1)),
        Token("}", "RightBrace", 2, (0, 1)),
        Token(";", "Semicolon", 2, (0, 1)),
    ]

    assert expected_tokens == actual_tokens
