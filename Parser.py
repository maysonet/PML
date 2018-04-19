import Utils
import ply.yacc as yacc
import Lexer
tokens = Lexer.tokens

#Parsing Rules
def p_statement(p):
    """
    statement : command NAME ID DATE DATE
                | command uNAME ID
    """
    try:
        if p[1] == 'NEW':
            print(Utils.new_project(p[2], p[3], p[4], p[5]))
        if p[1] == 'ADDuser':
            print(Utils.add_user(p[2], p[3]))

    except:
        print('Invalid Parameters')


def p_command(p):
    """
    command : NAME
    """
    p[0] = p[1]


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
while 1:
    try:
        s = input('PML > ')
    except EOFError:
        break
    if not s:
        continue
    parser.parse(s)
