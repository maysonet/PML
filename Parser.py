import Utils
import ply.yacc as yacc
import Lexer
tokens = Lexer.tokens

#Parsing Rules
def p_statement(p):
    """
    statement : command NAME ID
                | command NAME DATE DATE
                | command NAME
    """
    try:
        if p[1] == 'NEW':
            print(Utils.new_project(p[2], p[3]))
        if p[1] == 'USER':
            print(Utils.add_user(p[2]))
        if p[1] == 'TASK':
            print(Utils.add_task(p[2], p[3], p[4]))

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
