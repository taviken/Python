from .generated.IDLLexer import IDLLexer
from .generated.IDLParser import IDLParser


from .python_idl_listener import PythonIdlListener
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from antlr4.error.ErrorStrategy import BailErrorStrategy, ParseCancellationException
from antlr4.error.ErrorListener import ErrorListener

import sys


class ParseError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class CustomErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(
        self, recognizer, offendingSymbol, line, charPositionInLine, msg, e
    ):
        error_msg = f"line {line}:{charPositionInLine} {msg}"
        self.errors.append(error_msg)


class MyErrorStrategy(BailErrorStrategy):
    def recover(self, recognizer, e):
        recognizer._errHandler.reportError(recognizer, e)
        super().recover(recognizer, e)


def parseit(string):
    error = CustomErrorListener()
    lexer = IDLLexer(InputStream(string))
    stream = CommonTokenStream(lexer)
    parser = IDLParser(stream)

    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(error)
    parser.addErrorListener(error)
    parser._errHandler = MyErrorStrategy()

    try:
        tree = parser.specification()
    except ParseCancellationException as e:
        lines = [err for err in error.errors if error.errors]
        msg = f"Parseing error: {lines}"
        raise ParseError(msg)

    walker = ParseTreeWalker()
    listener = PythonIdlListener()
    walker.walk(listener, tree)

    return listener.root_obj


__all__ = [
    "parseit",
]
