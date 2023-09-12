#Angel Vargas
#CPSC 46000 Term Project - GeoJSON Visualizer
# Uses ply.lex to perform lexical analysis on the text given in a JSON format.
import ply.lex as lex

def tokenize(text):
    tokens = (
        'ID',
        'VALUE',
        'COORD',
        'LBRACE',
        'RBRACE',
        'LBRACKET',
        'RBRACKET',
    )

    #simple grammar
    t_LBRACE = r"\{"
    t_RBRACE = r"\}"
    t_LBRACKET = r"\["
    t_RBRACKET = r"\]"

    def t_ID(t):
        r"\w+:"     #any characher followed by ':'
        return t
    
    def t_VALUE(t):
        r"[a-z]+\d?"    # any letters optional digits
        return t
    
    def t_COORD(t):
        r"\d+\.?\d+"    #numbers with optional decimals
        return t
    
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    t_ignore = ' \t'
    
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    
    lexer = lex.lex()
    lexer.input(text)

    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)  #list of all the tokens

    return tokens