import pytest
from peg_parser import Lexer, Token, Lexicon, GrammarParser, Rule, default_lexicon

ENDMARKER = "ENDMARKER"
STRING = "STRING"
NAME = "NAME"
NEWLINE = "NEWLINE"

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

rules = {
    "whitespace": " |\t",
    "alpha": "[A-Za-z_]+",
    "numeric": "[0-9]+",
}


def test_lexer():
    default_lexicon.keywords = (
        [
            "long",
            "short",
            "unsigned",
            "module",
        ],
    )

    source = [
        " module test12345 { ~",
        "\tunsigned long var = 42;",
        "};",
    ]
    lexer = Lexer(source, default_lexicon)

    actual_tokens = lexer.tokens
    expected_tokens = [
        Token(text=" ", kind="INDENT", category="INDENT", lineno=1, span=(0, 1)),
        Token(text="module", kind="MODULE", category="NAME", lineno=1, span=(1, 7)),
        Token(text="test12345", kind="NAME", category="NAME", lineno=1, span=(8, 17)),
        Token(text="{", kind="LBRACE", category="OP", lineno=1, span=(18, 19)),
        Token(text="~", kind="TILDE", category="OP", lineno=1, span=(20, 21)),
        Token(
            text="unsigned", kind="UNSIGNED", category="NAME", lineno=1, span=(22, 30)
        ),
        Token(text="long", kind="LONG", category="NAME", lineno=1, span=(31, 35)),
        Token(text="var", kind="NAME", category="NAME", lineno=1, span=(36, 39)),
        Token(text="=", kind="EQUAL", category="OP", lineno=1, span=(40, 41)),
        Token(text="42", kind="NUMBER", category="NUMBER", lineno=1, span=(42, 44)),
        Token(text=";", kind="SEMI", category="OP", lineno=1, span=(44, 45)),
        Token(text="}", kind="RBRACE", category="OP", lineno=1, span=(45, 46)),
        Token(text=";", kind="SEMI", category="OP", lineno=1, span=(46, 47)),
        Token(text="", kind="NEWLINE", category="NEWLINE", lineno=1, span=(47, 48)),
        Token(text="", kind="DEDENT", category="DEDENT", lineno=2, span=(0, 0)),
        Token(text="", kind="ENDMARKER", category="ENDMARKER", lineno=2, span=(0, 0)),
    ]

    assert expected_tokens == actual_tokens


@pytest.mark.skip
def test_parser():
    lexicon = Lexicon(
        keywords=[
            ENDMARKER,
            STRING,
            NAME,
            NEWLINE,
        ],
        rules=rules,
    )
    program = [
        "stmt: asmt | expr\n",
        "asmt: NAME '=' expr\n",
        "expr: NAME\n",
    ]
    lexer = Lexer.from_str(program, lexicon)
    parser = GrammarParser(lexer)
    _rules = parser.grammar()
    assert _rules is [
        Rule("stmt", [["asmt"], ["expr"]]),
        Rule("asmt", [["NAME", "'='", "expr"]]),
        Rule("expr", [["NAME"]]),
    ]
