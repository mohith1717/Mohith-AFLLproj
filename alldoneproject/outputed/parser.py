from ply import yacc
from lexer import lexer, tokens

def p_statement_output(p):
    'statement : OUTPUT LPAREN output_data RPAREN SEMICOLON'

def p_output_data_string(p):
    'output_data : STRING'
    print("Valid output statement:", p[1])  # Message for valid strings

def p_output_data_number(p):
    'output_data : NUMBER'
    print("Valid output statement:", p[1])  # Message for valid numbers

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        try:
            data = input('Enter an output statement (or type "exit" to quit): ')
            if data == 'exit':
                break
            lexer.input(data)
            for token in lexer:
                pass
            parser.parse(data)
        except EOFError:
            break
