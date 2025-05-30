import fahri_lexer
import fahri_parser
import fahri_interpreter

from sys import *


lexer = fahri_lexer.BasicLexer()
parser = fahri_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    fahri_interpreter.BasicExecute(tree, env)
