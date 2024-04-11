import re

OPERATOR = "OPERATOR"
KEYWORD = "KEYWORD"
NUMERIC = "Numeric"
ALPHA = "alpha"
END_STMNT = "END_STMNT"
WHITE_SPACE = "WHITE_SPACE"


def operator(scanner, text):
    return OPERATOR, text


def keyword(scanner, text):
    return KEYWORD, text


def numeric(scaner, text):
    return NUMERIC, text


def alpha(scanner, text):
    return ALPHA, text


def end_stmnt(scanner, text):
    return END_STMNT, text


def white_space(scanner, text):
    return WHITE_SPACE, text


scanner = re.Scanner(
    [
        (r"int|float|string|const", keyword),
        (r"[a-zA-Z_]+", alpha),
        (r"[\+|\-|\\|\*|\=]", operator),
        (r"[0-9]+(\.[0-9]+)?", numeric),
        (r";", end_stmnt),
        (r"\s+", white_space),
    ]
)
