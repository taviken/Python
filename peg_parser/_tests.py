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
        Token(text=" ", kind=" ", lineno=0, span=(0, 1)),
        Token(text="module", kind="module", lineno=0, span=(1, 7)),
        Token(text=" ", kind=" ", lineno=0, span=(7, 8)),
        Token(text="test12345", kind="test12345", lineno=0, span=(8, 17)),
        Token(text=" ", kind=" ", lineno=0, span=(17, 18)),
        Token(text="{", kind="UNKNOWN", lineno=0, span=(18, 19)),
        Token(text=" ", kind=" ", lineno=0, span=(19, 20)),
        Token(text="\t", kind="\t", lineno=1, span=(0, 1)),
        Token(text="unsigned", kind="unsigned", lineno=1, span=(1, 9)),
        Token(text=" ", kind=" ", lineno=1, span=(9, 10)),
        Token(text="long", kind="long", lineno=1, span=(10, 14)),
        Token(text=" ", kind=" ", lineno=1, span=(14, 15)),
        Token(text="var", kind="var", lineno=1, span=(15, 18)),
        Token(text=" ", kind=" ", lineno=1, span=(18, 19)),
        Token(text="=", kind="UNKNOWN", lineno=1, span=(19, 20)),
        Token(text=" ", kind=" ", lineno=1, span=(20, 21)),
        Token(text="42", kind="42", lineno=1, span=(21, 23)),
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
