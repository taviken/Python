import pytest
from ._lexer import scanner


def test_lexer():
    source = "const int foo = 1*2;"
    tokens, remainder = scanner.scan(source)
    expected = [
        ("KEYWORD", "const"),
        ("WHITE_SPACE", " "),
        ("KEYWORD", "int"),
        ("WHITE_SPACE", " "),
        ("alpha", "foo"),
        ("WHITE_SPACE", " "),
        ("OPERATOR", "="),
        ("WHITE_SPACE", " "),
        ("Numeric", "1"),
        ("OPERATOR", "*"),
        ("Numeric", "2"),
        ("END_STMNT", ";"),
    ]
    assert tokens == expected
