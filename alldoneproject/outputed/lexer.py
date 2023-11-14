from ply import lex

tokens = (
    'OUTPUT',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'NUMBER',  # New token for numbers
    'STRING',
)

t_OUTPUT = r'Console\.WriteLine'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
