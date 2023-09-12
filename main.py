#Angel Vargas
#CPSC 46000 Term Project - GeoJSON Visualizer
#Opens the file and runs the tokenize, parse, and eval functions.
#This visualizer only allows for the primitive geometries.

import re
from lexer import tokenize
from parser import parse
from Eval import eval

def getText(fileName):
    file = open(fileName , "r")
    text = file.read().strip().lower()
    file.close()

    text = re.sub('["]|"|,', "", text)  #replaces quotations or commas with empty strings
    return text

print("Opening file geo.json...")

text = getText("geo.json")
tokens = tokenize(text)
tree = parse(tokens)
eval(tree.getChildren()[0])

