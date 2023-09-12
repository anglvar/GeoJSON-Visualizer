#Angel Vargas
#CPSC 46000 Term Project - GeoJSON Visualizer
#Parses the tokens and returns and AST

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def getValue(self):
        return self.value
    def getChildren(self):
        return self.children
    def setChild(self, child):
        self.children.append(child)

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    
def parse(tokens):
    stack = Stack()
    current = Node("file")      #parent node 

    for i in range(0, len(tokens)):
        if tokens[i].type == "LBRACE":      #if "{"
            # { --> ID
            if tokens[i + 1].type == "ID":
                stack.push(current)
            else:
                print("Error on line: ", tokens[i + 1].lineno)
                break
        elif tokens[i].type == "LBRACKET":  #if "["
            # [ --> {
            # [ --> [
            # [ --> COORD
            if tokens[i + 1].type == "LBRACE" or tokens[i + 1].type == "LBRACKET" or tokens[i + 1].type == "COORD":
                stack.push(current)
            else:
                print("Error on line: ", tokens[i + 1].lineno)
                break
        elif tokens[i].type == "ID":
            # ID --> {
            # ID --> [
            # ID --> VALUE
            if tokens[i + 1].type == "LBRACE" or tokens[i + 1].type == "LBRACKET" or tokens[i + 1].type == "VALUE":
                current = setCurrent(tokens[i], current)    #creates a child for current and sets it as current
                if tokens[i].value == "geometry:":
                    stack.push(current)
            else:
                print("Error on line: ", tokens[i + 1].lineno)  
                break      
        elif tokens[i].type == "VALUE":
            # VALUE --> ID
            # VALUE --> }
            if tokens[i + 1].type == "ID" or tokens[i + 1].type == "RBRACE":    #correct grammar
                current = setCurrent(tokens[i], current)
            else:
                print("Error on line: ", tokens[i + 1].lineno)  
                break
        elif tokens[i].type == "COORD":
            # COORD --> ]       -no more coordinates
            # COORD --> COORD   -additional coordinates
            if tokens[i + 1].type == "RBRACKET":
                node = Node(tokens[i])
                current.setChild(node)
                current = stack.pop()
            elif tokens[i + 1].type == "COORD":
                node = Node(tokens[i])
                current.setChild(node)
            else:
                print("Error on line: ", tokens[i + 1].lineno)
                break
        elif tokens[i].type == "RBRACKET":      #if "]" 
            # ] --> ]
            # ] --> }
            # ] --> [       -more than one coordinates
            if tokens[i + 1].type == "RBRACKET" or tokens[i + 1].type == "RBRACE":
                if not stack.isEmpty():
                    current = stack.pop()
            elif tokens[i + 1].type =="LBRACKET": 
                current = stack.pop()
                stack.push(current)
            else:
                print("Error on line: ", tokens[i + 1].lineno)
                break
        elif tokens[i].type == "RBRACE":        #if "}"
            # } --> }
            # } --> { 
            # } --> ]
            # } --> ID
            if not i == len(tokens) - 1:    #if it's the last token
                if tokens[i + 1].type == "RBRACE" or tokens[i + 1].type == "LBRACE" or tokens[i + 1].type == "RBRACKET" or tokens[i + 1].type == "ID":
                    if not stack.isEmpty():
                        current = stack.pop()
                else:
                    print("Error on line: ", tokens[i + 1].lineno)   
                    break   
        else:
            print("Something went wrong.")

    while not stack.isEmpty():
        current = stack.pop()       #return current to the parent node
    return current

def setCurrent(token, current):     #creates a child for current and sets current to that child
    node = Node(token)
    current.setChild(node)
    return node