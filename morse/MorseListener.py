# Generated from Morse.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MorseParser import MorseParser
else:
    from MorseParser import MorseParser

# This class defines a complete listener for a parse tree produced by MorseParser.
class MorseListener(ParseTreeListener):
     

    '''# Enter a parse tree produced by MorseParser#morse_code.
    def enterMorse_code(self, ctx:MorseParser.Morse_codeContext):
        pass

    # Exit a parse tree produced by MorseParser#morse_code.
    def exitMorse_code(self, ctx:MorseParser.Morse_codeContext):
        pass


    # Enter a parse tree produced by MorseParser#letter.
    def enterLetter(self, ctx:MorseParser.LetterContext):
        pass

    # Exit a parse tree produced by MorseParser#letter.
    def exitLetter(self, ctx:MorseParser.LetterContext):
        pass


    # Enter a parse tree produced by MorseParser#digit.
    def enterDigit(self, ctx:MorseParser.DigitContext):
        pass

    # Exit a parse tree produced by MorseParser#digit.
    def exitDigit(self, ctx:MorseParser.DigitContext):
        pass'''

class MorseToPythonString(MorseListener):
        def __init__(self):
            self.result = []
        def enterMorse_code(self, ctx:MorseParser.Morse_codeContext):
            pass #print('"', end="")
        def exitMorse_code(self, ctx:MorseParser.Morse_codeContext):
            pass #print('"', end="")
        def enterLetter(self, ctx:MorseParser.LetterContext):
            for child in ctx.getChildren():
                if child.symbol.type == MorseParser.A:
                    self.result.append("a") #print("a", end="")
                if child.symbol.type == MorseParser.B:
                    self.result.append("b") #print("b", end="")
                if child.symbol.type == MorseParser.C:
                    self.result.append("c") #print("c", end="")
                if child.symbol.type == MorseParser.D:
                    self.result.append("d") #print("d", end="")
                if child.symbol.type == MorseParser.E:
                    self.result.append("e") #print("e", end="")
                if child.symbol.type == MorseParser.F:
                    self.result.append("f") #print("f", end="")
                if child.symbol.type == MorseParser.G:
                    self.result.append("g") #print("g", end="")
                if child.symbol.type == MorseParser.H:
                    self.result.append("h") #print("h", end="")
                if child.symbol.type == MorseParser.I:
                    self.result.append("i") #print("i", end="")
                if child.symbol.type == MorseParser.J:
                    self.result.append("j") #print("j", end="")
                if child.symbol.type == MorseParser.K:
                    self.result.append("k") #print("k", end="")
                if child.symbol.type == MorseParser.L:
                    self.result.append("l") #print("l", end="")
                if child.symbol.type == MorseParser.M:
                    self.result.append("m") #print("m", end="")
                if child.symbol.type == MorseParser.N:
                    self.result.append("n") #print("n", end="")
                if child.symbol.type == MorseParser.O:
                    self.result.append("o") #print("o", end="")
                if child.symbol.type == MorseParser.P:
                    self.result.append("p")#print("p", end="")
                if child.symbol.type == MorseParser.Q:
                    self.result.append("q") #print("q", end="")
                if child.symbol.type == MorseParser.R:
                    self.result.append("r") #print("r", end="")
                if child.symbol.type == MorseParser.S:
                    self.result.append("s") #print("s", end="")
                if child.symbol.type == MorseParser.T:
                    self.result.append("t") #print("t", end="")
                if child.symbol.type == MorseParser.U:
                    self.result.append("u") #print("u", end="")
                if child.symbol.type == MorseParser.V:
                    self.result.append("v") #print("v", end="")
                if child.symbol.type == MorseParser.W:
                    self.result.append("w") #print("w", end="")
                if child.symbol.type == MorseParser.X:
                    self.result.append("x") #print("x", end="")
                if child.symbol.type == MorseParser.Y:
                    self.result.append("y") #print("y", end="")
                if child.symbol.type == MorseParser.Z:
                    self.result.append("z") #print("z", end="")

        def enterDigit(self, ctx:MorseParser.LetterContext):
            for child in ctx.getChildren():
                if child.symbol.type == MorseParser.ZERO:
                    self.result.append("0") #print("0", end="")
                if child.symbol.type == MorseParser.ONE:
                    self.result.append("1") #print("1", end="")
                if child.symbol.type == MorseParser.TWO:
                    self.result.append("2") #print("2", end="")
                if child.symbol.type == MorseParser.THREE:
                    self.result.append("3") #print("3", end="") 
                if child.symbol.type == MorseParser.FOUR:
                    self.result.append("4") #print("4", end="")
                if child.symbol.type == MorseParser.FIVE:
                    self.result.append("5") #print("5", end="")
                if child.symbol.type == MorseParser.SIX:
                    self.result.append("6") #print("6", end="")
                if child.symbol.type == MorseParser.SEVEN:
                    self.result.append("7") #print("7", end="")
                if child.symbol.type == MorseParser.EIGHT:
                    self.result.append("8") #print("8", end="")
                if child.symbol.type == MorseParser.NINE:
                    self.result.append("9") #print("9", end="")    
       
        #regresar la traduccion
        def get_translation(self):
            return ''.join(self.result)      


