import ply.yacc as yacc
from lexer_switch import lexer, tokens

# Parsing rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    # Add more precedences if needed
)

def p_switch_statement(p):
    '''switch_statement : SWITCH LPAREN CONSTANT RPAREN LBRACE case_statements DEFAULT COLON statements RBRACE'''
    print("Syntax is valid")
    # Add actions as needed
    pass

def p_case_statements(p):
    '''case_statements : case_statement case_statements
                      | empty'''
    # Add actions as needed
    pass

def p_case_statement(p):
    '''case_statement : CASE CONSTANT COLON statements'''
    # Add actions as needed
    pass

def p_statements(p):
    '''statements : statement statements
                 | empty'''
    # Add actions as needed
    pass

def p_statement(p):
    '''statement : BREAK SEMICOLON
                 | other_statements'''
    # Add actions as needed
    pass

def p_other_statements(p):
    '''other_statements : CONSTANT SEMICOLON
                       | expression SEMICOLON'''
    # Add actions as needed
    pass

def p_expression(p):
    '''expression : NUMBER
                  | BOOLEAN
                  | ID'''
    # Add actions as needed
    pass

def p_empty(p):
    'empty :'
    pass
def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {find_column(p)}: Unexpected token '{p.value}'")
    print("Syntax is not valid")


# Find column number
def find_column(p):
    input_code = lexer.lexdata
    line_start = input_code.rfind('\n', 0, p.lexpos) + 1
    return (p.lexpos - line_start) + 1

# Build the parser
parser = yacc.yacc()

def get_lexer():
    return lexer