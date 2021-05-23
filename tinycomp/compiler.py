import lexing
import parser
import sys

def main():
    print("Tinycomp")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input_ = inputFile.read()

        # Initialize the lexer and parser.
    lexer = lexing.Lexer(input)
    parser_ = parser.Parser(lexer)

    parser.program()  # Start the parser.
    print("Parsing completed.")

if __name__ == '__main__':
    main()