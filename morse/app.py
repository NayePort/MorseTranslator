from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from antlr4 import *
from MorseLexer import MorseLexer
from MorseParser import MorseParser
#from MorseListener import MorseListener
from MorseListener import MorseToPythonString

origins = ["*"]

app = FastAPI(title = 'Morse Translator Antlr')

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"]
)

class InputData(BaseModel):
    morse_sentence: str

class OutputData(BaseModel):
    result: str

@app.post('/morse', response_model = OutputData)
def morse(data:InputData):

    input_text = data.morse_sentence
    lexer = MorseLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = MorseParser(stream)

    tree = parser.morse_code()

    #listener posonalizado
    listener = MorseToPythonString()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    #print(tree.toStringTree(recog=parser))
    #result = tree.toStringTree(recog=parser)
    result = listener.get_translation()

    return {'result': result}
