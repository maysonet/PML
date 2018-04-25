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
                | command
    """
    try:
        if p[1] == 'NEW':
            Utils.new_project(p[2], p[3])
            # OR we can just accept project name and let the system assign ID
            # Need to fix input rules so that SPACES are allowed in Project name
        if p[1] == 'USER':
            Utils.add_user(p[2])
        if p[1] == 'TASK':
            Utils.add_task(p[2], p[3], p[4])
            # Need to fix input rules so that SPACES are allowed in task description

        if p[1] == 'BRAINSTORM':
            Utils.add_brainstorm(p[2])

        if p[1] == 'IDEA':
            Utils.add_idea(p[2])

        if p[1] == 'DIAGRAM':
            Utils.generate_diagram()

        #The following NEED to be IMPLEMENTED in LEXER and UTILS
        if p[1] == 'GANTT':
            pass
        if p[1] == 'TODAY':
            pass
        if p[1] == 'WEEK':
            pass


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
