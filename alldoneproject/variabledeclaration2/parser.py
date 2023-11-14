import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'IDENTIFIER',
    'SEMICOLON',
)

reserved = {
    'int': 'INT_TYPE',
    'float': 'FLOAT_TYPE',
    'string': 'STRING_TYPE',
    'bool': 'BOOL_TYPE',
    'char': 'CHAR_TYPE'  # Adding 'char' as a valid type
}

tokens += tuple(reserved.values())

t_SEMICOLON = r';'

t_ignore = ' \t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_statement(p):
    '''statement : variable_declaration SEMICOLON'''
    print("Valid syntax: Variable declaration")
    pass

def p_variable_declaration(p):
    '''variable_declaration : type IDENTIFIER'''
    pass

def p_type(p):
    '''type : INT_TYPE
            | FLOAT_TYPE
            | STRING_TYPE
            | BOOL_TYPE
            | CHAR_TYPE
    '''
    pass

def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

while True:
    user_input = input("Enter variable initialization (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

    lexer.input(user_input)
    for token in lexer:
        pass  # To consume tokens without printing
    parser.parse(user_input)
