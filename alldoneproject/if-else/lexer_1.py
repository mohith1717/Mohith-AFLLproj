import ply.lex as lex

# List of token names
tokens = (
    'ID', 'NUMBER', 'EQUALS', 'GT', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'IF', 'ELSE', 'BOOLEAN', 'SEMICOLON',
)

# Regular expression rules for simple tokens
t_EQUALS = r'=='
t_GT = r'>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'

# Define a rule for ID (variable names)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Define a rule for BOOLEAN (true or false)
def t_BOOLEAN(t):
    r'true|false'
    return t

# Define a rule for NUMBER
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Define a rule for newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Reserved words
reserved = {
    'if': 'IF',
    'else': 'ELSE',
}

lexer = lex.lex()
