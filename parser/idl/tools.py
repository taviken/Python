from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import BailErrorStrategy, ParseCancellationException
from .generated.IDLLexer import IDLLexer
from .generated.IDLParser import IDLParser
from .python_listener import PythonListener


class IdlParsingError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class IdlErrorListener(ErrorListener):
    def __init__(self):
        self.errors = []

    def syntaxError(
        self, recognizer, offendingSymbol, line, charPositionInLine, msg, e
    ):
        # Collect error details
        error_details = {
            "line": line,
            "charPositionInLine": charPositionInLine,
            "msg": msg,
            "offendingSymbol": offendingSymbol,
        }
        self.errors.append(error_details)


def parseit(string: str):
    input_stream = InputStream(string)
    lexer = IDLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = IDLParser(token_stream)

    error_listener = IdlErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    parser._errHandler = BailErrorStrategy()

    try:
        tree = parser.specification()
    except ParseCancellationException:
        errors = [err for err in error_listener.errors if error_listener.errors]
        msg = f"Error in parsing: {errors}"
        raise IdlParsingError(msg)

    walker = ParseTreeWalker()
    listener = PythonListener()

    walker.walk(listener, tree)

    return listener.root


__all__ = [
    "IdlParsingError",
    "parseit",
]
