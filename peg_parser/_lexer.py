from typing import List, Dict, Union, Optional, Iterator, IO
from collections import namedtuple
from dataclasses import dataclass
from pathlib import Path
import re
import io

Token = namedtuple("Token", ["text", "kind", "lineno", "span"])


@dataclass
class Lexicon:
    keywords: List[str]
    operators:Dict[str,str]
    comments:Dict[str,str]
    


_default_lexicon = Lexicon(
    keywords=[
        "long",
        "short",
        "unsigned",
        "module",
    ],
    operators=None,
    comments={
        "LINE_COMMENT":r"//.*$",
    }
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
    def __init__(self, source:Union[str,List], lexicon: Lexicon):
        if isinstance(source,str):
            io_str = io.StringIO(source)
            source = io_str.readlines()
        
        self._tokens = []
        self._pattern=self._super_pattern(lexicon)
        self._process_source(source,lexicon)

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

    def _process_source(self, source: List[str],lexicon:Lexicon) -> None:
        for lineno,line in enumerate(source):
            pos,max_len = 0,len(line)
            while match:=self._pattern.search(line,pos) and pos < max_len:
                if match:
                    start,end = match.span()
                    if pos < start:
                        self._make_unknown_token(line,lineno,pos,start)
                    self._make_token(match,lineno,start,end,lexicon)
                    pos = end
                else:
                    pos+=1

        

    def _super_pattern(self,lexicon:Lexicon):
        def group(*choices): return '(' + '|'.join(choices) + ')'
        def any(*choices): return group(*choices) + '*'
        def maybe(*choices): return group(*choices) + '?'
        def named_group(name:str,choices):
            return f"(?P<{name}{choices})"
        def _compile(expr):
            return re.compile(expr, re.MULTILINE|re.UNICODE)

        # Note: we use unicode matching for names ("\w") but ascii matching for
        # number literals.
        Whitespace = r'[ \f\t]*'
        Comment = r'#[^\r\n]*'
        Ignore = Whitespace + any(r'\\\r?\n' + Whitespace) + maybe(Comment)
        Name = r'\w+'

        Hexnumber = r'0[xX](?:_?[0-9a-fA-F])+'
        Binnumber = r'0[bB](?:_?[01])+'
        Octnumber = r'0[oO](?:_?[0-7])+'
        Decnumber = r'(?:0(?:_?0)*|[1-9](?:_?[0-9])*)'
        Intnumber = group(Hexnumber, Binnumber, Octnumber, Decnumber)
        Exponent = r'[eE][-+]?[0-9](?:_?[0-9])*'
        Pointfloat = group(r'[0-9](?:_?[0-9])*\.(?:[0-9](?:_?[0-9])*)?',
                        r'\.[0-9](?:_?[0-9])*') + maybe(Exponent)
        Expfloat = r'[0-9](?:_?[0-9])*' + Exponent
        Floatnumber = group(Pointfloat, Expfloat)
        Imagnumber = group(r'[0-9](?:_?[0-9])*[jJ]', Floatnumber + r'[jJ]')
        Number = group(Imagnumber, Floatnumber, Intnumber)

        # Return the empty string, plus all of the valid string prefixes.
        def _all_string_prefixes():
            # The valid string prefixes. Only contain the lower case versions,
            #  and don't contain any permutations (include 'fr', but not
            #  'rf'). The various permutations will be generated.
            _valid_string_prefixes = ['b', 'r', 'u', 'f', 'br', 'fr']
            # if we add binary f-strings, add: ['fb', 'fbr']
            result = {''}
            for prefix in _valid_string_prefixes:
                for t in _itertools.permutations(prefix):
                    # create a list with upper and lower versions of each
                    #  character
                    for u in _itertools.product(*[(c, c.upper()) for c in t]):
                        result.add(''.join(u))
            return result



        # Note that since _all_string_prefixes includes the empty string,
        #  StringPrefix can be the empty string (making it optional).
        StringPrefix = group(*_all_string_prefixes())

        # Tail end of ' string.
        Single = r"[^'\\]*(?:\\.[^'\\]*)*'"
        # Tail end of " string.
        Double = r'[^"\\]*(?:\\.[^"\\]*)*"'
        # Tail end of ''' string.
        Single3 = r"[^'\\]*(?:(?:\\.|'(?!''))[^'\\]*)*'''"
        # Tail end of """ string.
        Double3 = r'[^"\\]*(?:(?:\\.|"(?!""))[^"\\]*)*"""'
        Triple = group(StringPrefix + "'''", StringPrefix + '"""')
        # Single-line ' or " string.
        String = group(StringPrefix + r"'[^\n'\\]*(?:\\.[^\n'\\]*)*'",
                    StringPrefix + r'"[^\n"\\]*(?:\\.[^\n"\\]*)*"')

        # Sorting in reverse order puts the long operators before their prefixes.
        # Otherwise if = came before ==, == would get recognized as two instances
        # of =.
        Special = group(*map(re.escape, sorted(EXACT_TOKEN_TYPES, reverse=True)))
        Funny = group(r'\r?\n', Special)

        PlainToken = group(Number, Funny, String, Name)
        Token = Ignore + PlainToken

        # First (or only) line of ' or " string.
        ContStr = group(StringPrefix + r"'[^\n'\\]*(?:\\.[^\n'\\]*)*" +
                        group("'", r'\\\r?\n'),
                        StringPrefix + r'"[^\n"\\]*(?:\\.[^\n"\\]*)*' +
                        group('"', r'\\\r?\n'))
        PseudoExtras = group(r'\\\r?\n|\Z', Comment, Triple)
        PseudoToken = Whitespace + group(PseudoExtras, Number, Funny, ContStr, Name)

        # For a given string prefix plus quotes, endpats maps it to a regex
        #  to match the remainder of that string. _prefix can be empty, for
        #  a normal single or triple quoted string (with no prefix).
        endpats = {}
        for _prefix in _all_string_prefixes():
            endpats[_prefix + "'"] = Single
            endpats[_prefix + '"'] = Double
            endpats[_prefix + "'''"] = Single3
            endpats[_prefix + '"""'] = Double3
        del _prefix