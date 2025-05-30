import fahri_lexer
import fahri_parser
import fahri_interpreter

from sys import *

#MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = fahri_lexer.BasicLexer()
    parser = fahri_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('fahri > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            fahri_interpreter.BasicExecute(tree, env)
