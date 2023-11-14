import ply.lex as lex

tokens = (
    'TYPE',
    'IDENTIFIER',
    'ASSIGN',
    'SEMICOLON',
)

t_TYPE = r'int|float|string|bool'  # Simplified types
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ASSIGN = r'='
t_SEMICOLON = r';'

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
