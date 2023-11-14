import ply.lex as lex

# List of token names
tokens = [
    'SWITCH',
    'CASE',
    'DEFAULT',
    'CONSTANT',
    'ID',
    'NUMBER',
    'BOOLEAN',
    'PLUS',
    'MINUS',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COLON',
    'BREAK',
    'SEMICOLON',
]

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_SEMICOLON = r';'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BOOLEAN(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    return t

def t_CONSTANT(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'switch':
        t.type = 'SWITCH'
    elif t.value == 'case':
        t.type = 'CASE'
    elif t.value == 'default':
        t.type = 'DEFAULT'
    elif t.value == 'break':
        t.type = 'BREAK'
    else:
        t.type = 'CONSTANT'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
