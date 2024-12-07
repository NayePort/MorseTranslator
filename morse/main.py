from antlr4 import *
from MorseLexer import MorseLexer
from MorseParser import MorseParser
#from MorseListener import MorseListener
from MorseListener import MorseToPythonString

input_text = input('> ')
lexer = MorseLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = MorseParser(stream)

tree = parser.morse_code()

#listener posonalizado
listener = MorseToPythonString()

walker = ParseTreeWalker()
walker.walk(listener, tree)

#print(tree.toStringTree(recog=parser))

