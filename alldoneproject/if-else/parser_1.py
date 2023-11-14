

import ply.yacc as yacc
from lexer_1 import tokens

# Parsing rules


def p_start(p):
    '''start : statements'''
    p[0] = p[1]
    print("Valid syntax")


def p_statements(p):
    '''statements : statement statements
                  | empty'''
    pass


def p_statement(p):
    '''statement : IF LPAREN expression RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE
                 | ID EQUALS expression SEMICOLON'''
    pass


def p_expression(p):
    '''expression : expression GT expression
                  | BOOLEAN
                  | ID'''
    pass


def p_empty(p):
    'empty :'
    pass

# Error handling rule


def p_error(p):
    if p:
        print(
            f"Syntax error at line {p.lineno}, position {find_column(p)}: Unexpected token '{p.value}'")
    else:
        print("Syntax error: Unexpected end of input")

# Find column position of the token


def find_column(p):
    last_cr = p.lexer.lexdata.rfind('\n', 0, p.lexpos)
    return (p.lexpos - last_cr)


# Build the parser
parser = yacc.yacc()

# Test the parser


def parse_input(input_code):
    result = parser.parse(input_code)
    return result


if __name__ == '__main__':
    input_code = input("Enter C code with if-else statements:\n")
    parse_input(input_code)
