from parser_switch import parser, get_lexer

def check_syntax(input_code):
    parser.parse(input_code, lexer=get_lexer())

if __name__ == "__main__":
    input_code = input("Enter C code with switch statement: ")
    check_syntax(input_code)
